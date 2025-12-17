import re


def main():
    print(count(input("Text: ")))


def count(s):
    valid = r"\bum\b(\?|\s|'|\.''|,|.+|$)"
    matches = re.findall(valid, s, re.IGNORECASE)
    return len(matches)


if __name__ == "__main__":
    main()


# import re

# def main():
#     print(count(input("Text: ").lower()))


# def count(s):
#     times = 0
#     times = s.count(" um...") + s.count(" um, ") + s.count(" um ") + s.count(" um? ")
#     if (2 == len(s)) and s[0] == "u" and s[1] == "m":
#         times += 1
#     elif (2 < len(s)) and (s[0] == "u") and (s[1] == "m") and (s[2] == "," or s[2] == "?" or s[2] == "."):
#         times += 1
#     return int(times)




# if __name__ == "__main__":
#     main()
