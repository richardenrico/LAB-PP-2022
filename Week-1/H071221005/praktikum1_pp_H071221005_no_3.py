watt = input('Total Konsumsi Daya Listrik (Dalam watt) : ')
kwh = (int(watt) / 1000 * 1352 * 30 //1)
print("Jumlah Tagihan Listrik Dalam Sebulan : Rp",kwh)