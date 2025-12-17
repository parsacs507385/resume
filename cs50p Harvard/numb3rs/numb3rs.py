import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        matches = re.search("^(.+)\.(.+)\.(.+)\.(.+)$", ip)

        if matches:
            num1 = matches.group(1)
            num2 = matches.group(2)
            num3 = matches.group(3)
            num4 = matches.group(4)


            if len(str(num1)) == 1 and len(str(num2)) == 1 and len(str(num3)) == 1  and len(str(num4)) == 1:
                if (not(0 <= int(num1) <= 9)) or (not(0 <= int(num2) <= 9)) or (not(0 <= int(num3) <= 9)) or (not(0 <= int(num4) <= 9)):
                    return False
            if len(str(num1)) == 2 and len(str(num2)) == 2 and len(str(num3)) == 2  and len(str(num4)) == 2:
                if (not(10 <= int(num1) <= 99)) or (not(10 <= int(num2) <= 99)) or (not(10 <= int(num3) <= 99)) or (not(10 <= int(num4) <= 99)):
                    return False
            if len(str(num1)) == 3 and len(str(num2)) == 3 and len(str(num3)) == 3  and len(str(num4)) == 3:
                if (not(100 <= int(num1) <= 255)) or (not(100 <= int(num2) <= 255)) or (not(100 <= int(num3) <= 255)) or (not(100 <= int(num4) <= 255)):
                    return False

            if 255<int(num1) or int(num1) < 0:
                return False
            elif 255<int(num2) or int(num2) < 0:
                return False
            elif 255<int(num3) or int(num3) < 0:
                return False
            elif 255<int(num4) or int(num4) < 0:
                return False
            else:
                return True
        else:
            return False
    except ValueError:
        return False


if __name__ == "__main__":
    main()



# import sys


# def main():
#     print(validate(input("IPv4 Address: ")))

# def validate(parInp:str):

#     inp = parInp
#     numList = inp.split(".")
#     if len(numList) != 4:
#         return "False"

#     try:
#         for num in numList:
#             if not (0 <= int(num) <= 255):
#                 raise ValueError
#             if len(str(num)) == 1:
#                 if not (0 <= int(num) <= 9):
#                     raise ValueError
#             if len(str(num)) == 2:
#                 if not (10 <= int(num) <= 99):
#                     raise ValueError
#             if len(str(num)) == 3:
#                 if not (100 <= int(num) <= 255):
#                     raise ValueError

#     except ValueError:
#         return "False"

#     return "True"

# if __name__ == "__main__":
#     main()
