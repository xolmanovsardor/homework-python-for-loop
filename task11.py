#Sonlarning kvadratlarini yig'ish
# Foydalanuvchi kiritgan N sonigacha bo'lgan sonlarning kvadratlarini yig'indisini hisoblang.
N = int(input("N ni kiriting: "))
yigindi = 0
for i in range(1, N + 1):
    yigindi += i ** 2
print("Sonlarning kvadratlarini yig'indisi:", yigindi)