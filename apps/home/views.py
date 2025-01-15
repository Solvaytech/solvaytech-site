from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, FileResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from django.utils import timezone
from core.settings import DEBUG, SECRET_KEY, ALLOWED_HOSTS, CSRF_TRUSTED_ORIGINS
from .futures.query import Query
import json
from apps.home.models import Contact
from core.settings import BASE_DIR


def arisistemiServe(request):
    context = {}
    html_template = loader.get_template('flex/pages/cozumler/projeler/tübitak/arisistemi.html')
    return HttpResponse(html_template.render(context, request))

def droneprojeServe(request):
    context = {}
    html_template = loader.get_template('flex/pages/cozumler/projeler/tübitak/droneproje.html')
    return HttpResponse(html_template.render(context, request))

def esp_sm3Serve(request):
    context = {}
    html_template = loader.get_template('flex/pages/urunler/esp-sm3.html')
    return HttpResponse(html_template.render(context, request))

def assr_dim_plcServe(request):
    context = {}
    html_template = loader.get_template('flex/pages/urunler/assr-dim-plc.html')
    return HttpResponse(html_template.render(context, request))

def acc_plcServe(request):
    context = {}
    html_template = loader.get_template('flex/pages/urunler/acc-plc.html')
    return HttpResponse(html_template.render(context, request))

def acs_200Serve(request):
    context = {}
    html_template = loader.get_template('flex/pages/urunler/acs-200.html')
    return HttpResponse(html_template.render(context, request))

def Admin(request):
    return HttpResponseRedirect(reverse('admin:index'))

def serveIndex(request):
    context = {}
    html_template = loader.get_template('flex/home.html')
    return HttpResponse(html_template.render(context,request))

def webpIndex(request):
    context = {}
    html_template = loader.get_template('flex/index-webp.html')
    return HttpResponse(html_template.render(context,request))

def cerezIndex(request):
    context = {}
    html_template = loader.get_template('flex/pages/cookie-policy/cookie-policy.html')
    return HttpResponse(html_template.render(context,request))

def kvkkPDFServe(request):
    try:
        file = open(BASE_DIR + '/staticfiles/assets/flex/pdf/kvkk.pdf', 'rb')
        return FileResponse(file, as_attachment=False, filename= 'kvkk-aydinlatma.pdf')
    except:
        return HttpResponseRedirect('/')
    
def kisielBilgiBasvuruPDFServe(request):
    try:
        file = open(BASE_DIR + '/staticfiles/assets/flex/pdf/basvuru.pdf', 'rb')
        return FileResponse(file, as_attachment=False, filename= 'kisisel-veri-sahibi-basvuru-formu.pdf')
    except:
        return HttpResponseRedirect('/')

def blogIndex(request):
    context = {}
    html_template = loader.get_template('flex/blog.html')
    return HttpResponse(html_template.render(context,request))

def blogSingleIndex(request):
    context = {}
    html_template = loader.get_template('flex/blog-single.html')
    return HttpResponse(html_template.render(context,request))

def portfolioDetails(request):
    context = {}
    html_template = loader.get_template('flex/portfolio-details.html')
    return HttpResponse(html_template.render(context, request))

def shoppingCart(request):
    context = {}
    html_template = loader.get_template('flex/shopping-cart.html')
    return HttpResponse(html_template.render(context, request))

def aboutServe(request):
    context = {}
    html_template = loader.get_template('flex/pages/hakkimizda/about.html')
    return HttpResponse(html_template.render(context, request))

def esitlikServe(request):
    context = {}
    html_template = loader.get_template('flex/pages/hakkimizda/esitlik.html')
    return HttpResponse(html_template.render(context, request))

def cozumServe(request):
    context = {}
    html_template = loader.get_template('flex/pages/cozumler/cozum.html')
    return HttpResponse(html_template.render(context, request))

def projeDanismaServe(request):
    context = {}
    html_template = loader.get_template('flex/pages/cozumler/danisman/proje-danisma.html')
    return HttpResponse(html_template.render(context, request))

def meedpServe(request):
    context = {}
    html_template = loader.get_template('flex/pages/cozumler/danisman/meedp.html')
    return HttpResponse(html_template.render(context, request))

def otomasyonServe(request):
    context = {}
    html_template = loader.get_template('flex/pages/cozumler/otomasyon/otomasyon.html')
    return HttpResponse(html_template.render(context, request))

