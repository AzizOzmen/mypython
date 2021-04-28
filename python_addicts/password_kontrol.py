import time
sifre =4434
def bekle(sn):
    print("{}sn beklemeniz gerekmektedir!!!".format(sn))
    while sn>=0:
        print(sn,end=",")
        time.sleep(1)
        sn=sn-1
def parolaiste():
    global parola
    parola=int(input("4 haneli kilit şifresini giriniz:"))
while True:
    parolaiste()
    sayac=1
    if parola==sifre:
        print("GİRİŞ DOĞRULANDI.")
        break
    elif parola!=sifre:
        print("HATALI ŞİFRE")
        while True:
            sayac+=1
            parolaiste()
            if parola==sifre:
                print("GİRİŞ DOĞRULANDI")
                sayac=1
                break
            elif sayac>=0 and sayac<3:
                print("HATALI ŞİFRE")
            elif sayac>=3 and sayac<5:
                print("HATALI ŞİFRE")
                print("3 ve daha fazla hatalı şifre girdiniz. 3 sn beklemeniz gerekmektedir!")
                bekle(3)
                print()
            elif sayac>=5 and sayac<10:
                print("HATALI ŞİFRE")
                print("5 ve daha fazla hatalı şifre girdiniz. 10 sn beklemeniz gerekmektedir!")
                bekle(10)
                print()
            elif sayac>=10:
                print("HATALI ŞİFRE")
                print("10 ve daha fazla hatalı şifre girdiniz. 30 sn beklemeniz gerekmektedir!")
                bekle(30)
                print()
    break