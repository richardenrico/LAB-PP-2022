total_detik = int(input('Detik :'))

jam = total_detik//3600
sisa_detik = total_detik%3600
menit = sisa_detik//60
detik = sisa_detik%60

print ('{:02d}:{:02d}:{:02d}'.format (jam, menit, detik))