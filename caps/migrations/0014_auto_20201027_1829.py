# Generated by Django 2.2.8 on 2020-10-27 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caps', '0013_auto_20201023_1749'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='council',
            options={'ordering': ['name']},
        ),
    ]