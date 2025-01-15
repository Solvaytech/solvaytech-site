from django.urls import path, re_path
from apps.home import views
from .views import ContactAPI, NewsAPI, TeklifAPI

urlpatterns = [

    # The home page
    path('', views.serveIndex, name='home'),
    path('admin', views.Admin, name='admin'),
    path('webp', views.webpIndex, name="webp"),
    path('cerez-politikasi', views.cerezIndex, name="cookie-policy"),
    path('kvkk-aydinlatma', views.kvkkPDFServe, name="kvkk-pdf"),
    path('kisisel-bilgi-basvuru', views.kisielBilgiBasvuruPDFServe, name="basvuru-pdf"),
    path('blog', views.blogIndex, name="blog"),
    path('about', views.aboutServe, name="about"),
    path('about/esitlik', views.esitlikServe, name="esitlik"),
    path('cozumler', views.cozumServe, name="cozumler"),
    path('urunler', views.urunServe, name="urunler"),
    path('cozumler/proje-danisma', views.projeDanismaServe, name="proje-danisma"),
    path('cozumler/meedp', views.meedpServe, name="meedp"),
    path('cozumler/otomasyon', views.otomasyonServe, name="otomasyon"),
    path('cozumler/ekkkyg', views.ekkkygServe, name="ekkkyg"),
    path('cozumler/ekkkt', views.ekkktServe, name="ekkkt"),
    path('cozumler/imkkkt', views.imkkktServe, name="imkkkt"),
    path('cozumler/imkkkyg', views.imkkkygServe, name="imkkkyg"),
    path('cozumler/projeler', views.projeServe, name="proje"),
    path('cozumler/projeler/onboard-charger', views.onboardChargerServe, name="onboard-charger"),
    path('cozumler/projeler/multiport', views.multiportServe, name="multiport"),

    path('cozumler/projeler/arisistemi', views.arisistemiServe, name="arisistemi"),
    path('cozumler/projeler/droneproje', views.droneprojeServe, name="droneproje"),
    
    path('cozumler/projeler/ceryan', views.ceryanServe, name="ceryan"),
    path('urunler/dc-dc', views.dcdcServe, name="dc-dc"),
    path('urunler/motor-surucu', views.msServe, name="motor-surucu"),
    path('urunler/mikro-inverter', views.miServe, name="mikro-inverter"),
    path('urunler/bms', views.bmsServe, name="bms"),
    path('urunler/stk', views.stkServe, name="stk"),
    path('urunler/bty', views.btyServe, name="bty"),
    
    path('urunler/esp-sm3', views.esp_sm3Serve, name='esp-sm3'),
    path('urunler/assr-dim-plc', views.assr_dim_plcServe, name='assr-dim-plc'),
    path('urunler/acc-plc', views.acc_plcServe, name='acc-plc'),
    path('urunler/acs-200', views.acs_200Serve, name='acs-200'),
    # path('urunler/aais', views.aaisServe, name="aais"),
    path('makaleler', views.makaleServe, name="makale"),
    path('news', views.newsServe, name="news"),
    # path('blog-single', views.blogSingleIndex, name="blog-single"),
    # path('portfolio', views.portfolioDetails, name="portfolio"),
    # path('shopping-cart', views.shoppingCart, name="shopping"),
    path('contact-api', ContactAPI.as_view(), name="contact"),
    path('news-api', NewsAPI.as_view(), name="news"),
    # path('tekliff', views.serveExample, name="example"),
    # path('teklifff', views.serveExamplee, name="examplee"),
    # path('teklif-api', TeklifAPI.as_view(), name="teklif-api"),
    # path('api/staj/202307', StajerAPI.as_view(), name="stajer-api"),
    # Matches any html file
    re_path(r'^.*\.*', views.errorServe, name='404'),
    
    
    

]


