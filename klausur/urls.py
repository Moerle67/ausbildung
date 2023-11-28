from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.advanced_pdf_view, name= 'test'),
    path('g_pdf/<int:id>/<int:typ>', views.gen_pdf, name= 'gen_pdf'),
    path('design/<int:id>', views.klaus_design, name= 'klausur_design'),
    path('pos/<int:klausur>/<int:frage>/<int:richtung>', views.richtung, name= 'richtung'),
]