#
# Author: Hakan CERAN
# Date:12.10.2021
# Content: Sayı Tahmin Oyunu
#

from random import randint

rand = randint(1, 100)

sayac = 0

print("Sayi tahmin oyunu baslamistir. Cikmak icin 0 giriniz.")

while True:
    sayac += 1
    sayi = int(input("1 ile 100 arasinda bir deger girin: "))

    if (sayi == 0):
        print("Oyunu iptal ettiniz.")
        break

    if (sayi < rand):
        print("Yukari")
        continue
    elif (sayi > rand):
        print("Asagi")
        continue
    else:
        print("")
        print("Tebrikler ", sayac, "denemede ", rand, "sayisini buldunuz.")
        break