# 🎥 YouTube Video Downloader

Bu basit ve güçlü Python betiği, `yt-dlp` kütüphanesini kullanarak YouTube videolarını en yüksek kalitede yerel bilgisayarınıza indirmenizi sağlar.

---

## ✨ Özellikler

* **Kolay Kullanım:** Sadece video URL'sini yapıştırın ve indirmeyi başlatın.
* **Otomatik İsimlendirme:** Videoları orijinal YouTube başlıklarıyla kaydeder.
* **Yüksek Performans:** `yt-dlp` altyapısı sayesinde hızlı ve güvenilir indirme sağlar.
* **Hata Yönetimi:** Geçersiz link veya bağlantı sorunlarında kullanıcıyı bilgilendirir.

---

## 🛠️ Kurulum

Betiği çalıştırmadan önce sisteminizde Python'un yüklü olduğundan emin olun. Ardından gerekli kütüphaneyi yüklemek için terminale şu komutu yazın:

```bash
pip install yt-dlp
🚀 Kullanım
Betiği Çalıştırın:

Bash
python YoutubeVDownloader.py
URL Girin: Terminalde beliren YouTube URL: kısmına indirmek istediğiniz videonun bağlantısını yapıştırın.

Keyfini Çıkarın: Video, betiğin bulunduğu klasöre otomatik olarak indirilecektir.

📂 Kod Yapısı
Proje temel olarak şu mantıkla çalışır:

Python
import yt_dlp

# Kullanıcıdan URL alma
url = input("YouTube URL: ").strip()

# İndirme seçenekleri (Dosya adı formatı)
ydl_opts = {
    "outtmpl": "%(title)s.%(ext)s",
}

# İndirme işlemi
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
⚠️ Sorumluluk Reddi
Bu araç yalnızca eğitim amaçlı ve kişisel kullanım için tasarlanmıştır. Telif hakkıyla korunan içeriklerin izinsiz indirilmesi YouTube hizmet şartlarını ihlal edebilir. Kullanım sorumluluğu tamamen kullanıcıya aittir.

🤝 Katkıda Bulunma
Her türlü iyileştirme fikrine açığım! Bir issue açabilir veya doğrudan pull request gönderebilirsiniz.

📄 Lisans
Bu proje MIT lisansı altındadır.
