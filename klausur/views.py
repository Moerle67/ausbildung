import datetime
from django.http import Http404
from django.shortcuts import render
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

def gen_pdf(request, id):
    fragen = Klausurthema.objects.filter(klausur=id)
    klausur = Klausur.objects.get(pk=id)
    thema = klausur.titel
    punkte = klausur.get_gesamtpunkte
    termin = klausur.termin.date()
    context = {
        'termin': termin,
        'punkte': punkte,
        'thema': thema,
        'fragen': fragen,
    }
    response = renderers.render_to_pdf("pdfs/klausur_gen.html", context)
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