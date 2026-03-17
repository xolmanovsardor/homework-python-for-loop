# Sonlarning kublarini yig'ish
N = int(input("N ni kiriting: "))
yigindi = 0
for i in range(1, N + 1):
    yigindi += i ** 3
print("Sonlarning kublarini yig'indisi:", yigindi)