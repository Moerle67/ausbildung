import datetime
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from .models import *

import locale

from . import renderers

locale.setlocale(locale.LC_ALL, "")
# Create your views here.

def pdf_view(self, request, *args, **kwargs):
    data = {
        'today': datetime.date.today(),
        'amount': 39.99,
        'customer_name': 'Cooper Mann',
        'invoice_number': 1233434,
    }
    return renderers.render_to_pdf('pdfs/invoice.html', data)

def advanced_pdf_view(request):
    thema = "Testklausur"
    fragen = Frage.objects.all()
    context = {
        'thema': thema,
        'fragen': fragen,
    }
    response = renderers.render_to_pdf("pdfs/klausur.html", context)
    if response.status_code == 404:
        raise Http404("Invoice not found")

    filename = f"Klausur_{thema}.pdf"
    """
    Tell browser to view inline (default)
    """
    content = f"inline; filename={filename}"
    download = request.GET.get("download")
    if download:
        """
        Tells browser to initiate download
        """
        content = f"attachment; filename={filename}"
    response["Content-Disposition"] = content
    return response

def gen_pdf(request, id, typ):
    # fragen = Klausurthema.objects.filter(klausur=id)
    # typ 1 - Klausur, 
    #     2 - Muster
    #     3 - Sort Fragen
    klausur = Klausur.objects.get(pk=id)
    if typ == 1 or typ == 2:
        fragen = klausur.fragen.all()
    elif typ == 3:
        fragen = []
        pfragen = Klausurthema.objects.filter(klausur=klausur)
        for pfrage in pfragen:
            fragen.append(pfrage.frage)
    thema = klausur.titel
    punkte = klausur.get_gesamtpunkte
    termin = klausur.termin.date()
    context = {
        'klausur': klausur,
        'fragen': fragen,
        'termin': termin,
        'punkte': punkte,
        'thema': thema,
    }
    if typ == 1 or typ == 3: # Klausur
        response = renderers.render_to_pdf("pdfs/klausur_gen.html", context)
    elif typ == 2: # Muster
        response = renderers.render_to_pdf("pdfs/muster_gen.html", context)        
    
    if response.status_code == 404:
        raise Http404("Invoice not found")

    filename = f"Klausur_{thema}.pdf"
    """
    Tell browser to view inline (default)
    """
    content = f"inline; filename={filename}"
    download = request.GET.get("download")
    if download:
        """
        Tells browser to initiate download
        """
        content = f"attachment; filename={filename}"
    response["Content-Disposition"] = content
    return response

def klaus_design(request, id):
    klausur = Klausur.objects.get(pk=id)
    fragen = klausur.fragen.all()
    i = 0
    # Fragen eintragen
    for frage in fragen:
        position, created = Klausurthema.objects.get_or_create(klausur = klausur, frage=frage)
        if created:
            position.position = i
            position.save()
        
        i +=1

    # Datenbank leeren
    fragen = Klausurthema.objects.filter(klausur=klausur)
    print(fragen)
    for frage in fragen:
        fragek = klausur.fragen.filter(frage=frage)
        print(fragek)
    pos_fragen = Klausurthema.objects.filter(klausur = klausur)
    content = {
        'klausur': klausur,
        'fragen': pos_fragen,
    }
    return render(request, "design.html", content)

def richtung(request, klausur, frage, richtung):
    klausur = Klausur.objects.get(pk=klausur)
    frage = Frage.objects.get(pk=frage)
    position = Klausurthema.objects.get(klausur=klausur, frage=frage)
    if richtung==1 :
        position.position += 1
    elif richtung==2:
        position.position -= 1
    position.save()
    return redirect("/klausur/design/"+str(klausur.pk))
