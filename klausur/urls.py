from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.advanced_pdf_view, name= 'test'),
    path('g_pdf/<int:id>', views.gen_pdf, name= 'gen_pdf'),
]