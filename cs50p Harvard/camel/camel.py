inp = str(input("camelCase:"))

for l in inp:
    if l.isupper():
        modifiedL = "_" + l.lower()
        inp = inp.replace(l, modifiedL)

print(inp)
