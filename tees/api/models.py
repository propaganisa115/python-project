from django.db import models
from django.utils.timezone import now
# Create your models here.

class Pembeli(models.Model):
    email=models.CharField(max_length=100,blank=True, null=True)
    name=models.CharField(max_length=200)
    phone= models.CharField(max_length=20)
    address = models.CharField(max_length=300)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=now, blank=True, null=True)

class Penjual(models.Model):
    email=models.CharField(max_length=100)
    name=models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=now, blank=True, null=True)

class Product(models.Model):
    email=models.CharField(max_length=100,blank=True,null=True)
    name= models.CharField(max_length=200)
    image= models.CharField(max_length=300,blank=True,default=None,null=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    penjual_id =  models.IntegerField()
    created_at = models.DateTimeField(default=now, blank=True, null=True)

class Pesanan(models.Model):
    STATUS_CHOICES = (
        ('Belum diproses', 'Belum diproses'),
        ('Packing', 'Packing'),
        ('Kirim', 'Kirim'),
        ('Selesai', 'Selesai'),
    )
    waktu_pemesanan= models.DateTimeField(default=now, blank=True, null=True)
    total_pesanan= models.DecimalField(max_digits=20, decimal_places=2,blank=True, default=0,null=True)
    status_pesanan= models.CharField(max_length=20, choices=STATUS_CHOICES ,default='Belum diproses',null=True)
    id_kode_promo = models.IntegerField(blank=True, null=True)
    pembeli_id= models.IntegerField()

class Detail_Pesanan(models.Model):
    id_pesanan = models.IntegerField()
    id_product=models.IntegerField()
    qty= models.IntegerField()
    price= models.DecimalField(max_digits=20, decimal_places=2,blank=True, default=0,null=True)
    created_at = models.DateTimeField(default=now, blank=True, null=True)

class Kode_promo(models.Model):
    kode_promo=models.CharField(max_length=50)
    persentase_diskon= models.IntegerField()
    deskripsi = models.CharField(max_length=300)
    created_at = models.DateTimeField(default=now, blank=True, null=True)

class Keranjang(models.Model):
    id_product=models.IntegerField()
    qty= models.IntegerField()
    pembeli_id= models.IntegerField()
    created_at = models.DateTimeField(default=now, blank=True, null=True)