def main():
    sch = [{"meal":"breakfast time", "sHour":7, "eHour":8},
           {"meal":"lunch time", "sHour":12, "eHour":13},
           {"meal":"dinner time", "sHour":18, "eHour":19},
    ]
    time = input("Hello: ")
    inp = float(convert(time))

    for d in sch:
        if float(d["sHour"]) <= inp <= float(d["eHour"]):
            print(d["meal"])
        else:
            continue

def convert(t):
    c = 0.0
    if t.rfind(" a.m.") != -1:
        t = t.replace(" a.m.", "")
    elif t.rfind(" p.m.") != -1:
        t = t.replace(" p.m.", "")
        c = 12.00

    h, m = t.strip().split(":")
    time = float(h) + c + (float(m)/60)
    return time

if __name__ == "__main__":
    main()











# def main():
#     firstInp = input("What time is it? ").strip().split(":")
#     inp = convert(firstInp)

#     if 7.0 <= inp <= 8.0:
#         print("breakfast time")
#     elif 12.0 <= inp <= 13.0:
#         print("lunch time")
#     elif 18.0 <= inp <= 19.0:
#         print("dinner time")


# def convert(time):
#     hour = time[0]
#     mins = time[1]
#     modifiedMins = (5*float(mins))/3
#     ans = ""
#     ans = ans + str(hour) + "." + str(int(modifiedMins))
#     return (float(ans))



# if __name__ == "__main__":
#     main()

