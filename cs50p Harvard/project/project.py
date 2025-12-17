import random
import math

cheers = ["AHAHAHAHAHA YES!!!!!!!!", "WOOOOHOOOO!!!!!!", "AYYYYYYYE!!!!!!!!!!!!", "YESSSSS!!!!!!!", "COOOREEEEEECT!!!!!!!!!!!!!", "AHHAHAHAHAAH!!!!!!!!",
          "WOOOOOOOO!!!!!!!", "SHEEEEEEEESH!!!!!!!", "BRO IS COOKING!", "EXACTLYYYYYYYY!!!!!", "THATS RIGHTTTTTT!!!!!!!!!!!!!", "THATS CORREEEEECT!!!!!!"]


def main():
    level = 0

    print()
    print("WELCOME TO MATH QUIZ!")
    print("CHOOSE A LEVEL????? ")
    print("1 is meh")
    print("2 is Alright ")
    print("3 is... ... ... ... ... 💀🙏")
    print("(and by the way if you see division (/), TAKE THE FLOOR FOR THE CORRECT ANSWER!) (for example 9/10 = 0)")
    print()
    while 1:
        try:
            level = int(input("(1 or 2 or 3): "))
            if level == 1 or level == 2 or level == 3:
                break
            if level != 1 or level != 2 or level != 3:
                raise Exception
        except Exception:
            print("I SAID (1 OR 2 OR 3)!!!!")
    if level == 1:
        print(play1())
    elif level == 2:
        print(play2())
    elif level == 3:
        print(play3())

def add(a, b):
    return a+b


def sub(a, b):
    return a-b


def mul(a, b):
    return a*b


def fdiv(a, b):
    return math.floor(float(a/b))


####################################################################################################################


def play1():
    question = 1
    corrects = 0
    while question != 6:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        op = random.choice(["+", "-"])
        try:
            inp = int(input(f"{a} {op} {b} = "))
        except Exception:
            print("really?")
            continue

        if op == "+":
            ans = a+b
            if inp == ans:
                corrects += 1
                question += 1
                print(random.choice(cheers))
                continue
            else:
                question += 1
                print("💀🥀")
                continue
        elif op == "-":
            ans = a-b
            if inp == ans:
                corrects += 1
                question += 1
                print(random.choice(cheers))
                continue
            else:
                question += 1
                print("💀🥀")
                continue
    fin = (corrects/5)*100
    quote = ""
    if fin == 0:
        quote = "🤣"
    elif fin == 20:
        quote = "😆"
    elif fin == 40:
        quote = "😏"
    elif fin == 60:
        quote = "👍"
    elif fin == 80:
        quote = "😮"
    elif fin == 100:
        quote = "😱🤑🤩💲💀🔥"
    return f"{fin}% {quote}"


def play2():
    question = 1
    corrects = 0
    while question != 6:
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        op = random.choice(["+", "-", "*"])
        try:
            inp = int(input(f"{a} {op} {b} = "))
        except Exception:
            print("really?")
            continue

        if op == "+":
            ans = a+b
            if inp == ans:
                corrects += 1
                question += 1
                print(random.choice(cheers))
                continue
            else:
                question += 1
                print("💀🥀")
                continue
        elif op == "-":
            ans = a-b
            if inp == ans:
                corrects += 1
                question += 1
                print(random.choice(cheers))
                continue
            else:
                question += 1
                print("💀🥀")
                continue
        elif op == "*":
            ans = a*b
            if inp == ans:
                corrects += 1
                question += 1
                print(random.choice(cheers))
                continue
            else:
                question += 1
                print("💀💀🥀")
                continue
    fin = (corrects/5)*100
    quote = ""
    if fin == 0:
        quote = "🤣🤣🤣🤣🤣"
    elif fin == 20:
        quote = "😆😆😆😆😆"
    elif fin == 40:
        quote = "😏😏😏😏😏"
    elif fin == 60:
        quote = "👍👍👍👍👍"
    elif fin == 80:
        quote = "😮😮😮😮😮"
    elif fin == 100:
        quote = "🔥💀💲🔥💀💲🔥💀💲🔥💀😱🔥🔥💀🔥🔥💀🤑🔥💲🔥💀🤩💀🔥💲💀🔥🔥"
    return f"{fin}% {quote}"


def play3():
    question = 1
    corrects = 0
    while question != 6:
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        op = random.choice(["+", "-", "*", "/"])
        try:
            inp = int(input(f"{a} {op} {b} = "))

        except Exception:
            print("really?")
            question += 1
            continue

        if op == "+":
            ans = a+b
            if inp == ans:
                corrects += 1
                question += 1
                print(random.choice(cheers))
                continue
            else:
                question += 1
                print("💀🥀")
                continue
        elif op == "-":
            ans = a-b
            if inp == ans:
                corrects += 1
                question += 1
                print(random.choice(cheers))
                continue
            else:
                question += 1
                print("💀🥀")
                continue
        elif op == "*":
            ans = a*b
            if inp == ans:
                corrects += 1
                question += 1
                print(random.choice(cheers))
                continue
            else:
                question += 1
                print("💀💀🥀")
                continue
        elif op == "/":
            

            ans = math.floor(float(a/b))
            if inp == ans:
                corrects += 1
                question += 1
                print(random.choice(cheers))
                continue
            else:
                question += 1
                print("💀🥀")
                continue
    fin = (corrects/5)*100
    quote = ""
    if fin == 0:
        quote = "🤣🤣🤣🤣🤣"
    elif fin == 20:
        quote = "😆😆😆😆😆"
    elif fin == 40:
        quote = "😏😏😏😏😏"
    elif fin == 60:
        quote = "👍👍👍👍👍"
    elif fin == 80:
        quote = "😮😮😮😮😮"
    elif fin == 100:
        quote = "🔥💀🔥💀💲🔥💀💲🔥💀💲🔥💀😱🔥🔥💀😱🔥🔥💀🔥🔥💀🤑🔥💲🔥💀🤩💀🔥💲💀🔥🔥🔥💀💲🔥💀💲🔥💀💲🔥💀😱🔥🔥💀🔥🔥💀🤑🔥💲🔥💀🤩💀🔥💲💀🔥🔥"
    return f"{fin}% {quote}"


####################################################################################################################


if __name__ == "__main__":
    main()
