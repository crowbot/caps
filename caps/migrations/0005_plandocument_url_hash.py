# Generated by Django 2.2.8 on 2020-10-19 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caps', '0004_auto_20201019_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='plandocument',
            name='url_hash',
            field=models.CharField(max_length=7),
            preserve_default=False,
        ),
    ]