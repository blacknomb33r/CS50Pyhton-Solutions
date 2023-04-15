user_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").replace("-", " ").lower().strip()

if user_input == "42":
    print("Yes")
elif user_input == "forty two":
    print("Yes")
else:
    print("No")
