# Generated by Django 4.2.7 on 2023-11-20 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('klausur', '0004_alter_frage_titel_alter_thema_titel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Klausur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=50, verbose_name='Titel')),
                ('thema', models.CharField(max_length=50, verbose_name='Thema')),
                ('termin', models.DateTimeField(verbose_name='termin')),
                ('gruppe', models.CharField(max_length=50, verbose_name='Gruppe')),
            ],
            options={
                'verbose_name': 'Klausur',
                'verbose_name_plural': 'Klausur',
            },
        ),
        migrations.CreateModel(
            name='KlausurThema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(verbose_name='Position')),
                ('seitenwechsel', models.BooleanField(verbose_name='Seitenwechsel im Anschluss')),
                ('frage', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='klausur.frage', verbose_name='Frage')),
                ('klausur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='klausur.klausur', verbose_name='Klausur')),
            ],
            options={
                'verbose_name': 'KlausurThema',
                'verbose_name_plural': 'KlausurThemas',
                'ordering': ['klausur', 'position'],
            },
        ),
    ]
