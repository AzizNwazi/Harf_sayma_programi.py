from HarfSayma_Modul import * # metottan fonksiyona erişim sağla

metin = input("Metin giriniz: ")  # kullanıcadan metni al

sonuc = harf_sayilari(metin)  # harf sayılarını hesapla ve sonuc parametresine ata
print("Harf sayilari:\n")

for i, j in sonuc.items():  # harfsayılarını yazdır
    print(f"{i} : {j} kes gecti") # birar satır aralıklarla her harfin kaç kes geçtiğini bastır
