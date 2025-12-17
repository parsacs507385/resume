from pyfiglet import Figlet, FontNotFound
import sys

font = ""
if len(sys.argv) == 1:
    font = "slant"
elif sys.argv[1] == "-f" or sys.argv[1] == "--font":
    try:
        font = sys.argv[2]
    except IndexError:
        sys.exit("Please Input A Font")
else:
    sys.exit("Invalid usage")
try:
    f = Figlet(font=font)
except FontNotFound:
    sys.exit("Please Input A Valid Font")


inp = input("Input: ").strip()
print(f.renderText(inp))
