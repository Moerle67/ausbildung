from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *

# Register your models here.
# admin.site.register(Frage)
admin.site.register(Thema)
#admin.site.register(Klausur)
#admin.site.register(Klausurthema)

@admin.action(description="PDF generieren")
def pdf_generate(modeladmin, request, queryset):
    for klausur in queryset:
        return HttpResponseRedirect(f"/klausur/g_pdf/{klausur.pk}")


@admin.register(Frage)
class FrageAdmin(admin.ModelAdmin):
    list_filter = ['thema']

@admin.register(Klausurthema)
class KlausurthemaAdmin(admin.ModelAdmin):
    list_filter = ['klausur']

@admin.register(Klausur)
class KlausurAdmin(admin.ModelAdmin):
    list_filter = ['gruppe']
    actions = [pdf_generate]

