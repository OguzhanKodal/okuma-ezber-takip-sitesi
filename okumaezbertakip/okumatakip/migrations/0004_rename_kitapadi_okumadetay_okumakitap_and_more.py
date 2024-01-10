# Generated by Django 4.2.6 on 2024-01-04 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('okumatakip', '0003_alter_okumadetay_toplamsayfa_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='okumadetay',
            old_name='kitapAdi',
            new_name='okumaKitap',
        ),
        migrations.RenameField(
            model_name='okumadetay',
            old_name='kitapAldigiTarih',
            new_name='okumayaBasladigiTarih',
        ),
        migrations.RemoveField(
            model_name='okumadetay',
            name='toplamsayfa',
        ),
        migrations.RemoveField(
            model_name='okumatakip',
            name='okumasayfa',
        ),
        migrations.AddField(
            model_name='okumadetay',
            name='kullanici',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='kullanici', to='okumatakip.okumatakip'),
        ),
        migrations.AddField(
            model_name='okumadetay',
            name='okumaSayfa',
            field=models.IntegerField(null=True),
        ),
    ]
