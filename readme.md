# Django Website Projesi

## İçindekiler
1. [Proje Açıklaması](#proje-açıklaması)
2. [Gereksinimler](#gereksinimler)
3. [Kurulum Adımları](#kurulum-adımları)
4. [Proje Yapısı](#proje-yapısı)
5. [Projeyi Yerelde Çalıştırma](#projeyi-yerelde-çalıştırma)
6. [Kullanım](#kullanım)
7. [Statik ve Template Dosyaları](#statik-ve-template-dosyaları)
8. [Projenin Canlıya Çıkartılması](#deploy)
---

## Proje Açıklaması
Bu proje, **Django tabanlı bir web sitesi** olup, kullanıcı kimlik doğrulama, veritabanı etkileşimleri ve duyarlı bir ön yüz içerir. Proje, formlar, modeller, statik dosyalar, şablonlar ve temel işlevleri yöneten modüler uygulamalarla organize edilmiştir.

## Gereksinimler
Aşağıdaki araçların sisteminizde yüklü olduğundan emin olun:

- Python 3.8+  
- pip (Python paket yöneticisi)
- Virtualenv (isteğe bağlı fakat önerilir)
- SQLite (Python ile birlikte gelir)

## Kurulum Adımları
Projeyi yerel makinenizde kurmak için aşağıdaki adımları izleyin:

1. **Sanal Ortam Oluşturun**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

2. **Gerekli Paketleri Kurun**:
   Gerekli bağımlılıklar `requirements.txt` dosyasında belirtilmiştir. Aşağıdaki komutu çalıştırın:
   ```bash
   pip install -r requirements.txt
   ```

3. **Ortam Değişkenlerini Ayarlayın**:
   `.django.env` dosyasını kopyalayın ve gerekli ortam değişkenlerini yapılandırın:
   ```bash
   cp django.env .env
   ```

4. **Veritabanı Migrasyonlarını Çalıştırın**:
   SQLite veritabanını ayarlamak için aşağıdaki komutu çalıştırın:
   ```bash
   python manage.py migrate
   ```

5. **Süper Kullanıcı Oluşturun** (isteğe bağlı):
   Admin paneline erişmek için bir yönetici kullanıcı oluşturun:
   ```bash
   python manage.py createsuperuser
   ```

---

## Proje Yapısı
Projenin klasör yapısına genel bir bakış aşağıda verilmiştir:

### 1. **Ana Dosyalar**
```plaintext
- apps                 # Web fonksiyonları, statik dosyalar
- core                 # Server fonksiyonları
- db.sqlite3           # SQLite veritabanı dosyası
- manage.py            # Django yönetim scripti
- django.env           # Ortam yapılandırma dosyası
- requirements.txt     # Gerekli kütüphaneler listesi
```

### 2. **Apps**
#### apps
Bu klasör, modüler Django uygulamalarını içerir:
- **apps/authentication**: Kullanıcı formları, modelleri ve kimlik doğrulama işlemlerini yönetir.
- **apps/home**: Web isteklerini işler, `futures` modülü ile veritabanında arama fonksiyonları 
içerir.
- **apps/static**: Bütün css, js, resim, pdf dosyalarını içerir.
- **apps/templates**: Bütün html dosyalarını içerir.

### 3. **Templates**
#### apps/templates
Bu klasör, projede kullanılan tüm HTML şablonlarını içerir:
```plaintext
- blog.html
- blog-single.html
- home.html
- index.html
- index-webp.html
- inner-page.html
- portfolio-details.html
- shopping-cart.html
```
Şablonlar, ön yüz düzeni ve içerik render işlemlerini yönetir.

### 4. **Statik Dosyalar**
#### apps/static
Bu klasör, CSS, JavaScript, resimler, PDF dosyaları ve dış kütüphaneler gibi tüm statik kaynakları içerir:
```plaintext
- css/      # Stil dosyaları
- img/      # Görsel dosyaları
- js/       # JavaScript dosyaları
- pdf/      # PDF dosyaları
- vendor/   # Harici kütüphaneler
```

### 5. **Çekirdek Yapılandırma**
#### core
Projenin ana yapılandırma dosyalarını içerir (örneğin `settings.py`, `urls.py` vb.).

---

## Projeyi Yerelde Çalıştırma
1. Geliştirme sunucusunu başlatmak için aşağıdaki komutu çalıştırın:
   ```bash
   python manage.py runserver
   ```

2. Tarayıcınızı açın ve aşağıdaki adrese gidin:
   ```
   http://127.0.0.1:8000/
   ```
3. Admin paneline erişmek için şu adrese gidin:
   ```
   http://127.0.0.1:8000/admin
   ```
   Daha önce oluşturduğunuz süper kullanıcı bilgileriyle giriş yapabilirsiniz.

---

## Kullanım
- Kullanıcılar, web sitesinde gezinerek ön yüz sayfalarıyla etkileşim kurabilir.
- Arama, form gönderimi gibi veritabanı işlemleri sorunsuz bir şekilde gerçekleştirilir.
- Admin paneli üzerinden içerik ve kullanıcılar yönetilebilir.

---

## Statik ve Template Dosyaları
- Statik dosyalar (CSS, JS, resimler vb.) `apps/static` klasöründe yer alır.
- HTML şablonları `apps/templates` klasöründe bulunur.

## Deploy

1. Proje localhost üzerinde bütün ayarlamaları tamamlandıktan sonra core dosyası içindeki setting.py içerisinden debug=False hale getirilmeli. 
   ```
   debug=False
   ```

2. DigitalOcean ya da benzeri platformlar için proje uygun hale getirilir. (Projenin yükleneceği platformun dökümantasyonu okunarak gerekli işlemler yapılmalıdır.)

3. Proje dosyaları github'a yüklenmelidir.

4. Projenin barındılacağı platforma github bağlantısı ile projenin canlıya yüklenilir.

5. Platforma yüklendikten sonra core\setting.py içerisinde allowed_host içerisine platformun size verdiği url içerecek şekilde güncellenmelidir.

6. Platform üzerinden domain name için dns adresleri alınır.

7. Cloudflare üzerinden dns yönlendirmeleri yapılır.

8. Domain name kontrolü yapılır. (solvaytech.com.tr)

9. Tarayıcıdan url adresi girilerek websitesine giriş yapılır.