## URL Harvester

-Bu Python projesi, girilen bir web adresinden (örneğin bir blog, haber sitesi, vb.) sayfadaki tüm bağlantıları (href) toplayarak listeleyen basit bir web kazıyıcıdır. 
-Ayrıca kullanıcı dostu bir Tkinter GUI arayüzü ile desteklenmiştir.

## 📁 Proje Dosya Yapısı

url-harvester/

│

├── link_extractor.py   # Web sayfasından bağlantıları toplayan scraper kodu

├── gui.py              # Kullanıcı arayüzü (Tkinter GUI)

└── README.md           # Proje tanıtım dosyası

## 🚀 Özellikler

- HTTP/HTTPS destekli bağlantı kazıma

- requests ve BeautifulSoup ile sayfa analizi

- Tkinter ile kolay arayüz

- Listbox ile bağlantıları listeleme

- Kaydırma çubuğu desteği (scrollbar)

## 🔧 Gereksinimler

Bu proje için Python 3.7 veya üzeri önerilir. Kullanılan ek kütüphaneler:

- requests

- beautifulsoup4

Bu kütüphaneleri elle kurmak için terminal veya komut satırında aşağıdaki komutları çalıştırabilirsin:

- pip install requests

- pip install beautifulsoup4


## 📄 Dosya Açıklamaları

| Dosya               | Açıklama                                                         |
| ------------------- | ---------------------------------------------------------------- |
| `link_extractor.py` | Sayfadaki bağlantıları (`<a href>`) çıkarır                      |
| `gui.py`            | Kullanıcının web adresini girip tarama yapabildiği grafik arayüz |
| `README.md`         | Proje açıklaması ve kurulum adımları                             |


## 🧪 Nasıl Kullanılır?

1. Proje klasörüne gir:

- cd url-kaziyici

2. GUI uygulamasını çalıştır:

- python gui.py

3. Açılan pencerede bir web adresi gir (örneğin: https://www.wikipedia.org) ve “Taramaya Başla” butonuna bas.

4. Bağlantılar listelenmiş olarak arayüzde görünecektir.

## Ekran Görüntüsü

<img width="876" height="435" alt="image" src="https://github.com/user-attachments/assets/65be1997-49d8-47aa-9e8c-e41e44723cc2" />

## 👨‍💻 Geliştirici

Umutcan Kemahlı

İsparta Uygulamalı Bilimler Üniversitesi

Bilgisayar Mühendisliği, 4. Sınıf

Back-End Developer Adayı


