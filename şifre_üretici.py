import string
import random
import os

if __name__ == "__main__":
    harfler = string.ascii_letters # Büyüklü küçüklü harfler 
    rakamlar = string.digits #0123456789
    bazi_semboller = string.punctuation #semboller 
    liste = []
    liste.extend(list(harfler))
    liste.extend(list(rakamlar))
    liste.extend(list(bazi_semboller))
    def random_sifre():
        os.system("cls")    
        uzunluk = abs(int(input("Lütfen rastgele şifreniz için 7'den büyük olucak şekilde şifre uzunluğunu tam sayı olarak giriniz : "))) 
        while uzunluk < 8:
            os.system("cls")
            
            uzunluk =abs(int(input("Lütfen rastgele şifreniz için 7'den büyük olucak şekilde şifre uzunluğunu tam sayı olarak giriniz :")))
            
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
            pass
        
