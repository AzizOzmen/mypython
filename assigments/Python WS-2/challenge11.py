numara = int(input("kac sayı gireceksiniz\n"))
sayac = 0
start = 0
while sayac < numara:
    sayi = int(input("sayilar"))
    if sayi > start:
        start = sayi
    sayac += 1
print(start)