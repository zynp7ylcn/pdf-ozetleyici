# Yapay Zeka Destekli PDF Özetleyici (AI PDF Summarizer)

Bu proje, Python kullanılarak geliştirilmiş, Nesne Yönelimli Programlama (OOP) mimarisine sahip ve toplu veri işleme yeteneği olan bir **PDF Özetleme Platformu** simülasyonudur. Proje, kurumsal yazılım standartlarına uygun olarak `.env` çevre değişkenleri güvenliği ve Git versiyon kontrol sistemiyle geliştirilmiştir.

## Özellikler

- **OOP (Nesne Yönelimli) Mimari:** Modüler, genişletilebilir ve temiz kod yapısı.
- **Toplu İşlem (Batch Processing):** Belirtilen giriş klasöründeki tüm PDF dosyalarını otomatik olarak tarar ve sırayla işler.
- **Gelişmiş PDF Metin Ayıklama:** `pypdf` kütüphanesi yardımıyla dökümanların içerisindeki tüm metin verisini kayıpsız şekilde okur.
- **Otomatik Raporlama (I/O):** Yapay zeka tarafından üretilen özet raporlarını otomatik olarak dışa aktarır ve `.txt` formatında kaydeder.
- **Siber Güvenlik Standartları:** Hassas API anahtarlarını korumak amacıyla `.env` (Dotenv) yapılandırması kullanılmıştır.

## Kullanılan Teknolojiler

- **Dil:** Python 3.14+
- **Kütüphaneler:** `pypdf`, `python-dotenv`
- **IDE / Ortam:** VS Code
- **Versiyon Kontrol:** Git & GitHub

## Proje Yapısı

```text
pdf-summarizer/
│
├── belgeler/          # Özetlenecek PDF dosyalarının yüklendiği giriş klasörü
├── ozetler/           # Yapay zekanın ürettiği .txt raporlarının kaydedildiği çıkış klasörü
├── summarizer.py      # Projenin ana OOP kod yapısı
├── .env               # Gizli API anahtarlarını barındıran çevre dosyası (GitHub'a yüklenmez)
├── .gitignore         # Güvenlik nedeniyle git takibinden çıkarılan dosyalar listesi
└── README.md          # Proje tanıtım ve kullanım kılavuzu