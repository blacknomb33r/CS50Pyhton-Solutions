from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
lst = ["-f", "--font"]
fontList = figlet.getFonts()
#print(fontList)

s = sys.argv

if len(s) >= 2:
    font = s[2]
    if s[1] in lst and s[2] in fontList:
        user = input("Input: ")
        output = Figlet(font=font)
        print(output.renderText(user))
    else:
         sys.exit("Invalid usage")

elif len(s) < 2:
        user = input("Input: ")
        font = random.choice(fontList)
        output = Figlet(font=font)
        print(output.renderText(user))
else:
    sys.exit("Invalid usage")
