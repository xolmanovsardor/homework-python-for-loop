#Minimal qiymatni topish
#Foydalanuvchi tomonidan kiritilgan 7 ta raqam bo'yicha minimal qiymatni toping.
raqamlar = []
for i in range(7):
    raqam = float(input(f"{i + 1}-raqamni kiriting: "))
    raqamlar.append(raqam)
minimal_qiymat = min(raqamlar)
print("Minimal qiymat:", minimal_qiymat)