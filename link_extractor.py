import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import os

def sayfayi_getir(adres):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(adres, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as Hata: 
        print(f"Sayfa Alınamadı Abi: {Hata}")
        return None
    
def urlleri_ayikla(html, ana_adres):
    ayirici = BeautifulSoup(html, "html.parser")
    bulunan_url = set()

    for etiket in ayirici.find_all("a", href=True):
        href = etiket.get("href")
        if href.startswith('#'):
            continue  # Sayfa içi bağlantıları atla
        tam_url = urljoin(ana_adres, href)
        
        if urlparse(tam_url).scheme in ["http", "https"]:
            bulunan_url.add(tam_url)

    return list(bulunan_url)

def url_kazayici(hedef_adres):
    print(f"Bağlantılar Taranıyor Abi: {hedef_adres}")
    html = sayfayi_getir(hedef_adres)
    if html is None:
        return []
    return urlleri_ayikla(html, hedef_adres)

def ayni_domain_url_ayikla(url_listesi, domain):
    """Aynı domaindeki URL'leri filtreler"""
    parsed_domain = urlparse(domain)
    base_domain = parsed_domain.netloc
    
    return [url for url in url_listesi if urlparse(url).netloc == base_domain]

def url_filtrele(url_listesi, uzanti_listesi):
    """İstenen uzantılara göre URL'leri filtreler"""
    return [url for url in url_listesi 
            if any(url.lower().endswith(ext.lower()) for ext in uzanti_listesi)]

def url_listesini_dosyaya_yaz(url_listesi, dosya_adi):
    """URL listesini dosyaya yazar"""
    try:
        with open(dosya_adi, 'w', encoding='utf-8') as dosya:
            for url in url_listesi:
                dosya.write(url + '\n')
        return True
    except Exception as hata:
        print(f"Dosyaya yazma hatası: {hata}")
        return False

def dosyadan_url_oku(dosya_adi):
    """Dosyadan URL listesini okur"""
    try:
        if not os.path.exists(dosya_adi):
            return []
        
        with open(dosya_adi, 'r', encoding='utf-8') as dosya:
            return [satir.strip() for satir in dosya.readlines() if satir.strip()]
    except Exception as hata:
        print(f"Dosya okuma hatası: {hata}")
        return []