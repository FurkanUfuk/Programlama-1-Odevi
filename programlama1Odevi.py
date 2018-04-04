# Programlama-1-Odevi
YBS 2008 Programlama1
soru-1
def gelirHesaplama(x,y,z):
    gelir=x+y+z
    return gelir
x=int(input("Finansman Gelirini Giriniz:"))
y=int(input("Pazar Gelrini Giriniz:"))
z=int(input("Kira Gelirini Giriniz:"))
k=gelirHesaplama(x,y,z)
print("Gelirlerinizin Toplamı:",k)
def giderHesaplama(q,w,e,r,t):
    gider=(q+w+e+r+t)
    return gider
q=int(input("Ücret Giriniz:"))
w=int(input("Finansman Giderini Girniz:"))
e=int(input("Pazar Giderini Giriniz:"))
r=int(input("Kira Giderini Giriniz:"))
t=int(input("Muhasebe Giderini Giriniz:"))
u=giderHesaplama(q,w,e,r,t)
print("Giderlerinizin Toplamı:",u)
def karHesaplama(k,u):
    kar=k-u
    return kar
p=karHesaplama(k,u)
print("Karınız:",p)
if (k-u)>1000:
    print("Şirketiniz Kar Etmiştir.Tebrikler.")
elif (k-u)==1000:
    print("Şirketiniz Başabaş Noktasındadır.")
else:
    print("Şirketiniz Zarar Etmiştir.")

soru-2
def ekipmanKullanilabilirlik(x,y):
    kullanılabilirlik=(x-y)/x
    return kullanılabilirlik
x=int(input("Planlanmış Üretim Süresini Giriniz:"))
y=int(input("Plansız Duruş Süresini Giriniz:"))
k=ekipmanKullanilabilirlik(x,y)
print("Kullanılabilirlik Oranınız:",k)
def performansOrani(q,w,x,y):
    performans=(q*w)%(x-y)
    return performans
q=int(input("Standart Çevrim Zamanını Giriniz:"))
w=int(input("Üretim Miktarını Giriniz:"))
p=performansOrani(q,w,x,y)
print("Performans Oranınız:",p)
def kaliteOrani(a,b):
    kalite=a/b
    return kalite
a=int(input("Sağlam Ürün Miktarını Giriniz:"))
b=int(input("Toplam Üretim Miktarını Giriniz:"))
u=kaliteOrani(a,b)
print("Kalite Oranınız:",u)
def oeeHesaplama(k,p,u):
    oee=k*p*u
    return oee
m=oeeHesaplama(k,p,u)
print("Ekipman Etkinlik Oranınız:",m)

soru-3
def ciroHesaplama(x,y):
    ciro=x*y
    return ciro
x=int(input("Satış Miktarını Giriniz:"))
y=int(input("Birim Satış Fiyatını Giriniz:"))
k=ciroHesaplama(x,y)
print("Toplam Cironuz:",k)
def adambasıCiroHesaplama(k,z):
    adambasıCiro=k/z
    return adambasıCiro
z=int(input("Toplam Çalışan Sayısını Giriniz:"))
p=adambasıCiroHesaplama(k,z)
print("Adambaşı Cironuz:",p)
