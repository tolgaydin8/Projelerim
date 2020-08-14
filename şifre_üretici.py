import string
import random

if __name__ == "__main__":
    harfler = string.ascii_letters # Büyüklü küçüklü harfler 
    rakamlar = string.digits #0123456789
    bazi_semboller = ["!","?","%","/","&","<",">",".",",","_","=","+","-","*",")","("]
    liste = []
    liste.extend(list(harfler))
    liste.extend(list(rakamlar))
    liste.extend(bazi_semboller)
    def random_sifre():    
        uzunluk = abs(int(input("Lütfen şifrenin uzunluğunu giriniz: "))) 
        while uzunluk < 8:
            print("lütfen 8'den fazla sayı giriniz")
            uzunluk =abs(int(input("Lütfen şifrenin uzunluğunu giriniz: ")))
            
            continue
        else:
            random.shuffle(liste)
            print("Şifeniz: "+ "".join(liste[0:uzunluk]))
    
    while True:    
        try:
            random_sifre()
            break
        except ValueError:
            print("lütfen sayı giriniz")
        


