price = 50
owed = 0

while 0 < price:
    print(f"Amount Due: {price}")
    ins = int(input("Insert Coin"))

    if ins == 5 or ins == 10 or ins == 25:
        price -= ins
        if price < 0:
            owed = abs(price)



print(f"Change Owed: {owed}")
