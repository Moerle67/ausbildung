# Generated by Django 4.2.7 on 2023-12-01 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klausur', '0012_remove_frage_platz_alter_klausurthema_position_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='frage',
            name='bildbreite',
            field=models.IntegerField(default=80, verbose_name='Bildbreite in %'),
        ),
    ]
