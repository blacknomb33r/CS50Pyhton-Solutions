def main():
    u = input("Greeting: ").lower().strip()
    print(f"${value(u)}")

def value(u):
    if u.startswith("hello"):
        return 0
    elif u.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()