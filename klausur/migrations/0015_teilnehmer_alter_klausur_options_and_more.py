# Generated by Django 4.2.7 on 2024-04-02 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klausur', '0014_alter_klausur_options_frage_bildmuster'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teilnehmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
                ('nummer', models.IntegerField(verbose_name='Nummer')),
                ('info', models.TextField(verbose_name='Info')),
            ],
            options={
                'verbose_name': 'Teilnehmer',
                'verbose_name_plural': 'Teilnehmers',
            },
        ),
        migrations.AlterModelOptions(
            name='klausur',
            options={'verbose_name': 'Klausur', 'verbose_name_plural': 'Klausuren'},
        ),
        migrations.RemoveField(
            model_name='klausur',
            name='fragen',
        ),
        migrations.RemoveField(
            model_name='klausur',
            name='gruppe',
        ),
        migrations.CreateModel(
            name='Gruppe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Bezeichnung')),
                ('teilnehmer', models.ManyToManyField(to='klausur.teilnehmer', verbose_name='Teilnehmer')),
            ],
            options={
                'verbose_name': 'Gruppe',
                'verbose_name_plural': 'Gruppen',
            },
        ),
        migrations.AddField(
            model_name='klausur',
            name='gruppe',
            field=models.ManyToManyField(null=True, to='klausur.frage', verbose_name='Fragen'),
        ),
    ]
