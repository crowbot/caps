# Generated by Django 2.2.8 on 2020-10-19 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caps', '0007_auto_20201019_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plandocument',
            name='url',
            field=models.URLField(max_length=600),
        ),
    ]
