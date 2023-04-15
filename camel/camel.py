user_input = input("camelCase: ")
print("snake_case: ", end="")
for i in user_input:
       if i.isupper():
              print("_" + i.lower(), end="")
       else:
              print(i, end="")

print("")