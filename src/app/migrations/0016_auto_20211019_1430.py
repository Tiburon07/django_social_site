# Generated by Django 3.2.8 on 2021-10-19 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20211019_1420'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descrizione', models.CharField(max_length=200)),
                ('giorni', models.IntegerField(default=0)),
                ('codice', models.IntegerField(default=0)),
                ('livello', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Tipo Documento',
                'verbose_name_plural': 'Tipi Documento',
            },
        ),
        migrations.AlterModelOptions(
            name='permessipagine',
            options={'verbose_name': 'Permessi Pagina', 'verbose_name_plural': 'Permessi Pagina'},
        ),
        migrations.AlterModelOptions(
            name='relutentefsn',
            options={'verbose_name': 'Relazione Utente/Federazione', 'verbose_name_plural': 'Relazioni Utente/Federazione'},
        ),
        migrations.AlterModelOptions(
            name='statofascicolo',
            options={'verbose_name': 'Stato Fascicolo', 'verbose_name_plural': 'Stati Fascicolo'},
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letto', models.BooleanField()),
                ('fascicolo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.fascicolo')),
                ('tipo_documento', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='app.tipodocumento')),
            ],
            options={
                'verbose_name': 'Documento',
                'verbose_name_plural': 'Documenti',
            },
        ),
    ]
