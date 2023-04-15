import inflect
import sys
result = []
p = inflect.engine()

while True:
    try:
        u = input("Name: ")
        result.append(u)

    except EOFError:
        break
myList = p.join((result))
print("\nAdieu, adieu, to", myList)