# Generated by Django 2.2.8 on 2020-11-06 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caps', '0023_council_related_authorities'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='council',
            name='related_authorities',
        ),
        migrations.AddField(
            model_name='council',
            name='related_councils',
            field=models.ManyToManyField(blank=True, related_name='_council_related_councils_+', to='caps.Council'),
        ),
    ]