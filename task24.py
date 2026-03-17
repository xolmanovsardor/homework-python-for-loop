# Sinfdagi talabalarning umumiy ballini hisoblash
# Sinfda 10 ta talaba bor. Ularning har birining imtihon natijalarini kiritib, umumiy ballini hisoblang. [] ishlalatmasik
talaba_ballar = []
for i in range(10):
    ball = float(input(f"{i + 1}-talabaning ballini kiriting: "))
    talaba_ballar.append(ball)
umumiy_ball = sum(talaba_ballar)
print("Sinfda umumiy ball:", umumiy_ball)