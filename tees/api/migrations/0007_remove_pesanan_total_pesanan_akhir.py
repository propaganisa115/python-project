# Generated by Django 4.0.1 on 2022-01-16 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_detail_pesanan_price_alter_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pesanan',
            name='total_pesanan_akhir',
        ),
    ]
