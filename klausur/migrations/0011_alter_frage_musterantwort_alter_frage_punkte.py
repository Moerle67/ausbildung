# Generated by Django 4.2.7 on 2023-11-26 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klausur', '0010_rename_frage_klausur_fragen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frage',
            name='musterantwort',
            field=models.TextField(default='', verbose_name='Musterantwort'),
        ),
        migrations.AlterField(
            model_name='frage',
            name='punkte',
            field=models.IntegerField(default=1, verbose_name='Erreichbare Punkte'),
        ),
    ]