def ekkkygServe(request):
    context = {}
    html_template = loader.get_template('flex/pages/cozumler/boh/EKKKYG.html')
    return HttpResponse(html_template.render(context, request))

def ekkktServe(request):
    context = {}
    html_template = loader.get_template('flex/pages/cozumler/boh/EKKKT.html')
    return HttpResponse(html_template.render(context, request))

def imkkktServe(request):
    context = {}
    html_template = loader.get_template('flex/pages/cozumler/boh/IMKKKT.html')
    return HttpResponse(html_template.render(context, request))

def imkkkygServe(request):
    context = {}
    html_template = loader.get_template('flex/pages/cozumler/boh/IMKKKYG.html')
    return HttpResponse(html_template.render(context, request))

def urunServe(request):
    context = {}
    html_template = loader.get_template('flex/pages/urunler/urun.html')
    return HttpResponse(html_template.render(context, request))

def dcdcServe(request):
    context = {}
    html_template = loader.get_template('flex/pages/urunler/dc-dc.html')
    return HttpResponse(html_template.render(context, request))

def msServe(request):
    context = {}
    html_template = loader.get_template('flex/pages/urunler/motor-surucu.html')
    return HttpResponse(html_template.render(context, request))

def miServe(request):
    context = {}
    html_template = loader.get_template('flex/pages/urunler/mikro-inverter.html')
    return HttpResponse(html_template.render(context, request))

def bmsServe(request):
    context = {}
    html_template = loader.get_template('flex/pages/urunler/bms.html')
    return HttpResponse(html_template.render(context, request))

def stkServe(request):
    context = {}
    html_template = loader.get_template('flex/pages/urunler/deney-setleri/stk.html')
    return HttpResponse(html_template.render(context, request))

def btyServe(request):
    context = {}
    html_template = loader.get_template('flex/pages/urunler/deney-setleri/bty.html')
    return HttpResponse(html_template.render(context, request))

def aaisServe(request):
    context = {}
    html_template = loader.get_template('flex/pages/urunler/aais.html')
    return HttpResponse(html_template.render(context, request))

def projeServe(request):
    context = {}
    html_template = loader.get_template('flex/pages/cozumler/projeler/proje.html')
    return HttpResponse(html_template.render(context, request))

def onboardChargerServe(request):
    context = {}
    html_template = loader.get_template('flex/pages/cozumler/projeler/tübitak/onboard-charger.html')
    return HttpResponse(html_template.render(context, request))

def multiportServe(request):
    context = {}
    html_template = loader.get_template('flex/pages/cozumler/projeler/tübitak/multiport.html')
    return HttpResponse(html_template.render(context, request))

def ceryanServe(request):
    context = {}
    html_template = loader.get_template('flex/pages/cozumler/projeler/kosgeb/ceryan.html')
    return HttpResponse(html_template.render(context, request))

def makaleServe(request):
    context = {}
    html_template = loader.get_template('flex/pages/makaleler/makale.html')
    return HttpResponse(html_template.render(context, request))

def newsServe(request):
    context = {}
    html_template = loader.get_template('flex/pages/news/news.html')
    return HttpResponse(html_template.render(context, request))

def errorServe(request):
    context = {}
    html_template = loader.get_template('flex/pages/404/404.html')
    return HttpResponse(html_template.render(context, request))

class ContactAPI(View):
    def get(self, request):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            response = {
                'response' : False,
                'reason' : 'Access Denied.'
            }
        return render(request, 'flex/home.html')
    def post(self, request):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            data = json.loads(request.body)
            if data['name'] and data['email'] and data['subject'] and data['message']:
                try:
                    con = Contact(
                            name = data['name'], 
                            email = data['email'], 
                            subject  = data['subject'], 
                            message = data['message'], 
                            date = timezone.now())
                    con.save(using="default")
                    response = {
                        'response' : True
                    }
                    return JsonResponse(response)
                except Exception as e:
                    response = {
                    'response' : False,
                    'reason' : 'Contact server downed. Please Try again later.'
                }
            else:
                response = {
                        'response' : False,
                        'reason' : 'Form eksik ya da hatalı dolduruldu.'
                    }
                return JsonResponse(response)
        else:
            response = {
                'response' : False,
                'reason' : 'Access Denied.'
            }
            return JsonResponse(response)

