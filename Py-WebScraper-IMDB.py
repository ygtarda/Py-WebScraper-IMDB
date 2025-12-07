import requests
from bs4 import BeautifulSoup
import pandas as pd

# Hedef URL (IMDB Top 250)
url = 'https://www.imdb.com/chart/top/'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5"
}

def main():
    print("🎬 IMDB verileri çekiliyor... Lütfen bekleyin.")
    
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            print("Hata: Siteye erişilemedi!")
            return

        soup = BeautifulSoup(response.content, 'html.parser')
        
        movie_titles = []
        movie_years = []
        movie_ratings = []
        
        # Filmleri bul
        movies = soup.find_all('li', class_='ipc-metadata-list-summary-item')
        print(f"Toplam {len(movies)} film bulundu. İşleniyor...")

        for movie in movies:
            try:
                # 1. Başlık Çekme (Hata Korumalı)
                title_tag = movie.find('h3', class_='ipc-title__text')
                if title_tag:
                    raw_title = title_tag.text
                    # Eğer "1. Film" formatındaysa böl, değilse olduğu gibi al
                    if '. ' in raw_title:
                        title = raw_title.split('. ', 1)[1]
                    else:
                        title = raw_title
                else:
                    title = "Bilinmiyor"
                
                # 2. Yıl Bilgisi
                metadata = movie.find_all('span', class_='cli-title-metadata-item')
                if len(metadata) > 0:
                    year = metadata[0].text
                else:
                    year = "0000"
                
                # 3. Puan Çekme
                rating_tag = movie.find('span', class_='ipc-rating-star--rating')
                # Puan bazen boş gelebilir, kontrol edelim
                if rating_tag:
                    rating = rating_tag.text.strip()
                else:
                    rating = "0.0"

                # Listelere ekle
                movie_titles.append(title)
                movie_years.append(year)
                movie_ratings.append(rating)

            except Exception as e:
                # Tek bir filmde hata olursa program çökmesin, o filmi atlasın
                print(f"Bir satır atlandı: {e}")
                continue

        # --- EXCEL'E AKTARMA ---
        if len(movie_titles) > 0:
            df = pd.DataFrame({
                'Film Adı': movie_titles,
                'Yıl': movie_years,
                'Puan': movie_ratings
            })

            # Puanı sayıya çevirmeyi dene (Hata verirse boşver)
            try:
                df['Puan'] = df['Puan'].astype(float)
            except:
                pass
            
            print("\n------------------------------------------------")
            print("📊 İSTATİSTİKLER")
            print(f"Listelenen Film Sayısı: {len(df)}")
            print("------------------------------------------------")

            file_name = "IMDB_Listesi.xlsx"
            df.to_excel(file_name, index=False)
            print(f"✅ Başarılı! Veriler '{file_name}' dosyasına kaydedildi.")
        else:
            print("❌ Hiç veri çekilemedi. Site yapısı değişmiş olabilir.")

    except Exception as e:
        print(f"Genel bir hata oluştu: {e}")

if __name__ == "__main__":
    main()