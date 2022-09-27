#Hitunglah panjang kapal !

a = float(input("Masukkan sudut elevasi pengamat terhadap ujung belakang kapal : "))
b = float(input("Masukkan sudut elevasi pengamat terhadap ujung kapal : "))
h = float(input("Masukkan tinggi menara : "))

import math

ac = math.tan(math.radians(a))*h
bc = math.tan(math.radians(b))*h
result = (ac - bc)

print("{:.1f}m".format(result))