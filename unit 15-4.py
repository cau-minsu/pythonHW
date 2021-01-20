age = int(input())
balance = 9000
if 7<=age<=12:
    print(balance-650)
elif 13<=age<=18:
    print(balance-1050)
elif 19<=age:
    print(balance-1250)
else:
    print('잘못된 입력')