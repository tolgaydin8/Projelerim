import time
import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox


def uyari_kutusu():
    messagebox.showinfo("UYARI!","""Pomodoron bitti dinlenme vakti
    Hazır olunca Tamam'a bas.""")
def uyari_kutusu2():
    messagebox.showinfo("UYARI!","""Mola bitti pomodoraya devam
    Hazır olunca Tamam'a bas """)
    
def pomodoro_25_dk(): # 25 dk pomodoro ve molanın fonksiyonu
    for i in range(26):
        print(str(25-i)+ " dakika kaldı")
        time.sleep(1)
        os.system("cls")
        if i == 25:
            uyari_kutusu()

def pomodoro_kısa_molda_5_dk():
    for j in range (6):
        print("Molanızın bitmesine "+ str(5-j) + " dakika kaldı")
        time.sleep(1)
        os.system("cls")
        if j == 5:
            uyari_kutusu2()

def pomodoro_uzun_mola_15_dk():
    for j in range (15):
        print("Molanızın bitmesine "+ str(15-j) + " dakika kaldı")
        time.sleep(1)
        os.system("cls")
        if j == 15:
            uyari_kutusu2()


def pomodoro_custom_ders(): 
    for i in range(ders_süresi + 1 ):
        print(str(ders_süresi - i)+ " dakika kaldı")
        time.sleep(1)
        os.system("cls")
        if i == ders_süresi:
            uyari_kutusu()


def pomodoro_custom_kısa_mola():
    for j in range (mola_süresi + 1):
        print("Molanızın bitmesine "+ str(mola_süresi-j) + " dakika kaldı")
        time.sleep(1)
        os.system("cls")
        if j == mola_süresi:
            uyari_kutusu2()


def pomodoro_uzun_mola_custom():
    for j in range (uzun_süresi+1):
        print("Molanızın bitmesine "+ str(uzun_süresi - j) + " dakika kaldı")
        time.sleep(1)
        os.system("cls")
        if j == uzun_süresi:
            uyari_kutusu2()

print("""Merhaba Pomodoro Zamanlayıcısına Hoşgeldin :)
Nasıl bir pomodoro istediğini tuşar mısın? 
1- Klasik pomodoro (25-5-15-4)
2- Kendim yapmak istiyorum """)

while True:
    try:
        sayı = int(input(" "))
    except:
        pass
    try:
        if sayı == 1:
            for j in range(4):
                pomodoro_25_dk()
                pomodoro_kısa_molda_5_dk()
                pomodoro_25_dk()
                pomodoro_kısa_molda_5_dk()
                pomodoro_25_dk()                      #1. Pomodoro dönügüsü
                pomodoro_kısa_molda_5_dk() 
                pomodoro_25_dk()
                pomodoro_uzun_mola_15_dk()
            messagebox.showinfo("UYARI!","""Pomodoron bitti tebrikler!!.""")

        elif sayı == 2 :
            os.system("cls")
            ders_süresi = int(input("ders süresini dakika cinsinen tuşlayınız: "))
            mola_süresi = int(input("Mola süresini dakika cinsinden tuşlayınız: "))
            uzun_süresi = int(input("uzun molda süresini dakika cinsinden tuşlayınız: "))
            tekrar = int (input("tekrar sayısı tuşlayınız: "))
    

        for i in range(tekrar):
            pomodoro_custom_ders()
            pomodoro_custom_kısa_mola()
            pomodoro_custom_ders()
            pomodoro_custom_kısa_mola()
            pomodoro_custom_ders()
            pomodoro_custom_kısa_mola()
            pomodoro_custom_ders()
            pomodoro_uzun_mola_custom()
    except:
        os.system("cls")
        print("""Girdiğiniz değer geçersiz lütfen nasıl bir pomodoro istediğinizi tuşlar mısınız?
        1- Klasik pomodoro (25-5-15-4)
        2-Custom""")
