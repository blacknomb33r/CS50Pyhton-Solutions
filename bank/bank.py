user_input = input("Greeting: ").lower().strip()

if user_input.startswith("hello"):
    print("$0")
elif user_input.startswith("h") and not user_input.startswith("hello"):
    print("$20")
else:
    print("$100")