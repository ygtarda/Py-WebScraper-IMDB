# 🎬 IMDB Top Movies Scraper

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-Scraping-green?style=for-the-badge)

**IMDB Scraper**, dünyanın en popüler film veritabanı olan IMDB üzerinden en yüksek puanlı filmleri otomatik olarak çeken, verileri temizleyen ve analiz edilebilir **Excel (.xlsx)** formatında raporlayan bir Python otomasyon aracıdır.

Bu proje, **Veri Madenciliği (Data Mining)** ve **ETL (Extract, Transform, Load)** süreçlerinin temel bir örneğidir.

---

## 🚀 Özellikler

* **🕷️ Akıllı Web Scraping:** `BeautifulSoup4` kullanarak HTML yapısını parçalar ve anlamlı verileri ayıklar.
* **📊 Veri Yapılandırma:** Ham veriyi `Pandas` DataFrame yapısına dönüştürür ve temizler.
* **💾 Excel Raporlama:** Çekilen verileri, analiz edilmeye hazır formatta Excel dosyasına kaydeder.
* **🛡️ Hata Yönetimi:** Bağlantı kopmaları veya site yapısı değişikliklerine karşı dirençli kod yapısı.
* **🖥️ CLI Arayüzü:** Kullanıcı dostu terminal arayüzü ve ASCII art banner desteği.
---

## 🛠️ Kullanılan Teknolojiler

* **Python 3.11**
* **Requests:** HTTP isteklerini yönetmek için.
* **BeautifulSoup4:** HTML/XML ayrıştırma işlemleri için.
* **Pandas:** Veri analizi ve Excel işlemleri için.
* **OpenPyXL:** Excel dosya yazma motoru.
---

## 💻 Kurulum ve Çalıştırma

Projeyi yerel ortamınızda çalıştırmak için aşağıdaki adımları izleyin:

**1. Repoyu Klonlayın**
```bash
git clone [https://github.com/ygtarda/./Py-WebScraper-IMDB](https://github.com/ygtarda/./Py-WebScraper-IMDB)
cd imdb-scraper
```
**2. Sanal Ortamı Kurun (Önerilen)**
```bash
python3.11 -m venv .venv
source .venv/bin/activate  # Mac/Linux
# .venv\Scripts\activate   # Windows
```
**3. Gerekli Kütüphaneleri Yükleyin**
```bash
pip install requests beautifulsoup4 pandas openpyxl
```
**4. Botu Çalıştırın**
```bash
python Py-WebScraper-IMDB.py
```
---

## 📊 Örnek Çıktı
Program çalıştırıldığında proje klasöründe IMDB_Top_Movies.xlsx adında bir dosya oluşur:
[Görsel](1.png)

## 👤 Geliştirici
Arda Yiğit
* 🐙 GitHub: [ygtarda](https://github.com/ygtarda)
* 💼 LinkedIn: [Arda Yiğit](https://www.linkedin.com/in/arda-yigit)
---
Bu proje eğitim amaçlıdır. Veri çekme işlemleri site politikalarına uygun yapılmalıdır.