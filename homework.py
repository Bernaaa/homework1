#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


"""


#SORU 1
tmp = 0
x = input("Haftanin gününü sayi olarak girin(Pazartesi 1):")
gun = int(x) 

y = input("Çıkmak istediğiniz saati girin:")
saat = int(y)

z = input("Yaşınızı giriniz:")
yas = int(z)



if ((gun == 6) or (gun == 7)):
    print("Sokağa çıkmak yasak.")
    
if((gun > 0) and (gun <= 5)):
    
    if(yas >= 65):
        if((saat >= 10) and (saat <= 13)):
            print("Sokağa çıkabilirsiniz.")
        else:            
            print("Sokağa çıkmak yasak.")
    if(yas < 20):
        if((saat >= 13) and (saat <=16)):
            print("Sokağa çıkabilirsiniz.")
        else:
            print("Sokağa çıkmak yasak")
    if((yas > 20) and (yas < 65)):
        if((saat >= 5) and (saat <= 21)):
            print("Sokağa çıkabilirsiniz.")
        else:
            print("Sokağa çıkmak yasak.")


#SORU 2
x = input("alt_deger giriniz:")
alt_deger = int(x)
y = input("ust_deger giriniz:")
ust_deger = int(y)
tmp = 1
for z in range(ust_deger):
    tmp *= alt_deger
print(tmp)

#SORU 3
x = input("alt_deger giriniz:")
alt_deger = int(x)
y = input("ust_deger giriniz:")
ust_deger = int(y)
tmp2 = 1
while(ust_deger >= 1):
    tmp2 *= alt_deger
    ust_deger = ust_deger - 1
print(tmp2)

#SORU 4
tmp = 0
sayı = input("İkilik sistemde sayı giriniz:")
i = len(sayı)
for y in range(i):
    tmp += (int(sayı[y]))*((2)**(i-1-y))  
   
print("Sayının onluk sistemdeki degeri:",tmp)
    
