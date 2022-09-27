tinggi = float(input('Masukan Tinggi Menara (Dalam m) : '))
a = float(input('Masukan Derajat Elevensi Pengamat Terhadap Ujung Belakang Kapal : '))
b = float(input('Masukkan Derajat Sudut Elevasi Pengamat Terhadap Ujung Depan Kapal : ')) 
import math
belakang = tinggi * (math.tan(math.radians(a)))
depan = tinggi * (math.tan(math.radians(b)))
panjangkapal = (belakang - depan) 
print('Panjang Kapal Adalah %.1fm'% panjangkapal)