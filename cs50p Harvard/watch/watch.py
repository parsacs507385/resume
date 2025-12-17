import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r'<iframe(.)*></iframe>', s):
        link_pattern = re.search(r'http(s)*:\/\/(www\.)?youtube\.com\/embed\/([a-zA-Z0-9_-]+)', s)
        if link_pattern:
            return str("https://youtu.be/"+str(link_pattern.group(3)))


if __name__ == "__main__":
    main()







# import sys
# import re
# indexSpan = ()
# indexTitleSpan = ()
# indexStartOfLink = 0
# indexEndOfLink = 0


# def main():
#     print(parse(input("HTML: ")))


# def parse(s):
#     try:
#         indexSpan = re.search("src=", s)
#         indexTitleSpan = re.search("title=", s)
#         if indexSpan == None or indexTitleSpan == None:
#             raise Exception
#     except Exception:
#         sys.exit("INVALID")

#     indexStartOfLink = int(indexSpan.span()[1])+1
#     indexEndOfLink = int(indexTitleSpan.span()[0])-1
#     linkBefore = ""
#     linkAfter = ""
#     for l in s[indexStartOfLink:indexEndOfLink]:
#         linkBefore = str(linkBefore)+str(l)

#     linkAfter = linkBefore.replace("www.youtube.com/embed", "youtu.be")
#     return str(linkAfter)


# if __name__ == "__main__":
#     main()
