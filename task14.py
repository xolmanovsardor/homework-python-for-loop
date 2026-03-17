#  Kollektorning umumiy daromadini hisoblash
# Foydalanuvchi tomonidan kiritilgan 3 oylik daromadlar ro'yxatidan umumiy daromadni hisoblang.
daromadlar = []
for i in range(3):
    daromad = float(input(f"{i + 1}-oy daromadini kiriting: "))
    daromadlar.append(daromad)
umumiy_daromad = sum(daromadlar)
print("Kollektorning umumiy daromadi:", umumiy_daromad)