# Generated by Django 3.2.8 on 2021-10-14 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_documentobacheca_nome'),
    ]

    operations = [
        migrations.CreateModel(
            name='PermessiPagine',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('url', models.CharField(max_length=200)),
                ('permessi', models.CharField(max_length=200)),
            ],
        ),
    ]
