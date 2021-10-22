# Generated by Django 3.2.8 on 2021-10-18 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('app', '0011_auto_20211018_1057'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupLabel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=200)),
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
            ],
        ),
    ]
