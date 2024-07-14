import sys
import pyfiglet
import random

figlet = pyfiglet.Figlet()

num_arguments = len(sys.argv) - 1

if  num_arguments == 0:
    font_list = figlet.getFonts()
    figlet.setFont(font=random.choice(font_list))
elif num_arguments == 2:
    flag = sys.argv[1]

    if not (flag == "-f" or flag == "--font"):
        sys.exit("Invalid usage")

    try:
        figlet.setFont(font=sys.argv[2])
    except pyfiglet.FontNotFound:
        sys.exit("Invalid usage")

else:
    sys.exit("Invalid usage")

prompt = input("Input: ")
print("Output:")
print(figlet.renderText(prompt))
