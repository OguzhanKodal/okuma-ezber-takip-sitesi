# Generated by Django 4.2.6 on 2023-12-31 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('okumatakip', '0002_alter_okumadetay_toplamsayfa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='okumadetay',
            name='toplamsayfa',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='okumatakip',
            name='okumasayfa',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
