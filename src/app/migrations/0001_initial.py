# Generated by Django 3.2.7 on 2021-09-30 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fascicolo',
            fields=[
                ('id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('anno', models.IntegerField(default=0)),
                ('progressivo', models.IntegerField(default=0)),
                ('titolo', models.CharField(max_length=200)),
            ],
        ),
    ]
