import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

# --- AYARLAR ---
URL = 'https://www.imdb.com/chart/top/'
EXCEL_FILE = "IMDB_Top_Movies.xlsx"

# Tarayıcı Taklidi Yapan Başlıklar
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    print("""
    ██╗███╗   ███╗██████╗ ██████╗ 
    ██║████╗ ████║██╔══██╗██╔══██╗
    ██║██╔████╔██║██║  ██║██████╔╝
    ██║██║╚██╔╝██║██║  ██║██╔══██╗
    ██║██║ ╚═╝ ██║██████╔╝██████╔╝
    ╚═╝╚═╝     ╚═╝╚═════╝ ╚═════╝ 
      --- Python Web Scraper ---
    """)

def fetch_data():
    print("⏳ IMDB sunucularına bağlanılıyor...")
    try:
        response = requests.get(URL, headers=HEADERS)
        if response.status_code != 200:
            print(f"❌ Hata: Bağlantı reddedildi! (Kod: {response.status_code})")
            return None
        
        print("✅ Bağlantı başarılı! Veriler işleniyor...")
        return response.content
    except Exception as e:
        print(f"❌ Kritik Hata: {e}")
        return None

def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    movie_list = []
    
    # IMDB Liste Öğelerini Bul
    items = soup.find_all('li', class_='ipc-metadata-list-summary-item')
    
    for item in items:
        try:
            # Başlık
            title_tag = item.find('h3', class_='ipc-title__text')
            title = title_tag.text.split('. ', 1)[1] if title_tag and '. ' in title_tag.text else title_tag.text

            # Yıl ve Süre (Metadata)
            metadata = item.find_all('span', class_='cli-title-metadata-item')
            year = metadata[0].text if metadata else "N/A"
            duration = metadata[1].text if len(metadata) > 1 else "N/A"

            # Puan
            rating_tag = item.find('span', class_='ipc-rating-star--rating')
            rating = float(rating_tag.text) if rating_tag else 0.0

            movie_list.append({
                "Film Adı": title,
                "Yıl": year,
                "Süre": duration,
                "IMDB Puanı": rating
            })
        except Exception:
            continue
            
    return movie_list

def save_to_excel(data):
    if not data:
        print("⚠️ Kaydedilecek veri bulunamadı.")
        return

    df = pd.DataFrame(data)
    
    # Excel'e yaz
    with pd.ExcelWriter(EXCEL_FILE, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='IMDB Top List')
        
    print(f"\n🎉 İŞLEM TAMAMLANDI!")
    print(f"📊 Toplam {len(data)} film çekildi.")
    print(f"💾 Dosya oluşturuldu: {EXCEL_FILE}")
    print("-" * 40)

def main():
    clear_screen()
    print_banner()
    html = fetch_data()
    if html:
        data = parse_html(html)
        save_to_excel(data)

if __name__ == "__main__":
    main()