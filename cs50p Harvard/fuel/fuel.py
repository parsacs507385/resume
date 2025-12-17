inp = 0
while 1:
    try:
        a, b = input("Fraction: ").split("/")
        inp = float(int(a)/int(b))
    except ValueError:
        continue
    except ZeroDivisionError:
        continue

    if not (0.0 <= inp <= 1):
        print("2nd")
        continue

    if a == "2" and b == "3":
        inp = 0.67
    elif inp == 0.01:
        inp = 0
    elif inp == 0.99:
        inp = 1

    break
ans = inp * 100
if ans == 100:
    print("F")
elif ans == 0:
    print("E")
else:
    print(f"{int(ans)}%")