class NewsAPI(View):
    def get(self, request):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            response = {
                'response' : True,
                'Anadolu Ajansı' : {
                    'img_jpg' : 'static/assets/flex/img/news/jpg/resized/aa.jpg',
                    'link': 'https://www.aa.com.tr/tr/bilim-teknoloji/cukurova-teknokentte-tasarlanan-elektrikli-arac-ceryanda-hedef-seri-uretim/2751699#',
                    'desc': "Adana'da, Çukurova Teknokent bünyesindeki mühendislik firmasınca geliştirilen, tek kapılı ve 100 kilometre menzilli elektrikli araç 'Ceryan'..."
                    },
                'Ulusal' : {
                    'img_jpg' : 'static/assets/flex/img/news/jpg/resized/ulusal.jpg',
                    'link': 'https://www.ulusal.com.tr/bilim-ve-teknoloji/cukurova-teknokentte-elektirikli-arac-uretildi-ceryan-15007587',
                    'desc' : "Adana'da, Çukurova Teknokentte geliştirilen, tek kapılı ve 100 kilometre menzilli elektrikli araç Ceryan için seri üretim hazırlıkları yapılıyor."
                    },
                'Tamindir': {
                    'img_jpg' : 'static/assets/flex/img/news/jpg/resized/tamindir.jpg',
                    'link' : 'https://www.tamindir.com/haber/yerli-elektrikli-arac-ceryan-ozellikleri_77375/',
                    'desc' : "Çukurova Teknokent'te yer alan Solvaytech Mühendislik tarafından geliştirilen yerli elektrikli araç Ceryan, seri üretime geçmeye hazırlanıyor."
                    },
                'Donanım Haber' : {
                    'img_jpg': 'static/assets/flex/img/news/jpg/resized/donanim-haber.jpg',
                    'link' : 'https://www.donanimhaber.com/citroen-ami-ye-yerli-rakip-ceryan-seri-uretime-hazirlaniyor--156483',
                    'desc' : 'Çukurova Teknokent bünyesindeki mühendislik firmasınca geliştirilen, tek kapılı ve 100 kilometre menzilli elektrikli araç "Ceryan"...'
                    },
                'Sondakika.com' : {
                    'img_jpg': 'static/assets/flex/img/news/jpg/resized/son-dakika.jpg',
                    'link' : 'https://www.sondakika.com/haber/haber-cukurova-teknokent-te-tasarlanan-elektrikli-arac-15462913/',
                    'desc' : "Adana'da, Çukurova Teknokent bünyesindeki mühendislik firmasınca geliştirilen, tek kapılı ve 100 kilometre menzilli elektrikli araç 'Ceryan'...",
                    },
                'Trt Haber' : {
                    'img_jpg' : 'static/assets/flex/img/news/jpg/resized/trt-haber.jpg',
                    'link' : 'https://www.trthaber.com/foto-galeri/cukurova-teknokentte-tasarlanan-elektrikli-arac-ceryanda-hedef-seri-uretim/52234/sayfa-1.html',
                    'desc' : "Adana'da, Çukurova Teknokent bünyesindeki mühendislik firmasınca geliştirilen, tek kapılı ve 100 kilometre menzilli elektrikli araç 'Ceryan'...",
                    },
                'Çukurova Teknokent' : {
                    'img_jpg' : 'static/assets/flex/img/news/jpg/resized/teknokent.jpg',
                    'link' : 'https://cukurovateknokent.com/event/cukurova-teknokent-firmamiz-solvaytech-muhendislik-tarafindan-gelistirilen-elektrikli-arac-ceryan-tamamlanan-yol-testlerinin-ardindan-seri-uretime-hazirlaniyor/',
                    'desc' : 'Çukurova Teknokent firmamız Solvaytech Mühendislik tarafından geliştirilen elektrikli araç ‘Ceryan’, tamamlanan yol testlerinin ardından...',
                    },
                'Haber 7' : {
                    'img_jpg' : 'static/assets/flex/img/news/jpg/resized/haber7.jpg',
                    'link' : 'https://otomobil.haber7.com/foto-galeri/77023-elektrikli-otomobil-ceryan-seri-uretime-hazirlaniyor',
                    'desc' : "Adana'da, Çukurova Teknokent bünyesindeki mühendislik firmasınca geliştirilen, tek kapılı ve 100 kilometre menzilli elektrikli araç 'Ceryan'...",
                    },
                'Toros' : {
                    'img_jpg' : 'static/assets/flex/img/news/jpg/resized/toros.jpg',
                    'link' : 'https://adanatorosgazetesi.net/cukurova-teknokentte-tasarlanan-elektrikli-arac-ceryanda-hedef-seri-uretim/',
                    'desc' : "Adana'da, Çukurova Teknokent bünyesindeki mühendislik firmasınca geliştirilen, tek kapılı ve 100 kilometre menzilli elektrikli araç 'Ceryan'...",
                    },
                'Dünya Gazatesi' : {
                    'img_jpg' : 'static/assets/flex/img/news/jpg/resized/dunya.jpg',
                    'link' : 'https://www.dunya.com/sehirler/elektrikli-arac-ceryan-seri-uretime-hazirlaniyor-haberi-675523',
                    'desc' : "Adana'da, Çukurova Teknokent bünyesindeki mühendislik firmasınca geliştirilen, tek kapılı ve 100 kilometre menzilli elektrikli araç 'Ceryan'...",
                    },
                'Volkan Haber' : {
                    'img_jpg' : 'static/assets/flex/img/news/jpg/resized/volkan-haber.jpg',
                    'link' : 'https://www.volkanhaber.net/ceryanda-hedef-seri-uretime-gecmek',
                    'desc' : "Adana’da, Çukurova Teknokent bünyesindeki mühendislik firmasınca geliştirilen, tek kapılı ve 100 kilometre menzilli elektrikli araç 'Ceryan'...",
                    },
                'Yorum' : {
                    'img_jpg' : 'static/assets/flex/img/news/jpg/resized/yorum.jpg',
                    'link' : 'https://www.yorumgazetesi.com/haber/cukurova-teknokentte-tasarlanan-elektrikli-arac-ceryanda-hedef-seri-uretim-41726.html',
                    'desc' : "Adana'da, Çukurova Teknokent bünyesindeki mühendislik firmasınca geliştirilen, tek kapılı ve 100 kilometre menzilli elektrikli araç 'Ceryan'...",
                    },
                'Adalet.tv' : {
                    'img_jpg' : 'static/assets/flex/img/news/jpg/resized/adalet.jpg',
                    'link' : 'https://www.adalet.tv/cukurova-teknokent-te-tasarlanan-elektrikli-arac-ceryan-da-hedef-seri-uretim/10025/',
                    'desc' : "Adana'da modeli anketle belirlenen, fiziki geliştirme süreci de 2 yıl süren araç, saatte 45 kilometre hıza ulaşabiliyor.",
                    },
                'Haber 1' : {
                    'img_jpg' : 'static/assets/flex/img/news/jpg/resized/haber1.jpg',
                    'link' : 'https://www.haber1.com/teknoloji/cukurova-teknokentte-tasarlanan-elektrikli-arac-ceryanda-hedef-seri-uretim/',
                    'desc' : "Adana'da, Çukurova Teknokent bünyesindeki mühendislik firmasınca geliştirilen, tek kapılı ve 100 kilometre menzilli elektrikli araç 'Ceryan'...",
                    },
                'Türkiye Ajansı' : {
                    'img_jpg' : 'static/assets/flex/img/news/jpg/resized/turkiye-ajansi.jpg',
                    'link' : 'https://www.turkiyeajansi.com/bilim-teknoloji/cukurova-teknokentte-tasarlanan-elektrikli-arac-342331h',
                    'desc' : "Adana'da, Çukurova Teknokent bünyesindeki mühendislik firmasınca geliştirilen, tek kapılı ve 100 kilometre menzilli elektrikli araç 'Ceryan'...",
                    },
                'Megabayt' : {
                    'img_jpg' : 'static/assets/flex/img/news/jpg/resized/megabayt.jpg',
                    'link' : 'https://www.megabayt.com/citroen-amiye-yerli-rakip-ceryan',
                    'desc' : "Adana'da, Çukurova Teknokent bünyesinde geliştirilen tek kapılı ve elektrikli mini otomobil 'Ceryan', Citoren Ami'ye rakip olmaya...",
                    },
                'Objektifa' : {
                    'img_jpg' : 'static/assets/flex/img/news/jpg/resized/objektifa.jpg',
                    'link' : 'https://www.objektifa.com/mobil/haber/ceryanda-seri-uretim-hedefleniyor-1643.html',
                    'desc' : "‘Ceryan’da Seri Üretim Hedefleniyor. Çukurova Teknokent'teki firma, yürüyen aksam ve elektronik sistemlerini tamamladıktan sonra...",
                    },
                'Emlak Kulisi' : {
                    'img_jpg' : 'static/assets/flex/img/news/jpg/resized/emlak-kulisi.jpg',
                    'link' : 'https://emlakkulisi.com/yol-testleri-tamamlandi-tek-kapili-elektrikli-arac-ceryan-seri-uretime-hazirlaniyor/738423',
                    'desc' : "Adana'da, Çukurova Teknokent bünyesindeki mühendislik firmasınca geliştirilen, tek kapılı ve 100 kilometre menzilli elektrikli araç 'Ceryan'...",
                    },
                'Emlak 365' : {
                    'img_jpg' : 'static/assets/flex/img/news/jpg/resized/emlak-365.jpg',
                    'link' : 'https://www.emlak365.com/finans/100-kilometrede-9-tl-yakan-elektrikli-yerli-otomobil-ceryan-geliyor-192693',
                    'desc' : "Türkiye’de geliştirilen elektrikli otomobillere bir yenisinin daha eklenmeye hazırlandığı bildirildi. 100 km’de 9 TL yakan elektrikli otomobil...",
                    },
                'Adana Post' : {
                    'img_jpg' : 'static/assets/flex/img/news/jpg/resized/adana-post.jpg',
                    'link' : 'https://www.adanapost.com/cukurova-teknokentte-tasarlanan-elektrikli-arac-ceryanda-hedef-seri-uretim-171642h.htm',
                    'desc' : "Çukurova Teknokent'te tasarlanan elektrikli araç Ceryan'da hedef seri üretim. Adana'da modeli anketle belirlenen, fiziki geliştirme süreci...",
                    },
                'Breakingnews' : {
                    'img_jpg' : 'static/assets/flex/img/news/jpg/resized/breakingnews.jpg',
                    'link' : 'https://www.breakingnews.com.tr/haber/cukurova-teknokentte-tasarlanan-elektrikli-arac-ceryanda-hedef-seri-uretim-93999',
                    'desc' : "Adana'da, Çukurova Teknokent bünyesindeki mühendislik firmasınca geliştirilen, tek kapılı ve 100 kilometre menzilli elektrikli araç 'Ceryan'...",
                    },
                'Dik gazete' : {
                    'img_jpg' : 'static/assets/flex/img/news/jpg/resized/dik-gazete.jpg',
                    'link' : 'https://www.dikgazete.com/mobil/haber/cukurova-teknokentte-tasarlanan-elektrikli-arac-ceryanda-hedef-seri-uretim-806548.html',
                    'desc' : "Adana'da, Çukurova Teknokent bünyesindeki mühendislik firmasınca geliştirilen, tek kapılı ve 100 kilometre menzilli elektrikli araç 'Ceryan'...",
                    },
                'Külliye Haber' : {
                    'img_jpg' : 'static/assets/flex/img/news/jpg/resized/kulliye-haber.jpg',
                    'link' : 'https://www.kulliyehaber.com/cukurova-teknokentte-tasarlanan-elektrikli-arac-ceryanda-hedef-seri-uretim/',
                    'desc' : "Adana'da, Çukurova Teknokent bünyesindeki mühendislik firmasınca geliştirilen, tek kapılı ve 100 kilometre menzilli elektrikli araç 'Ceryan'...",
                    },
                'Shift Delete' : {
                    'img_jpg' : 'static/assets/flex/img/news/jpg/resized/shiftdelete.jpg',
                    'link' : 'https://shiftdelete.net/citroen-ami-rakibi-yerli-elektrikli-otomobil-ceryan',
                    'desc' : "Türkiye'de geliştirilen farklı tasarıma sahip otomobillere bir yenisi daha eklendi. İşte Citroen Ami rakibi yerli elektrikli otomobil Ceryan.",
                    },
                'Arabam Blog' : {
                    'img_jpg' : 'static/assets/flex/img/news/jpg/resized/arabam-blog.jpg',
                    'link' : 'https://www.arabam.com/blog/haberler/citroen-amiye-yerli-rakip-ceryan-seri-uretime-hazirlaniyor/',
                    'desc' : "Citroen Ami’ye yerli rakip Ceryan seri üretime hazırlanıyor. Çukurova Teknokent bünyesindeki mühendislik firması yeni bir yerli otomobil...",
                    },
                'Yeni Şafak' : {
                    'img_jpg' : 'static/assets/flex/img/news/jpg/resized/yeni-safak.jpg',
                    'link' : 'https://www.yenisafak.com/foto-galeri/teknoloji/elektrikli-otomobil-ceryan-seri-uretime-hazirlaniyor-2073236?page=1',
                    'desc' : "Adana'da, Çukurova Teknokent bünyesindeki mühendislik firmasınca geliştirilen, tek kapılı ve 100 kilometre menzilli elektrikli araç 'Ceryan'...",
                    },
                'Bursa.com' : {
                    'img_jpg' : 'static/assets/flex/img/news/jpg/resized/bursa.jpg',
                    'link' : 'https://www.bursa.com/mobil/haber/cukurova-teknokentte-tasarlanan-elektrikli-arac-ceryanda-hedef-seri-uretim-536941.html',
                    'desc' : "Adana'da, Çukurova Teknokent bünyesindeki mühendislik firmasınca geliştirilen, tek kapılı ve 100 kilometre menzilli elektrikli araç 'Ceryan'...",
                    },
                'Samimi Haber' : {
                    'img_jpg' : 'static/assets/flex/img/news/jpg/resized/samimi-haber.jpg',
                    'link' : 'https://samimihaber.com/cukurova-teknokentte-tasarlanan-elektrikli-arac-ceryanda-hedef-seri-uretim/',
                    'desc' : "Adana'da, Çukurova Teknokent bünyesindeki mühendislik firmasınca geliştirilen, tek kapılı ve 100 kilometre menzilli elektrikli araç 'Ceryan'...",
                    },
                'Türkiye Gazetesi' : {
                    'img_jpg' : 'static/assets/flex/img/news/jpg/resized/turkiye.jpg',
                    'link' : 'https://www.turkiyegazetesi.com.tr/t-otomobil/citroen-amiye-yerli-rakip-ceryan-kmde-9-kurus-yakiyor-931457',
                    'desc' : "Fransız otomobil devi Citroen'in küçük sınıf otomobil modeli Ami'ye Türkiye'den yerli bir rakip çıktı. Adana'da modeli anketle belirlenen...",
                    },
                'Adanaliyik.net' : {
                    'img_jpg' : 'static/assets/flex/img/news/jpg/resized/adanaliyik.jpg',
                    'link' : 'https://adanaliyik.net/teknoloji/ceryan-seri-uretime-hazirlaniyor/',
                    'desc' : "Çukurova Teknokentte üretilen CERYAN, Citroen Ami’ye rakip olacak. Ceryan, tamamlanan yol testlerinin ardından seri üretime hazırlanıyor.",
                    },
                'Otomobilir' : {
                    'img_jpg' : 'static/assets/flex/img/news/jpg/resized/otomobil.jpg',
                    'link' : 'https://www.otomobilir.com/otomobil-haberleri/ceryan-seri-uretime-hazirlaniyor/',
                    'desc' : "Adana'da, Çukurova Teknokent bünyesindeki mühendislik firmasınca geliştirilen, tek kapılı ve 100 kilometre menzilli elektrikli araç 'Ceryan'...",
                    },
                'Expat Guide Turkey' : {
                    'img_jpg' : 'static/assets/flex/img/news/jpg/resized/expat.jpg',
                    'link' : 'https://expatguideturkey.com/turkish-rival-to-citroen-ami-ceryan/',
                    'desc' : "Turkish Rival to Citroen Ami; “Ceryan”. Developed by the engineering firm of Çukurova Teknokent, the single-door and 100-kilometer...",
                    },
                }
            return JsonResponse(response)
        return render(request, 'flex/home.html')
    def post(self, request):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            response = {
                'response' : False,
                'reason' : 'Access Denied.'
                }
            return JsonResponse(response)
        return render(request, 'flex/home.html')

