import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from link_extractor import (url_kazayici, ayni_domain_url_ayikla, 
                           url_filtrele, url_listesini_dosyaya_yaz, 
                           dosyadan_url_oku)

class Uygulama:
    def __init__(self, pencere):
        self.pencere = pencere
        self.pencere.title("Gelişmiş URL Kazıyıcı")
        self.pencere.geometry("800x600")
        
        self.url_listesi = []
        self.domain = ""
        
        self.arayuz_olustur()
    
    def arayuz_olustur(self):
        # Giriş Alanı
        giris_frame = ttk.Frame(self.pencere)
        giris_frame.pack(pady=10, fill=tk.X)
        
        ttk.Label(giris_frame, text="Web Adresi:").pack(side=tk.LEFT, padx=5)
        
        self.giris_kutusu = ttk.Entry(giris_frame, width=60)
        self.giris_kutusu.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)
        
        ttk.Button(giris_frame, text="Tara", command=self.tara).pack(side=tk.LEFT, padx=5)
        
        # Filtreleme Alanı
        filtre_frame = ttk.LabelFrame(self.pencere, text="Filtreleme Seçenekleri")
        filtre_frame.pack(pady=10, fill=tk.X, padx=10)
        
        # Aynı Domain
        self.ayni_domain_var = tk.BooleanVar()
        ttk.Checkbutton(filtre_frame, text="Sadece aynı domaindeki URL'ler", 
                       variable=self.ayni_domain_var).pack(anchor=tk.W)
        
        # Uzantı Filtresi
        uzanti_frame = ttk.Frame(filtre_frame)
        uzanti_frame.pack(fill=tk.X, pady=5)
        
        ttk.Label(uzanti_frame, text="Uzantılar (virgülle ayır):").pack(side=tk.LEFT, padx=5)
        
        self.uzanti_giris = ttk.Entry(uzanti_frame, width=30)
        self.uzanti_giris.pack(side=tk.LEFT, padx=5)
        self.uzanti_giris.insert(0, ".html,.php,.pdf")
        
        ttk.Button(uzanti_frame, text="Filtrele", command=self.filtrele).pack(side=tk.LEFT, padx=5)
        
        # Sonuç Listesi
        sonuc_frame = ttk.Frame(self.pencere)
        sonuc_frame.pack(pady=10, fill=tk.BOTH, expand=True, padx=10)
        
        self.scrollbar = ttk.Scrollbar(sonuc_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.sonuc_kutusu = tk.Listbox(sonuc_frame, width=100, height=20, 
                                      yscrollcommand=self.scrollbar.set)
        self.sonuc_kutusu.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.scrollbar.config(command=self.sonuc_kutusu.yview)
        
        # Dosya İşlemleri
        dosya_frame = ttk.Frame(self.pencere)
        dosya_frame.pack(pady=10, fill=tk.X, padx=10)
        
        ttk.Button(dosya_frame, text="Dosyaya Kaydet", 
                  command=self.dosyaya_kaydet).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(dosya_frame, text="Dosyadan Oku", 
                  command=self.dosyadan_oku).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(dosya_frame, text="Temizle", 
                  command=self.temizle).pack(side=tk.RIGHT, padx=5)
    
    def tara(self):
        adres = self.giris_kutusu.get().strip()
        if not adres:
            messagebox.showwarning("Uyarı", "Lütfen bir web adresi girin!")
            return
        
        if not adres.startswith(('http://', 'https://')):
            adres = 'http://' + adres
        
        try:
            self.domain = adres
            self.url_listesi = url_kazayici(adres)
            self.sonuc_goster(self.url_listesi)
        except Exception as e:
            messagebox.showerror("Hata", f"Tarama sırasında hata oluştu: {e}")
    
    def filtrele(self):
        if not self.url_listesi:
            messagebox.showwarning("Uyarı", "Önce tarama yapmalısınız!")
            return
        
        filtrelenmis_liste = self.url_listesi.copy()
        
        # Aynı domain filtresi
        if self.ayni_domain_var.get():
            filtrelenmis_liste = ayni_domain_url_ayikla(filtrelenmis_liste, self.domain)
        
        # Uzantı filtresi
        uzantilar = self.uzanti_giris.get().strip()
        if uzantilar:
            uzanti_listesi = [ext.strip() for ext in uzantilar.split(',') if ext.strip()]
            filtrelenmis_liste = url_filtrele(filtrelenmis_liste, uzanti_listesi)
        
        self.sonuc_goster(filtrelenmis_liste)
    
    def sonuc_goster(self, liste):
        self.sonuc_kutusu.delete(0, tk.END)
        for i, link in enumerate(liste, start=1):
            self.sonuc_kutusu.insert(tk.END, f"{i}. {link}")
    
    def dosyaya_kaydet(self):
        if not self.url_listesi:
            messagebox.showwarning("Uyarı", "Kaydedilecek URL bulunamadı!")
            return
        
        dosya_adi = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Dosyaları", "*.txt"), ("Tüm Dosyalar", "*.*")],
            title="URL Listesini Kaydet"
        )
        
        if dosya_adi:
            if url_listesini_dosyaya_yaz(self.url_listesi, dosya_adi):
                messagebox.showinfo("Başarılı", f"URL listesi başarıyla kaydedildi:\n{dosya_adi}")
            else:
                messagebox.showerror("Hata", "Dosya kaydedilirken bir hata oluştu!")
    
    def dosyadan_oku(self):
        dosya_adi = filedialog.askopenfilename(
            filetypes=[("Text Dosyaları", "*.txt"), ("Tüm Dosyalar", "*.*")],
            title="URL Listesi Dosyasını Seç"
        )
        
        if dosya_adi:
            self.url_listesi = dosyadan_url_oku(dosya_adi)
            if self.url_listesi:
                self.sonuc_goster(self.url_listesi)
                messagebox.showinfo("Başarılı", f"{len(self.url_listesi)} URL başarıyla yüklendi!")
            else:
                messagebox.showwarning("Uyarı", "Dosyadan URL okunamadı veya dosya boş!")
    
    def temizle(self):
        self.sonuc_kutusu.delete(0, tk.END)
        self.url_listesi = []
        self.giris_kutusu.delete(0, tk.END)

if __name__ == "__main__":
    pencere = tk.Tk()
    uygulama = Uygulama(pencere)
    pencere.mainloop()