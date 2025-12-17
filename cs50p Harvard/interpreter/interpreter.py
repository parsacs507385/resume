def do(a, op, b):
    if op == "+":
        return a+b
    elif op == "-":
        return a-b
    elif op == "*":
        return a*b
    elif op == "/":
        if b == 0:
            return 0
        else:
            return round(a/b, 1)

inp = str(input("hmm? ")).strip().split()
a = int(inp[0])
op = inp[1]
b = int(inp[2])
print(float(do(a, op, b)))
