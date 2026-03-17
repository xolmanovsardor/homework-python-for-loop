# Eng katta sonni topish
raqamlar = []
for i in range(7):
    raqam = float(input(f"{i + 1}-raqamni kiriting: "))
    raqamlar.append(raqam)
eng_katta_son = max(raqamlar)
print("Eng katta son:", eng_katta_son)