# yoshdagi talabalarni topish
# 7 ta talabaning yoshini kiritib, 21 yoshdan kichik bo'lgan talabalarning sonini toping. [] ishlatmaslik
yoshlar = []
for i in range(7):
    yosh = float(input(f"{i + 1}-talabaning yoshini kiriting: "))
    yoshlar.append(yosh)

kichik_talabalar_soni = 0
for yosh in yoshlar:
    if yosh < 21:
        kichik_talabalar_soni += 1

print("21 yoshdan kichik bo'lgan talabalarning soni:", kichik_talabalar_soni)