def serveExample(request):
    context = {}
    html_template = loader.get_template('flex/pages/teklif/example.html')
    return HttpResponse(html_template.render(context, request))

def serveExamplee(request):
    context = {}
    html_template = loader.get_template('flex/pages/teklif/example-2.html')
    return HttpResponse(html_template.render(context, request))

class TeklifAPI(View):
    def get(self, request):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            response = {
                'response' : False,
                'reason' : 'Access Denied'
            }
            return JsonResponse(response)
        return render(request, 'flex/pages/teklif/example.html')
    def post(self, request):
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            data = json.loads(request.body)
            self.checkData(data)
            response = {
                'response' : True,
                'msg' : 'Mesajınız bize ulaşmıştır. En kısa süre içerisinde geri dönüş sağlayacağız.'
            }
        else:
            response = {
                'response' : False,
                'reason' : 'Access Denied'
            }
        return JsonResponse(response)

    def checkData(self, data):
        z = ((lists, keys) for lists in data for keys in data[lists])
        datas = list(z)
        print(datas)
        for x in datas:
            print(data[x[0]][x[1]])

def serveAdminIndex(request):
    context = {}
    html_template = loader.get_template('flex/pages/admin.html')
    return HttpResponse(html_template.render(context, request))

# @method_decorator(csrf_exempt, name='dispatch')
# class StajerAPI(View):
#     def get(self, request):
#         try:
#             if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
#                 if request.headers.get('Staj-Id'):
#                     h = request.headers.get('Staj-Id')
#                     response = {
#                         'response' : True,
#                         'payload' : {
#                             'message' : h
#                         }
#                     }
#                 else:
#                     response = {
#                         'response' : False,
#                         'payload' : {
#                             'message' : 'Access Denied.'
#                         }
#                     }
#             else:
#                 response = {
#                     'response' : False,
#                     'payload' : {
#                         'message' : 'Wrong Request..!'
#                     }
#                 }
#         except:
#             response = {
#                 'response' : False,
#                 'payload' : {
#                     'message' : 'Parse Error: \n' + str(request.headers)
#                 }
#             }
#         return JsonResponse(response)

