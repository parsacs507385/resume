import sys
from PIL import Image, ImageOps

def main():
    if len(sys.argv) == 3 and ((sys.argv[1][-4:] == ".png" and sys.argv[2][-4:] == ".png") or sys.argv[1][-4:] == ".jpg" and sys.argv[2][-4:] == ".jpg"):
        try:
            image = Image.open(sys.argv[1])
            shirt = Image.open("shirt.png")
            image = ImageOps.fit(image, shirt.size)
            image.paste(shirt, (0, 0), shirt)
            image.save(sys.argv[2])


        except Exception as e:
            sys.exit(f"ERR: {e}")

    else:
        sys.exit("Invalid Args")

    sys.exit(0)

if __name__ == "__main__":
    main()
