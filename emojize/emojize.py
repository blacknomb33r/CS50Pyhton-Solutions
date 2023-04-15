import emoji

user = input(": ").replace(" ", ":")
print("Hello, ", emoji.emojize(user), sep="")