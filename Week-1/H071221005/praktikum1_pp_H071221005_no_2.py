detik = int(input("Masukkan Jumlah Detik: "))

jam = int(detik / 3600)
menit = int((detik % 3600) / 60)
detik = int(detik % 3600) % 60

print(jam,':',menit,':',detik)