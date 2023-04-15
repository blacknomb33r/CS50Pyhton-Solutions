def main():
    word = input("input: ")
    print(shorten(word))


def shorten(word):
    short = ""
    v = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for i in word:
        for j in i:
            if j in v:
                short = short + i.replace(j, "")
            else:
                short = short + j
    return short

if __name__ == "__main__":
    main()