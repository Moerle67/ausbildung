# Generated by Django 4.2.7 on 2024-04-04 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('klausur', '0022_alter_answer_punkte'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gruppe',
            options={'ordering': ['name'], 'verbose_name': 'Gruppe', 'verbose_name_plural': 'Gruppen'},
        ),
    ]