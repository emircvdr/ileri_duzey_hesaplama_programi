import math


print("""
***********************************************
İşlemler :
1 = Faktoriyel Alma
2 = En Yakın En Büyük Sayıya Yuvarlama
3 = En Yakın En Küçük Sayıya Yuvarlama
4 = Karesini Alma
5 = Kübünü Alma
6 = Permutasyonunu Alma
7 = 10 tabanında Log Alma
8 = 2 tabanında Log Alma
9 = İstediğiniz tabanda Log Alma
***********************************************
""")

işlem = input("Lütfen Gerçekleştirmek İstediğiniz İşlem Numarasını Giriniz. ")
while True:
    if işlem == '1':
        sayi = int(input("Faktoriyelini Almak İstediğiniz Sayıyı Giriniz:"))
        faktoriyel = math.factorial(sayi)
        print("Sayınızın Faktoriyeli",faktoriyel)
        break
    elif işlem == "2":
        sayi = float(input("Yuvarlamak İstediğiniz Sayıyı Giriniz:"))
        yyuvarlama = math.ceil(sayi)
        print("Sayınızın Yuvarlanmış Hali",yyuvarlama)
        break
    elif işlem == "3":
        sayi = float(input("Yuvarlamak İstediğiniz Sayıyı Giriniz:"))
        ayuvarlama = math.floor(sayi)
        print("Sayınızın Yuvarlanmış Hali", ayuvarlama)
        break
    elif işlem == "4":
        sayi = int(input("Karesini Almak İstediğiniz Sayıyı Giriniz:"))
        kare = math.pow(sayi,2)
        print("Sayınızın Karesi ", kare)
        break
    elif işlem == "5":
        sayi = int(input("Kübünü Almak İstediğiniz Sayıyı Giriniz:"))
        küp = math.pow(sayi, 3)
        print("Sayınızın Karesi ", küp)
        break
    elif işlem == "6":
        print("""Permütasyon işlemi : p(n,r)
        P(n,r) = n! / (n-r)! 'dir.
        O yüzden 2 tane sayı tanımlamalısınız.
        """)
        sayi1 = int(input(" n Sayısını Giriniz:"))
        sayi2 = int(input(" r Sayısını Giriniz:"))
        permü = math.perm(sayi1, sayi2)
        print("Permütasyon Sonucu ", permü)
        break
    elif işlem =="7":
        sayi = int(input("10 Tabanında Log Almak İstediğiniz Sayıyı Giriniz:"))
        onlog = math.log10(sayi)
        print("Sayınızın 10 Tabanında Logu ", onlog)
        break
    elif işlem == "8":
        sayi = int(input("2 Tabanında Log Almak İstediğiniz Sayıyı Giriniz:"))
        ikilog = math.log2(sayi)
        print("Sayınızın 2 Tabanında Logu ", ikilog)
        break
    elif işlem == "9":
        sayi1 = int(input("Logunu Almak İstediğiniz Sayıyı Giriniz:"))
        sayi2 = (input("Girdiğiniz Sayının Hangi Tabanda Olacağını Giriniz.Eğer e tabanında girmek isterseniz 'e' basmanız yeterli..:"))
        if sayi2 == "e":
            log = math.log(sayi1)
            print("Sayınızın Log Değer",log)
            break
        elif sayi2 != "e":
            log = math.log(int(sayi1),int(sayi2))
            print("Sayınızın Log Değeri ", log)
            break
