# Generated by Django 4.0.1 on 2022-01-16 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_detail_pesanan_id_pesanan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail_pesanan',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=20, null=True),
        ),
    ]
