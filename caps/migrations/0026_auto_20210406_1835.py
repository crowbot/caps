# Generated by Django 2.2.8 on 2021-04-06 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('caps', '0025_auto_20201112_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='council',
            name='combined_authority',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='caps.Council'),
        ),
    ]