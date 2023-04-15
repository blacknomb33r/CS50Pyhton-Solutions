#print(input("Input: ").translate({ord(letter): None for letter in 'AEIOUaeiou'}))


u = input("Input: ")
v = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
print("Output: ", end="")
for i in u:
    for j in i:
        if j in v:
            print(i.replace(j, ""), end="")
        else:
            print(j, end="")
print("")
