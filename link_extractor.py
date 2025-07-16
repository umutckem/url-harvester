import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def sayfayi_getir(adres):
    try:
        response = requests.get(adres, timeout = 10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as Hata: 
        print ( f" Sayfa Alınamadı Abi: {Hata} " )
        return None
    
def urlleri_ayikla(html,ana_adres):
    ayirici = BeautifulSoup(html,"html.parser")
    bulunan_url = set()

    for etiket in ayirici.find_all("a",href=True):
        href = etiket.get("href")
        tam_url = urljoin(ana_adres,href)

        if urlparse(tam_url).scheme in ["http","https"]:
            bulunan_url.add(tam_url)

    return list(bulunan_url)

def url_kazayici(hedef_adres):
    print (f"Bağlantılar Taranıyor Abi: {hedef_adres}")

    html = sayfayi_getir(hedef_adres)
    if html is None:
        return[]
    return urlleri_ayikla(html,hedef_adres)

if __name__ == "__main__":
    hedef = input("Lütfen bir web adresi gir abi (https://...) :")

    url_listesi = url_kazayici(hedef)

    print("\n Bulunan Bağlantılar:")
    for sira, link , in enumerate(url_listesi , start=1):
        print(f"{sira}. {link}")



