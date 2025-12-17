import validators
import sys


inp = str(input("Email: ").strip())
if inp.count("@") != 1:
    print("INVALID")
elif validators.email(inp) == False:
    print("INVALID")
else:
    print("VALID")


# import re
# import sys
# TODO
# marks = []

# inp = str(input("Email: ").strip())

# for l in inp:
#     if l in marks:
#         sys.exit("INVALID")

# if len(re.findall("@", inp)) != 1 or len(re.findall(".", inp)) != 1:
#     sys.exit("INVALID")
# indexAt = inp.find("@")
# indexDt = inp.find(".")

# if indexAt == 0:
#     sys.exit("INVALID")
# if indexDt < indexAt:
#     sys.exit("INVALID")
# if indexDt == indexAt+1:
#     sys.exit("INVALID")
# if len(inp) == indexDt+1:
#     sys.exit("INVALID")

# print("Valid")
