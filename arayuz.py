import tkinter as tk
from tkinter import ttk, messagebox
from link_extractor import url_kazayici

class Uygulama:
    def __init__(self, pencere):
        self.pencere = pencere
        self.pencere.title("Gelişmiş URL Kazıyıcı")
        self.pencere.geometry("800x600")
        
        self.url_listesi = []
        self.domain = ""
        
        self.arayuz_olustur()
    
    def arayuz_olustur(self):
        giris_frame = ttk.Frame(self.pencere)
        giris_frame.pack(pady=10, fill=tk.X)
        
        ttk.Label(giris_frame, text="Web Adresi:").pack(side=tk.LEFT, padx=5)
        
        self.giris_kutusu = ttk.Entry(giris_frame, width=60)
        self.giris_kutusu.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)
        
        ttk.Button(giris_frame, text="Tara", command=self.tara).pack(side=tk.LEFT, padx=5)
        
        sonuc_frame = ttk.Frame(self.pencere)
        sonuc_frame.pack(pady=10, fill=tk.BOTH, expand=True, padx=10)
        
        self.scrollbar = ttk.Scrollbar(sonuc_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.sonuc_kutusu = tk.Listbox(sonuc_frame, width=100, height=20, 
                                      yscrollcommand=self.scrollbar.set)
        self.sonuc_kutusu.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.scrollbar.config(command=self.sonuc_kutusu.yview)
    
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
    
    def sonuc_goster(self, liste):
        self.sonuc_kutusu.delete(0, tk.END)
        for i, link in enumerate(liste, start=1):
            self.sonuc_kutusu.insert(tk.END, f"{i}. {link}")

if __name__ == "__main__":
    pencere = tk.Tk()
    uygulama = Uygulama(pencere)
    pencere.mainloop()