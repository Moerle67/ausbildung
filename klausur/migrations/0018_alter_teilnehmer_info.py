# Generated by Django 4.2.7 on 2024-04-02 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klausur', '0017_remove_teilnehmer_nummer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teilnehmer',
            name='info',
            field=models.TextField(blank=True, null=True, verbose_name='Infos'),
        ),
    ]
