import datetime
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from .models import Klausur, Klausurthema, Frage

import locale, random

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
    #     3 - Design Fragen
    #     4 - Design Muster
    klausur = Klausur.objects.get(pk=id)
    fragen = []
    if typ == 1 or typ == 2:
        pfragen = klausur.fragen.all()
        for pfrage in pfragen:
            fragen.append((pfrage, False))
    elif typ == 3 or typ == 4:
        pfragen = Klausurthema.objects.filter(klausur=klausur)
        for pfrage in pfragen:
            fragen.append((pfrage.frage,pfrage.seitenwechsel))
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
    elif typ == 2 or typ == 4: # Muster
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
    # print(fragen)
    for frage in fragen:
        if not klausur.fragen.filter(id=frage.frage.id).exists():
            Klausurthema.objects.get(frage=frage.frage, klausur=klausur).delete()
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
        position.position += 2
    elif richtung==2:
        position.position -= 2
    position.save()
    return redirect("/klausur/design/"+str(klausur.pk))

def zufall(request, klausur):
    lst = list(range(len(Klausurthema.objects.filter(klausur = Klausur.objects.get(pk=klausur)))))
    fragen = Klausurthema.objects.filter(klausur=Klausur.objects.get(pk=klausur))
    for frage in fragen:
        pos = random.choice(lst)
        lst.remove(pos)
        frage.position=pos
        frage.save()
    return redirect("/klausur/design/"+str(klausur))

def newside(request, klausur):    
    frage=request.POST['nl']
    if frage == "gen":
        gen_pdf(request, klausur, 3)
    else:    
        ds = Klausurthema.objects.get(id=frage)
        ds.seitenwechsel = not ds.seitenwechsel
        ds.save()
        print(ds.frage)
    return redirect("/klausur/design/"+str(klausur))
