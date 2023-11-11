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
    frage = models.TextField(("Frage"))
    musterantwort = models.TextField(("Musterantwort"))
    bild = models.ImageField(("Bild"), blank=True, null=True)
    thema = models.ForeignKey(Thema, verbose_name=("Thema"), on_delete=models.RESTRICT)
    punkte = models.IntegerField(("Erreichbare Punkte"))
    platz = models.IntegerField(("Platz"), default=2)
    schwierigkeit = models.IntegerField(("Schwierigkeit") , default=2)
    class Meta:
        verbose_name = ("Frage")
        verbose_name_plural = ("Fragen")
        ordering = ['thema', 'titel', ]

    def __str__(self):
        return f"{self.titel} ({self.thema})"

    def get_absolute_url(self):
        return reverse("Fragen_detail", kwargs={"pk": self.pk})

