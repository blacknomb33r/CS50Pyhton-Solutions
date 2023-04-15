import sys
from PIL import Image, ImageOps
import os


def main():
    end = (".jpg", ".jpeg", ".png")
    if len(sys.argv) <= 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 4:
        sys.exit("Too many command-line arguments")
    elif (os.path.splitext(sys.argv[1])[1]) != (os.path.splitext(sys.argv[2])[1]):
        sys.exit("Input and output have different extensions")
    elif (os.path.splitext(sys.argv[1])[1]) or (os.path.splitext(sys.argv[2])[1]) in end:
        processImage(sys.argv[1], sys.argv[2])
    else:
        sys.exit("Invalid Input")


def processImage(input, output):
    try:
        shirt = Image.open("shirt.png")
        with Image.open(input) as input:
            input_cropped = ImageOps.fit(input, shirt.size)
            input_cropped.paste(shirt, mask = shirt)
            input_cropped.save(output)
    except FileNotFoundError:
        sys.exit(f"Input does not exist")
    


if __name__ == "__main__":
    main()