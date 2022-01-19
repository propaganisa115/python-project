from django.contrib import admin
from .models import Pesanan, Detail_Pesanan, Penjual, Product, Pembeli

admin.site.register(Pesanan)
admin.site.register(Detail_Pesanan)
admin.site.register(Penjual)
admin.site.register(Product)
admin.site.register(Pembeli)