# Generated by Django 3.2.8 on 2021-10-14 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20211013_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentobacheca',
            name='permessi',
            field=models.CharField(default='Procura', max_length=200),
            preserve_default=False,
        ),
    ]
