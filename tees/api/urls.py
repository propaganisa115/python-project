from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework_simplejwt import views as jwt_views
from .Pembeli.api import PembeliListView, PembeliRetrieveUpdateView, PembeliCreateView
from .Keranjang.api import KeranjangListView, KeranjangCreateView, KeranjangRetrieveUpdateView, KeranjangByPembeliView
from .Pesanan.api import PesananListView, PesananDetailListView, PesananUpdateStatusView
from .Product.api import ProductListView, ProductCreateView, ProductRetrieveUpdateView
from .KodePromo.api import KodePromoCreateView, KodePromoRetrieveUpdateView,KodePromoListView
from .Penjual.api import PenjualRetrieveUpdateView, PenjualListView,PenjualCreateView


urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('pesanan/', PesananListView.as_view(),name='list_pesanan'),
    path('pesanan_detail/<int:pk>', PesananDetailListView.as_view(),name='pesanan_detail'),
    path('pesanan/status', PesananUpdateStatusView.as_view(), name='update_status_pesanan'),

    path('penjual', PenjualListView.as_view(), name='list_penjual'),
    path('penjual/create', PenjualCreateView.as_view(),name='create_penjual'),
    path('penjual/<int:pk>', PenjualRetrieveUpdateView.as_view(),name='retireve_penjual'),

    path('product', ProductListView.as_view(),name='list_product'),
    path('product/create', ProductCreateView.as_view(),name='create_product'),
    path('product/<int:pk>', ProductRetrieveUpdateView.as_view(),name='retrieve_update_product'),

    path('kode_promo', KodePromoListView.as_view(),name='list_kode_promo'),
    path('kode_promo/create', KodePromoCreateView.as_view(),name='create_kode_promo'),
    path('kode_promo/<int:pk>', KodePromoRetrieveUpdateView.as_view(),name='retrieve_update_kode_promo'),

    path('pembeli', PembeliListView.as_view(), name='list_pembeli'),
    path('pembeli/create', PembeliCreateView.as_view(),name='create_pembeli'),
    path('pembeli/<int:pk>', PembeliRetrieveUpdateView.as_view(),name='retrieve_update_pembeli'),

    path('keranjang', KeranjangListView.as_view(), name='list_keranjang'),
    path('keranjang/create', KeranjangCreateView.as_view(),name='create_keranjang'),
    path('keranjang/<int:pk>', KeranjangRetrieveUpdateView.as_view(),name='retrieve_update_keranjang'),
    path('keranjang/pembeli/<int:pk>', KeranjangByPembeliView.as_view(),name='list_keranjang_by_pembeli'),

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
