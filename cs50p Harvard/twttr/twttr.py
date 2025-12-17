vowels = ["A", "E", "U", "I", "O", "a", "e", "u", "i", "o"]
def main():
    inp = input("Input: ").strip()

    print(f"Output: {shorten(inp)}")



def shorten(inp):
    for l in inp:
        if l in vowels:
            inp = inp.replace(l, "")
    return inp



if __name__ == "__main__":
    main()










# vowels = ["A", "E", "U", "I", "O", "a", "e", "u", "i", "o"]
# inp = input("Input: ").strip()

# for l in inp:
#     if l in vowels:
#         inp = inp.replace(l, "")

# print(f"Output: {inp}")
