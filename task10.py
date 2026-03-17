# Faktorial hisoblash
# Foydalanuvchi kiritgan N sonining faktorialini hisoblang (N! = N × (N-1) × ... × 1).
N = int(input("N ni kiriting: "))
faktorial = 1
for i in range(1, N + 1):
    faktorial *= i
print("Faktorial:", faktorial)