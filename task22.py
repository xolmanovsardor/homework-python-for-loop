#Telefonlarning eng katta va eng kichik narxining o'rtachasini topish
raqamlar = []
for i in range(7):
    raqam = float(input(f"{i + 1}-raqamni kiriting: "))
    raqamlar.append(raqam)
eng_katta_narx = max(raqamlar)
eng_kichik_narx = min(raqamlar)
ortacha_narx = (eng_katta_narx + eng_kichik_narx) / 2
print("Eng katta narx:", eng_katta_narx)
print("Eng kichik narx:", eng_kichik_narx)
print("O'rtachasi:", ortacha_narx)