girilenSayi = input("4 basamaklı sayı giriniz: ")

while True:
    tahmin = input("Tahmininizi giriniz: ")

    if len(tahmin) != 4:
        print("Lütfen 4 basamaklı sayı girin")
        continue

    girilenSayi_list = list(girilenSayi)
    tahmin_list = list(tahmin)

    sonuc = [""] * 4
    dogruYer = 0
    dogruSayi = 0

    for i in range(4):
        if tahmin_list[i] == girilenSayi_list[i]:
            sonuc[i] = "➕"
            dogruYer += 1
            dogruSayi += 1
            girilenSayi_list[i] = None
            tahmin_list[i] = None

    for i in range(4):
        if tahmin_list[i] is not None:
            if tahmin_list[i] in girilenSayi_list:
                sonuc[i] = "⭕"
                dogruSayi += 1
                girilenSayi_list[girilenSayi_list.index(tahmin_list[i])] = None
            else:
                sonuc[i] = "❌"

    print("Sonuç:", " ".join(sonuc))
    print("Doğru yerde:", dogruYer)
    print("Toplam doğru sayı:", dogruSayi)

    if dogruYer == 4:
        print("Sayıyı buldunuz")
        break
