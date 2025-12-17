import sys


def main():
    print(lines())


def lines():
    if len(sys.argv) == 2:
        if sys.argv[1].endswith('.py'):
            try:
                with open(sys.argv[1]) as file:
                    counter = 0
                    for line in file:
                        if not (remove_comments(line) or remove_docstrings(line) or remove_whitespace(line)):
                            counter += 1
                    return counter
            except FileNotFoundError:
                sys.exit('File does not exist')
        else:
            sys.exit('Not a Python file')
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    else:
        sys.exit('Too few command-line arguments')


def remove_comments(line):
    return (line.lstrip().startswith('#'))


def remove_docstrings(line):
    return line.lstrip().startswith("'''")


def remove_whitespace(line):
    return len(line.lstrip()) == 0


if __name__ == "__main__":
    main()




# import sys
# arg = ""
# lines = []
# count = 0

# if len(sys.argv) <= 1:
#     print("Too few args")
#     sys.exit()
# elif 2 < len(sys.argv):
#     print("Too many args")
#     sys.exit()
# arg = sys.argv[1]
# if arg[-2:] != "py":
#     print("Not a Python file")
#     sys.exit()


# try:
#     with open(arg, "r") as f:
#         lines = f.readlines()

# except FileNotFoundError:
#     print("File not found")
#     sys.exit()


# for line in lines:
#     if line[0] == "#" or line == "\n":
#         continue
#     count += 1

# print(f"Lines of ACTUAL code: {count}")
