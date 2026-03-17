# Juft va toq sonlarning yig'indisini alohida hisoblash
N = int(input("N ni kiriting: "))
juft_yigindi = 0
toq_yigindi = 0
for i in range(1, N + 1):
    if i % 2 == 0:
        juft_yigindi += i
    else:
        toq_yigindi += i
print("Juft sonlarning yig'indisi:", juft_yigindi)
print("Toq sonlarning yig'indisi:", toq_yigindi)