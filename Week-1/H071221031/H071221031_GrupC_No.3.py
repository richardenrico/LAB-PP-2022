print("=====Menghitung Jumlah Tagihan Listrik bulanan=====")
nilai = input("rata-rata pemakaian listrik harian(wh): ")
tarif_listrik = 1325
wh = int(nilai)

## Mengubah wh jadi kwh##
harian= int(wh/1000)
bulanan = int(harian * 30)
harga = int(bulanan * tarif_listrik)

print("jumlah tagihan listrik bulanan : Rp.", round(harga,2))