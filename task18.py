#Toq sonlarning yig'indisi (1 dan N gacha)
N = int(input("N ni kiriting: "))
yigindi = 0
for i in range(1, N + 1):
    if i % 2 == 1:
        yigindi += i
print("Toq sonlarning yig'indisi:", yigindi)

