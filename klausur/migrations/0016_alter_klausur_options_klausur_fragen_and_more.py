# Generated by Django 4.2.7 on 2024-04-02 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('klausur', '0015_teilnehmer_alter_klausur_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='klausur',
            options={'ordering': ['gruppe', '-termin'], 'verbose_name': 'Klausur', 'verbose_name_plural': 'Klausuren'},
        ),
        migrations.AddField(
            model_name='klausur',
            name='fragen',
            field=models.ManyToManyField(to='klausur.frage', verbose_name='Fragen'),
        ),
        migrations.RemoveField(
            model_name='klausur',
            name='gruppe',
        ),
        migrations.AlterField(
            model_name='teilnehmer',
            name='info',
            field=models.TextField(verbose_name='Infos'),
        ),
        migrations.AddField(
            model_name='klausur',
            name='gruppe',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='klausur.gruppe', verbose_name='Gruppe'),
        ),
    ]
