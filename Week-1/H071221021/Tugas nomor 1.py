#menghitung panjang kapal
import math
h = float(input('Masukkan tinggi menara : '))
b = float(input('Masukan sudut elevasi Pengamat terhadap ujung kapal : '))
a = float(input('Masukan sut elevasi pengamat terhadap ujung belakang kapal: '))

ac = math.tan(math.radians(a))*h
bc = math.tan(math.radians(b))*h
result = (ac - bc)

print("{:.1f}m".format(result))