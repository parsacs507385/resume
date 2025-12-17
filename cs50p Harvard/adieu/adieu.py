names = []

while 1:
    try:
        name = input("Name: ").strip()
        # if name == "":
        #     break
        names.append(name)


    except EOFError:
        print()
        break
final = str(names[0])

if len(names) == 1:
    final = names[0]
elif len(names) == 2:
    final = names[0] + " and " + names[1]
else:
    for i in range(1, len(names)-1):
        final += ", " + names[i]
    final += ", and " + names[len(names)-1]
print(f"Adieu, adieu, to {final}")
