import sys
from PIL import Image
from PIL import ImageOps

def main():
    if len(sys.argv[1:]) != 2:
        sys.exit("Incorrect number of command-line arguments")

    input, output = sys.argv[1:]

    try:
        _, _, input_extension = input.partition(".")
    except ValueError:
        sys.exit("Input file extension must be .jpg, .jpeg, or .png")

    try:
        _, _, output_extension = output.partition(".")
    except ValueError:
        sys.exit("Output file extension must be .jpg, .jpeg, or .png")

    valid_extensions = ["jpg", "jpeg", "png"]
    for extension in [input_extension, output_extension]:
        if not (extension.lower() in valid_extensions):
            sys.exit(f"Input and output file extensions must be one of the following: {valid_extensions}")

    if input_extension.lower() != output_extension.lower():
        sys.exit("Input and Output files must have the same extension")

    # Get size from shirt.png
    shirt = Image.open("shirt.png")

    # Open the input with Image.open, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.open
    try:
        photo = Image.open(input, formats=["JPEG", "PNG"])
    except FileNotFoundError:
        sys.exit(f"Input file not found: {input}")

    # resize and crop the input with ImageOps.fit, per pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.fit,
    #   using default values for method, bleed, and centering
    photo = ImageOps.fit(photo, shirt.size)

    # overlay the shirt with Image.paste, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.paste
    photo.paste(shirt, shirt)

    # save the result with Image.save, per pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.Image.save.
    photo.save(output)

if __name__ == "__main__":
    main()
