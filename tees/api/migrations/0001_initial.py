# Generated by Django 4.0.1 on 2022-01-15 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detail_Pesanan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_product', models.IntegerField(default=None)),
                ('qty', models.IntegerField(default=None)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Kode_promo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kode_promo', models.IntegerField(default=None)),
                ('persentase_diskon', models.IntegerField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='Pembeli',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.DateTimeField(blank=True, null=True)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Penjual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default=None, max_length=100)),
                ('name', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pesanan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waktu_pemesanan', models.CharField(max_length=100)),
                ('total_pesanan', models.DecimalField(decimal_places=2, max_digits=6)),
                ('status_pesanan', models.CharField(choices=[('Belum diproses', 'Belum diproses'), ('Packing', 'Packing'), ('Kirim', 'Kirim'), ('Selesai', 'Selesai')], default='Belum diproses', max_length=20, null=True)),
                ('id_kode_promo', models.IntegerField(default=None)),
                ('pembeli_id', models.IntegerField(default=None)),
                ('total_pesanan_akhir', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(max_length=200)),
                ('image', models.CharField(blank=True, default=None, max_length=300)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('penjual_id', models.IntegerField(default=None)),
            ],
        ),
    ]
