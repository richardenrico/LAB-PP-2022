#Konversi detik ke dalam format jam : menit : detik

detik = int(input('Masukan jumlah detik yang diinginkan : ')) 

jam = detik // 3600
sisa_detik = detik % 3600
menit = sisa_detik // 60
detik = sisa_detik % 60

print("%02d:%02d:%02d"%(jam,menit,detik))