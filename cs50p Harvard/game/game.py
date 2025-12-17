from random import randint

while 1:
    try:
        n = int(input("Level: "))
        if n <= 0:
            raise ValueError
        break
    except ValueError:
        pass

rand = randint(1, n)
while 1:
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            raise ValueError
        if guess < rand:
            print("Too small!")
        elif guess > rand:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass
