height = float(input("Masukkan tinggi menara : "))
a = float(input("Masukkan sudut elevasi terhadap ujung belakang kapal : "))
b = float(input("Masukkan sudut elevasi terhadap ujung depan kapal : "))

import math
tan_a = math.tan(math.radians (a))
tan_b = math.tan(math.radians (b))

ac = height*tan_a
bc = height*tan_b

# ab?
ab = ac - bc

print ('panjang kapal = {:.1f} m'. format (ab))