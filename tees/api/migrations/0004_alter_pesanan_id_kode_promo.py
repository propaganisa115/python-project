# Generated by Django 4.0.1 on 2022-01-15 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_pesanan_total_pesanan_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pesanan',
            name='id_kode_promo',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
