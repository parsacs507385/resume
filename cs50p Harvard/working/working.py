import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        if ":" in s:
            first_hr, second_hr = s.split(" to ")
            findin_first = re.search(r"(.+\:.+) (AM|PM)", first_hr)
            findin_second = re.search(r"(.+\:.+) (AM|PM)", second_hr)
            hr1, min = findin_first.group(1).split(":")
            hr2, min2 = findin_second.group(1).split(":")
        else:
            min = 00
            min2 = 00
            first_hr, second_hr = s.split(" to ")
            findin_first = re.search(r"(.+) (AM|PM)", first_hr)
            findin_second = re.search(r"(.+) (AM|PM)", second_hr)
            hr1 = findin_first.group(1)
            hr2 = findin_second.group(1)
    except ValueError:
        raise ValueError
    except AttributeError:
        raise ValueError

    try:

        hr1, min = int(hr1), int(min)
        validTime(hr1, min)
        hr2, min2 = int(hr2), int(min2)
        validTime(hr2, min2)

        if (findin_first.group(2) == "PM" and hr1 != 12) or (findin_first.group(2) == "AM" and hr1 == 12):
            if hr1 < 13:
                hr1 = hr1 + 12
            if hr1 == 24:
                hr1 = 00

        if (findin_second.group(2) == "PM" and hr2 != 12) or (findin_second.group(2) == "AM" and hr2 == 12):
            if hr2 < 13:
                hr2 = hr2 + 12
            if hr2 == 24:
                hr2 = 00
    except ValueError:
        raise ValueError

    return f"{hr1:02d}:{min:02d} to {hr2:02d}:{min2:02d}"


def validTime(hour, min):
    if 12 < hour:
        raise ValueError
    if 59 < min:
        raise ValueError
    return True


if __name__ == "__main__":
    main()
