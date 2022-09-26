jari_jari_alas = 18
tinggi = 21
sisi = ((jari_jari_alas**2)+(tinggi**2))**(1/2)

import math
volume = (1/3)*math.pi*(jari_jari_alas**2)*tinggi
luas_permukaan = (math.pi*jari_jari_alas*sisi) + (math.pi*(jari_jari_alas**2))

print ('Volume = {:.2f} cm'.format(volume))
print ('Luas permukaan = {:.2f} cm'.format(luas_permukaan))