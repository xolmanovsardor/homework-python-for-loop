#Eng katta va eng kichik son o'rtachasi
raqamlar = []
for i in range(7):
    raqam = float(input(f"{i + 1}-raqamni kiriting: "))
    raqamlar.append(raqam)
eng_katta_son = max(raqamlar)
eng_kichik_son = min(raqamlar)
ortacha = (eng_katta_son + eng_kichik_son) / 2
print("O'rtachasi:", ortacha)

