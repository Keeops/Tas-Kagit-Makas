import sys
def cikis():
    print("Kapatılıyor...")
    sys.exit()
def acilis():
    print("-*"*20)
    print("\tTaş Kağıt Makas Oyunu")
    print("*-"*20)
    print("\t    Made By Keops")
    print("-*"*20)
def oyun():
    print("""
(1): Yeni Oyun
(2): İstatistikler (Eklenecek)
(0): Çıkış

Hangisini Yapmak İstersiniz ?: """,end="")

def oynanis():
    print("""
(1): Taş
(2): Kağıt
(3): Makas

1.Oyuncu Hangisini Yapmak İstiyor? : """,end="")
def oyna(hamle_1,hamle_2):
    if hamle_1 == hamle_2:
        print("\n\tBeraberlik")
    elif (hamle_1=="tas" and hamle_2=="makas"):
        print("\n\t1.Oyuncu Kazandı")
    elif (hamle_1=="tas" and hamle_2=="kagit"):
        print("\n\t2.Oyuncu Kazandı")
    elif (hamle_1=="kagit"and hamle_2=="tas"):
        print("\n\t1.Oyuncu Kazandı")
    elif (hamle_1=="kagit"and hamle_2=="makas"):
        print("\n\t2.Oyuncu Kazandı")
    elif (hamle_1=="makas"and hamle_2=="tas"):
        print("\n\t2.Oyuncu Kazandı")
    elif (hamle_1=="makas"and hamle_2=="kagit"):
        print("\n\t1.Oyuncu Kazandı")
x="tas"
y="kagit"
z="makas"
acilis()
while True:
    oyun()
    a=int(input())
    try:
        if a == 0:
            cikis()
        elif a==1:
            oynanis()
            b=int(input())
            c=int(input("2.Oyuncu Hangisini Yapmak İstiyor? : "))
            if b==1:
                b=x
            elif b==2:
                b=y
            elif b==3:
                b=z
            else:
                print("\nSadece 1,2,3 girebilirsiniz!...")

            if c==1:
                c=x
            elif c==2:
                c=y
            elif c==3:
                c=z
            else:
                print("\nSadece 1,2,3 girebilirsiniz!...")
            oyna(b,c)
        else:
            print("\nLütfen Sadece Belirtilen İşlemleri Giriniz...")
    except ValueError:
        print("\nLütfen Sadece Belirtilen İşlemleri Giriniz...")
