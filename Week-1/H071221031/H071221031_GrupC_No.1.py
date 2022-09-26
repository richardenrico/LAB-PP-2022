print('=====Menghitung panjang kapal=====')

h= int(input('Masukkan tinggi menara : '))
a = int(input('Sudut elevasi pengamat terhadap ujung belakang kapal : '))
b= int(input('Sudut elevasi pengamat terhadap ujung depan kapal : '))

import math
belakang = h * (math.tan(math.radians(a)))
depan = h * (math.tan(math.radians(b)))
panjang = belakang-depan

print("Panjang Kapalnya adalah", panjang , "m")