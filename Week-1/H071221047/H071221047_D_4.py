detik = int(input())
jam = detik // 3600
sisa_detik = detik % 3600
menit = sisa_detik // 60
detik_real = sisa_detik % 60


print("%02d:%02d:%02d" % (jam,menit,detik_real))

