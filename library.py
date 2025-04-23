class Library:
    def __init__(self):
        self.kitaplar=[]

    def kitap_ekle(self):
        adet=int(input("Kaç Adet Kitap Eklemek İstiyorsunuz : "))
        for i in range(adet):
            bookName=input("Kitap Adı Giriniz : ")
            author=input("Yazarı Giriniz : ")
            self.kitaplar.append({"Kitap Adı": bookName, "Yazar": author})
            print(f"'{bookName}' adlı kitap kütüphaneye eklendi.")

    def kitap_çıkar(self):
        if not self.kitaplar:
            print("Kütüphanede çıkarılacak kitap yok.")
            return

        kitap_adi=input("Çıkarmak istediğiniz kitabın adını giriniz : ")
        kitap_bulundu=False

        for kitap in self.kitaplar:
            if kitap["Kitap Adı"]==kitap_adi:
                self.kitaplar.remove(kitap)
                print(f"'{kitap_adi}' adlı kitap kütüphaneden çıkarıldı.")
                kitap_bulundu=True
                break

        if not kitap_bulundu:
            print(f"'{kitap_adi}' adlı kitap kütüphanede bulunamadı.")

    def kitaplari_goster(self):
        if not self.kitaplar:
            print("Kütüphanede hiç kitap yok.")
        else:
            print("Kütüphanedeki Kitaplar:")
            for idx, kitap in enumerate(self.kitaplar,start=1):
                toplam=0
                toplam+=idx
                print(f"{idx}. {kitap['Kitap Adı']} - {kitap['Yazar']}")
            print("Toplam Kitap Sayısı : ",toplam)

bölüm1=Library()

bölüm1.kitap_ekle()
bölüm1.kitaplari_goster()
bölüm1.kitap_çıkar()
bölüm1.kitaplari_goster()
