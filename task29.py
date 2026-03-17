# Savdo daromadlari o'rtachasini hisoblash
#Har bir savdo nuqtasidagi daromadlar kiritiladi. O'rtacha daromadni hisoblang va float formatda chiqaring.
daromadlar = []
for i in range(5):
    daromad = float(input(f"{i + 1}-savdo nuqtasining daromadini kiriting: "))
    daromadlar.append(daromad)
ortacha_daromad = sum(daromadlar) / len(daromadlar)
print("O'rtacha daromad:", ortacha_daromad)