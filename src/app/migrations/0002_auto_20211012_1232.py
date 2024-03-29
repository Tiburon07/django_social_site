# Generated by Django 3.2.8 on 2021-10-12 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('codice_fiscale', models.CharField(max_length=16)),
                ('cognome', models.CharField(max_length=200)),
                ('nome', models.CharField(max_length=200)),
                ('data_nascita', models.DateField()),
                ('luogo_nascita', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Fascicolo',
        ),
    ]
