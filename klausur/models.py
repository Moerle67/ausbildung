from datetime import date
from django.db import models

# Create your models here.
class Thema(models.Model):
    titel = models.CharField(("Titel"), max_length=250, primary_key=True)
    kommentar = models.TextField(("Kommentar"), blank=True, null=True)
    

    class Meta:
        verbose_name = ("Thema")
        verbose_name_plural = ("Themas")
        ordering = ['titel']
    
    def __str__(self):
        return self.titel

    def get_absolute_url(self):
        return reverse("Thema_detail", kwargs={"pk": self.pk})


class Frage(models.Model):
    titel = models.CharField(("Titel"), max_length=250)
    inhalt = models.CharField("Inhalt", max_length=50, default="?")
    frage = models.TextField(("Frage"))
    musterantwort = models.TextField(("Musterantwort"), default ="")
    bild = models.ImageField(("Bild"), blank=True, null=True)
    bildmuster = models.ImageField(("Bild Muster"), blank=True, null=True)
    bildbreite = models.IntegerField(("Bildbreite in %"), default=80)
    thema = models.ForeignKey(Thema, verbose_name=("Thema"), on_delete=models.RESTRICT)
    punkte = models.IntegerField(("Erreichbare Punkte"), default=1)
#    platz = models.IntegerField(("Platz"), default=2)
    schwierigkeit = models.IntegerField(("Schwierigkeit") , default=2)
    class Meta:
        verbose_name = ("Frage")
        verbose_name_plural = ("Fragen")
        ordering = ['thema', 'titel', ]

    def __str__(self):
        return f"{self.titel}/{self.inhalt} ({self.thema} ({self.punkte} Punkte))"

    def get_absolute_url(self):
        return reverse("Fragen_detail", kwargs={"pk": self.pk})

class Klausur(models.Model):
    titel = models.CharField(("Titel"), max_length=50)
    thema = models.CharField(("Thema"), max_length=50)
    termin = models.DateTimeField(("termin"), auto_now=False, auto_now_add=False)
    gruppe = models.CharField(("Gruppe"), max_length=50)
    fragen = models.ManyToManyField(Frage, verbose_name=("Fragen"))

    @property
    def get_gesamtpunkte(self):
        fragen = self.fragen.all()
        gesamtpunkte = sum(frage.punkte for frage in fragen)
        return gesamtpunkte

    @property
    def get_aktiv(self):
        if self.termin > date.today():
            return True
        else:
            return False
            
    class Meta:
        verbose_name = ("Klausur")
        verbose_name_plural = ("Klausuren")
        ordering = [ 'gruppe', '-termin']

    def __str__(self):
        return f"{self.gruppe} - {self.titel}/{self.termin.date()}/{self.get_gesamtpunkte} Punkte"

    def get_absolute_url(self):
        return reverse("Klausur_detail", kwargs={"pk": self.pk})
    


class Klausurthema(models.Model):
    klausur = models.ForeignKey(Klausur, verbose_name=("Klausur"), on_delete=models.CASCADE)
    frage = models.ForeignKey(Frage, verbose_name=("Frage"), on_delete=models.RESTRICT)
    position = models.IntegerField(("Position"), default=1)
    seitenwechsel = models.BooleanField(("Seitenwechsel im Anschluss"), default=False)
    class Meta:
        verbose_name = ("Klausur-Thema")
        verbose_name_plural = ("Klausur-Themen")
        ordering = ['klausur', 'position']

    def __str__(self):
        return f"{self.klausur}/{self.frage}({self.frage.punkte} Punkte)"

    def get_absolute_url(self):
        return reverse("KlausurThema_detail", kwargs={"pk": self.pk})