#     def post (self, request):
#         header = request.headers
#         try:
#             if header.get('X-Requested-With') == 'XMLHttpRequest':
#                 data = json.loads(request.body)
#             if not header.get("Staj-Id"):
#                 response = {
#                     'response' : False,
#                     'payload' : {
#                     'message' : 'Wrong Request..!'
#                     }
#                 }
#                 return JsonResponse(response)
#         except Exception as e:
#                 response = {
#                     'response' : False,
#                     'payload' : {
#                         'error' : 'ParseError: ' + str(header)
#                     }
#                 }
#         else:
#             if request.headers.get('Command-Token') == "register-user":
#                 try:
#                     check = Query.createUser(data["id"], data["pw"], data["email"])
#                     # check = Query.createUser("bcd", "asd","asd@asd.com")
#                     if isinstance(check, Exception):
#                         response = {
#                             'response' : False,
#                             'payload' : {
#                                 'message' : str(check)
#                             }
#                         }
#                     else:
#                         response = {
#                             'response' : True,
#                             'payload' : {
#                                 'message' : "User creation succesfully!"
#                             }
#                         }
#                 except Exception as e:
#                     response = {
#                         'response' : False,
#                         'payload' : {
#                             'error' : "LoginError: Eksik ya da hatalı giriş yaptınız. -> " + str(e)
#                         }
#                     }
#             elif header.get("Command-Token") == "login-user":
#                 try:
#                     if Query.getUserInformationPW(data["id"], data["pw"]):
#                         response = {
#                             'response' : True,
#                             'payload' : {
#                                 'message' : 'Hoşgeldiniz, ' + data["id"]
#                             }
#                         }
#                     else:
#                         response = {
#                                     'response' : False,
#                                     'payload' : {
#                                         'message' : "Login failed!"
#                                     }
#                                 }
#                 except Exception as e:
#                     response = {
#                         'response' : False,
#                         'payload' : {
#                             'error' : "LoginError: Eksik yada hatalı giriş yaptınız. ->" + str(e)
#                         }
#                     }
#             else:
#                 response = {
#                     'response' : True,
#                     'payload' : {
#                         'message' : 'Your message: ' + data['mesaj']
#                     }
#                 }
#         return JsonResponse(response)
