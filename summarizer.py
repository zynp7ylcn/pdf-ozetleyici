import os
import time
from dotenv import load_dotenv
from pypdf import PdfReader

load_dotenv()

class PdfSummarizer:
    def __init__(self):
        """
        Gerekli çevre değişkenlerini ve API anahtarını yükler.
        """
        self.api_key = os.getenv("OPENAI_API_KEY")
        
    def pdf_metin_ayikla(self, pdf_yolu):
        """
        Verilen yoldaki PDF dosyasını açar, tüm sayfaları tarar
        ve içindeki ham metni tek bir metin bloğu olarak birleştirir.
        """
        try:
            reader = PdfReader(pdf_yolu)
            ham_metin = ""
            
            for sayfa in reader.pages:
                metin = sayfa.extract_text()
                if metin: 
                    ham_metin += metin + "\n"
            
            return ham_metin.strip()
            
        except FileNotFoundError:
            return "Hata: Belirtilen PDF dosyası bulunamadı. Lütfen dosya adını kontrol edin."
        except Exception as e:
            return f"Hata: PDF okunurken teknik bir sorun oluştu: {e}"

    def metni_ozetle(self, metin):
        """
        Ayıklanan metni analiz eder ve yapay zeka simülasyonu ile
        düzenli bir özet raporu oluşturur.
        """
        if not self.api_key:
            return "Hata: API anahtarı bulunamadı! Lütfen .env dosyasını kontrol edin."
        
        if not metin or metin.startswith("Hata:"):
            return f"Özetleme başarısız. Kaynak Durumu: {metin}"
        
        print("\n Yapay Zeka dokümanı analiz ediyor, lütfen bekleyin...")
        time.sleep(2) 
        
        karakter_sayisi = len(metin)
        kelime_sayisi = len(metin.split())
        
        ozet_raporu = f"""
==================================================
 YAPAY ZEKA PDF ÖZET RAPORU
==================================================
 DOKÜMAN İSTATİSTİKLERİ:
- Toplam Karakter Sayısı: {karakter_sayisi}
- Yaklaşık Kelime Sayısı: {kelime_sayisi}

 YÖNETİCİ ÖZETİ:
Bu doküman, içeriğindeki yapısal veriler ve teknik anlatımlarla 
önemli bir kaynak niteliğindedir. Yapay zeka analizine göre belgenin 
ana odağı, kullanıcının yüklediği akademik veya teknik içeriğin 
temel prensiplerini açıklamaktır.

 KRİTİK ÇIKARIMLAR:
1. Dokümanda geçen temel kavramların tanımları ve birbirleriyle olan ilişkileri vurgulanmıştır.
2. Süreç adımları veya mimari yapılar ardışık olarak ele alınmıştır.

 PROJE NOTU:
Gerçek OpenAI API bağlantısı kurulduğunda, bu alanda yüklediğiniz PDF'in 
tam olarak {kelime_sayisi} kelimelik içeriğinden üretilmiş %100 gerçek, 
doğru ve madde madde detaylandırılmış bir ders/çalışma özeti yer alacaktır.
==================================================
        """
        return ozet_raporu

if __name__ == "__main__":
    ozetleyici = PdfSummarizer()
    
    pdf_dosya_adi = "notlar.pdf" 
    
    print(f" '{pdf_dosya_adi}' dosyası işleniyor...")
    
    ayiklanan_metin = ozetleyici.pdf_metin_ayikla(pdf_dosya_adi)
    
    rapor = ozetleyici.metni_ozetle(ayiklanan_metin)
    
    print(rapor)
    
    if rapor and not rapor.startswith("Hata:"):
        cikti_dosyasi = "ozet_raporu.txt"
        
        with open(cikti_dosyasi, "w", encoding="utf-8") as dosya:
            dosya.write(rapor)
            
        print(f"\n Başarılı! Yapay zeka raporu '{cikti_dosyasi}' olarak otomatik kaydedildi.")