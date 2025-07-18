import tkinter as tk
from tkinter import ttk  # Düzeltme: tkinter.ttk değil tkk
from link_extractor import url_kazayici  # Web scraping kodlarının bulunduğu dosya

def tara():
    adres = giris_kutusu.get()
    sonuc_kutusu.delete(0, tk.END)
    url_listesi = url_kazayici(adres)
    for i, link in enumerate(url_listesi, start=1):
        sonuc_kutusu.insert(tk.END, f"{i}. {link}")


pencere = tk.Tk()
pencere.title("URL Kazıyıcı")
pencere.geometry("700x500")


etiket = ttk.Label(pencere, text="Web adresini girin Abi (https://...):")
etiket.pack(pady=10)

giris_kutusu = ttk.Entry(pencere, width=80)
giris_kutusu.pack(pady=5)


tara_butonu = ttk.Button(pencere, text="Taramaya Başla", command=tara)
tara_butonu.pack(pady=10)


frame = ttk.Frame(pencere)
frame.pack(pady=10, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

sonuc_kutusu = tk.Listbox(frame, width=100, height=20, yscrollcommand=scrollbar.set)
sonuc_kutusu.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar.config(command=sonuc_kutusu.yview)


pencere.mainloop()
