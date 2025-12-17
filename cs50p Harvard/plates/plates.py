marks = [".", ":", ";", "'", ",", "?", "!"]

def main():
    plate = input("Plate: ")
    if isValid(plate):
        print("Valid")
    else:
        print("Invalid")

def isValid(inp):
    if not (2 <= len(inp) <= 6):
        return False
    if inp[0:2].isdigit():
        return False


    firstNumberIndex = -1
    for i in range(0, len(inp)):
        if inp[i].isdigit():
            firstNumberIndex = i
            if int(inp[firstNumberIndex]) == 0:
                return False
            break
    if firstNumberIndex != -1:
        for i in range(firstNumberIndex, len(inp)):
            if not inp[i].isdigit():
                return False

    for m in marks:
        if inp.find(m) != -1:
            return False


    else:
        return True

main()
