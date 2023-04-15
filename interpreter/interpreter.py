user_input = input("Expression: ")

x, y, z = user_input.split(" ")


if y == "+":
    res = int(x) + int(z)
elif y == "-":
    res = int(x) - int(z)
elif y == "*":
    res = int(x) * int(z)
else:
    res = int(x) / int(z)

print(f"{res:.1f}")
