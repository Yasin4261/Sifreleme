"""
Bu kodu üniversiteye girmek için kullanacağım applybau için yazırlıyorum
"""
from time import sleep


print("Sezar şifreleme\n")
şifre = input("Şifrenizi girin\n")

sleep(1)
print("şifreniz:",şifre)
yeniŞifre = ""
for i in şifre:
    deger = ord(i)
    deger += 1
    deger = chr(deger)
    yeniŞifre  += deger
print("şifreli hali:",yeniŞifre)
