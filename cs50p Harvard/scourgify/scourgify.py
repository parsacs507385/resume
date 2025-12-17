import sys
import csv
students = []

def main():
    if len(sys.argv) == 3:
        if sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
            try:
                with open(sys.argv[1]) as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        students.append(row)

                with open(sys.argv[2], "w") as file:
                    writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
                    writer.writeheader()
                    for student in students:
                        last, first = student["name"].split(", ")
                        writer.writerow({"first": first, "last": last, "house": student["house"]})
            except FileNotFoundError:
                sys.exit("No Such A File")
        else:
            sys.exit("Please Input A CSV File")
    else:
        sys.exit("Invalid Args")


if __name__ == "__main__":
    main()













# import sys
# import csv
# first = ""
# last = ""
# house = ""

# if len(sys.argv) == 3:
#     beforeArg = sys.argv[1]
#     afterArg = sys.argv[2]
#     if not (beforeArg[-4:] == ".csv"):
#         sys.exit("Please Input A CSV File")
#     if not (afterArg[-4:] == ".csv"):
#         sys.exit("Please Input A CSV File")

#     try:
#         with open(beforeArg, "r") as beforeCsv:
#             with open(afterArg, "w") as afterCsv:
#                 beforeCsvReader = csv.DictReader(beforeCsv)
#                 afterCsvWriter = csv.writer(afterCsv)

#                 for line in beforeCsvReader:
#                     first, last = line["name"].split(",")
#                     house = line["house"]
#                     afterCsvWriter.writerow([first, last, house])

#     except Exception as e:
#         sys.exit(e)

# else:
#     sys.exit("Invalid Args")
