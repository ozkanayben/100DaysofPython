import requests
from bs4 import BeautifulSoup
import time

def kontrol_et():
    url = "http://www.koeri.boun.edu.tr/scripts/lst5.asp"
    response = requests.get(url)
    response.encoding = "iso-8859-9"  # Türkçe karakter desteği

    soup = BeautifulSoup(response.text, "html.parser")
    pre = soup.find("pre")
    if not pre:
        print("Veri alınamadı.")
        return

    lines = pre.text.strip().split("\n")[6:]  # Başlık dışı satırlar

    son10 = lines[:10]  # Son 10 deprem
    for line in son10:
        parts = line.split()
        if len(parts) < 7:
            continue
        try:
            ml = float(parts[6].replace(",", "."))  # ML değeri
            if ml >= 3.0:
                print("🚨 UYARI: Son 10 depremden biri 4.0 üzeri!")
                print("Detay:", line)
                return
        except ValueError:
            continue

    print("Son 10 depremde 4.0 üzeri yok.")

# 🔁 5 dakikada bir kontrol eder
while True:
    kontrol_et()
    time.sleep(300)  # 5 dakika
