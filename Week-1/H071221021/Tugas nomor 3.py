#Menghitung volume Bola

import math
d = float(input('Diameter bola :'))

phi = math.pi
v = phi * (d**3)/6

print("Volume bola = {:.1f}". format(v))