print('=====Program Konversi Detik Ke Jam=====')
jumlah_detik = int(input('Masukkan Jumlah detik yang ingin di konversi : '))
 
jam = jumlah_detik //3600
sisa_detik = jumlah_detik - 3600*jam
menit = sisa_detik // 60
Detik = sisa_detik - 60*menit

print(jam ,':' , menit , ':' , Detik)