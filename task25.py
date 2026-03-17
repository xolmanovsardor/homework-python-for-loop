#  Sinfdagi talabalarning o'rtacha yoshini hisoblash
# Sinfdagi 5 ta talabalarning yoshini kiriting. Ularning o'rtacha yoshini toping va float formatda chiqaring. [] ishlatmaslik
yoshlar = []
for i in range(5):          
    yosh = float(input(f"{i + 1}-talabaning yoshini kiriting: "))
    yoshlar.append(yosh)
urtacha_yosh = sum(yoshlar) / len(yoshlar)
print("Sinfda o'rtacha yosh:", urtacha_yosh)   