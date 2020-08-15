import string
import random
import os

if __name__ == "__main__":
    harfler = string.ascii_letters # Büyüklü küçüklü harfler 
    rakamlar = string.digits #0123456789
    bazi_semboller = ["!","?","%","/","&","<",">",".",",","_","=","+","-","*",")","("] #bunu böyle yazmamın sebebi diğer değişik karakterleri (} , { , | , ` vb ) istemememden kaynaklı
    liste = []
    liste.extend(list(harfler))
    liste.extend(list(rakamlar))
    liste.extend(bazi_semboller)
    def random_sifre():
        os.system("cls")    
        uzunluk = abs(int(input("Lütfen rastgele şifre için 7'den büyük sayı giriniz: "))) 
        while uzunluk < 8:
            os.system("cls")
            print("lütfen 7'den fazla sayı giriniz")
            uzunluk =abs(int(input("Lütfen şifrenin uzunluğunu giriniz: ")))
            
            continue
        else:
            os.system("cls") 
            random.shuffle(liste)
            print("Şifeniz: "+ "".join(liste[0:uzunluk]))
    
    while True:    
        try:
            random_sifre()
            break
        except :
            os.system("cls")    
            print("lütfen sayı giriniz")
        


