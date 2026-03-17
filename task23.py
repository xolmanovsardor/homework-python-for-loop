# Maxsus chegirma uchun telefon narxlarini hisoblash
#Telefon do'konida telefonlarning narxlari orasida faqat 5 ga qoldiqsiz bo'linadigan narxlarning yig'indisini hisoblang. [] ishlatmaslik 
yigindi = 0
for narx in range(1, 1001):  
    if narx % 5 == 0:
        yigindi += narx
print("5 ga qoldiqsiz bo'linadigan narxlarning yig'indisi:", yigindi)