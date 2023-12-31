# Generated by Django 4.2.6 on 2023-12-31 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ezberdetay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ezberAdi', models.CharField(max_length=20)),
                ('ezbereBasladiğiTarih', models.DateField(null=True)),
                ('toplamezber', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ezbertakip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talebeno', models.IntegerField(default=0)),
                ('ad', models.CharField(max_length=15)),
                ('soyad', models.CharField(max_length=15)),
                ('ezber', models.CharField(default='VarsayilanDeger', max_length=255)),
                ('kayittarihi', models.DateField(null=True)),
                ('aktiflik', models.BooleanField(null=True)),
            ],
        ),
    ]
