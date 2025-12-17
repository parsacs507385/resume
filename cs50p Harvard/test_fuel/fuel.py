import sys

while 1:
    try:
        y =list(map(int,input("Fraction:").split('/')))
        for num in y:
            if num < 0:
                raise ValueError
        if(y[0]>y[1]):
            continue
        break
    except ValueError:
        sys.exit(1)
    except ZeroDivisionError:
        pass

a=(y[0]/y[1])
b=a*100
c=round(b)

try:
    if (99 <= c):
        print("F")
    elif (0 <=c <= 1):
        print("E")
    elif (c < 0):
        raise ValueError
    else:
        print(f"{c}%")
except ValueError:
    sys.exit(1)


# def main():
#     while 1:
#         try:
#             fuel = gauge(convert(input("Fraction: ")))
#             print(fuel)
#             break
#         except ValueError:
#             print("Invalid fraction")
#         except ZeroDivisionError:
#             print("Invalid fraction")


# def convert(fraction):
#     a, b = fraction.split("/")
#     if (not a.isdigit()) or (not b.isdigit()):
#         raise ValueError
#     if int(b) == 0:
#         raise ZeroDivisionError
#     if int(b) < int(a):
#         raise ValueError
#     return round((int(a)/int(b))*100)


# def gauge(percentage):
#     if percentage <= 1:
#         return "E"
#     elif percentage >= 99:
#         return "F"
#     elif percentage < 0:
#         sys.exit(1)
#     else:
#         return f"{percentage}%"


# if __name__ == "__main__":
#     main()
