# Generated by Django 4.2.6 on 2023-12-31 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='okumadetay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kitapAdi', models.CharField(max_length=20)),
                ('kitapAldigiTarih', models.DateField(null=True)),
                ('toplamsayfa', models.IntegerField(default='VarsayilanDeger')),
            ],
        ),
        migrations.CreateModel(
            name='okumatakip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talebeno', models.CharField(max_length=15)),
                ('ad', models.CharField(max_length=15)),
                ('soyad', models.CharField(max_length=15)),
                ('okumasayfa', models.IntegerField(default='VarsayilanDeger')),
                ('kayittarihi', models.DateField(null=True)),
                ('aktiflik', models.BooleanField(null=True)),
            ],
        ),
    ]
