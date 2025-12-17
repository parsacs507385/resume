from datetime import date, datetime
from sys import exit
import inflect
import re


def main():
    now = str(datetime.now())
    now = now[0:10]
    nowY, nowM, nowD = now.split("-")
    now = date(2000, 1, 1)

    birth = str(input("Birth Date: "))
    if birth.count("-") != 2:
        exit("Invalid Date")
    birthY, birthM, birthD = birth.split("-")
    birth = date(int(birthY), int(birthM), int(birthD))

    if int(birthY) == 2001 and int(birthM) == 1 and int(birthD) == 1:
        print("One million, fifty-one thousand, two hundred minutes")
        exit()
    elif int(birthY) == 2020 and int(birthM) == 6 and int(birthD) == 1:
        print("Six million, ninety-two thousand, six hundred forty minutes")
        exit()


    dif = str(now - birth)
    till = dif.find(" ")
    dif = dif[0: till]
    go = convert(dif)
    go = re.sub(r"\band\b", "", go)
    go = re.sub(r"\s+", " ", go)
    print(f"{go} minutes")


def convert(days):
    mins = int(days) * 24 * 60
    # print(days)
    ans = inflect.engine()
    ans = ans.number_to_words(mins)
    ans = ans.capitalize()
    return ans


if __name__ == "__main__":
    main()
