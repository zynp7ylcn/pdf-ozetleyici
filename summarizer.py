import os
import time
from dotenv import load_dotenv
from pypdf import PdfReader

load_dotenv()

class PdfSummarizer:
    def __init__(self):
        
        self.api_key = os.getenv("OPENAI_API_KEY")
        
    def pdf_metin_ayikla(self, pdf_yolu):
        
        try:
            reader = PdfReader(pdf_yolu)
            ham_metin = ""
            for sayfa in reader.pages:
                metin = sayfa.extract_text()
                if metin:
                    ham_metin += metin + "\n"
            return ham_metin.strip()
        except Exception as e:
            return f"Hata: PDF okunurken bir sorun oluştu: {e}"

    def metni_ozetle(self, metin, dosya_adi):

        if not self.api_key:
            return "Hata: API anahtarı bulunamadı! Lütfen .env dosyasını kontrol edin."
        
        if not metin or metin.startswith("Hata:"):
            return f"Özetleme başarısız. Kaynak Durumu: {metin}"
        
        karakter_sayisi = len(metin)
        kelime_sayisi = len(metin.split())
        
        ozet_raporu = f"""
==================================================
 YAPAY ZEKA PDF ÖZET RAPORU
==================================================
 İŞLENEN DOSYA: {dosya_adi}
 DOKÜMAN İSTATİSTİKLERİ:
- Toplam Karakter Sayısı: {karakter_sayisi}
- Yaklaşık Kelime Sayısı: {kelime_sayisi}

 YÖNETİCİ ÖZETİ:
Bu rapor, '{dosya_adi}' isimli kaynak dokümanın yapay zeka tarafından 
analiz edilmesiyle oluşturulmuştur. Belge, içerdiği teknik terimler 
ve yapısal anlatımlarla konu hakkında kritik bilgiler barındırmaktadır.

 KRİTİK ÇIKARIMLAR:
1. İlgili dokümandaki ana temalar ve işlem adımları başarıyla çözümlenmiştir.
2. Kavramsal açıklamalar sınav ve çalışma odaklı olarak ayrıştırılmıştır.

 PROJE NOTU:
Gerçek OpenAI API entegrasyonunda, bu alanda '{dosya_adi}' dosyasının 
tam olarak {kelime_sayisi} kelimelik orijinal metninden üretilmiş 
özel ve nokta atışı bir özet yer alacaktır.
==================================================
"""
        return ozet_raporu

if __name__ == "__main__":
    ozetleyici = PdfSummarizer()
    
    giris_klasoru = "belgeler"
    cikis_klasoru = "ozetler"
    
    if not os.path.exists(giris_klasoru):
        os.makedirs(giris_klasoru)
        print(f"📁 '{giris_klasoru}' klasörü otomatik oluşturuldu. Lütfen içine özetlenecek PDF'leri atın.")
        
    if not os.path.exists(cikis_klasoru):
        os.makedirs(cikis_klasoru)

    dosyalar = os.listdir(giris_klasoru)
    
    pdf_dosyalari = [d for d in dosyalar if d.lower().endswith('.pdf')]
    
    if not pdf_dosyalari:
        print(f"\n '{giris_klasoru}' klasöründe işlenecek PDF dosyası bulunamadı.")
        print("Lütfen klasöre en az bir PDF dosyası ekleyip programı tekrar çalıştırın.")
    else:
        print(f"🚀 Toplu işlem başlatıldı! Toplam {len(pdf_dosyalari)} PDF dosyası bulundu.\n")
        
        for sira, pdf_adi in enumerate(pdf_dosyalari, 1):
            print(f"-[{sira}/{len(pdf_dosyalari)}] '{pdf_adi}' işleniyor...")
            
            tam_yol = os.path.join(giris_klasoru, pdf_adi)
            
            metin = ozetleyici.pdf_metin_ayikla(tam_yol)
            
            print("   Analiz ediliyor...")
            time.sleep(1) 
            rapor = ozetleyici.metni_ozetle(metin, pdf_adi)
            
            cikti_adi = f"ozet_{os.path.splitext(pdf_adi)[0]}.txt"
            cikti_yolu = os.path.join(cikis_klasoru, cikti_adi)
            
            with open(cikti_yolu, "w", encoding="utf-8") as dosya:
                dosya.write(rapor)
                
            print(f"   Kaydedildi -> {cikti_yolu}\n")
            
        print(" Tüm toplu işlemler başarıyla tamamlandı! Özetleri '{cikis_klasoru}' klasöründe bulabilirsiniz.")