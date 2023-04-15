import sys


def main():
    try:
        checkUserInput()
        output()
    except FileNotFoundError:
        sys.exit("File does not exist")
    

def output():
    user_input = checkUserInput()   
    print(f"{countLines(user_input)}")

def checkUserInput():
    user_input = sys.argv
    if len(user_input) == 1:
        sys.exit("too few command-line arguments")
    elif len(user_input) > 2:
        sys.exit("too many command-line arguments")
    elif user_input[1].endswith(".py"):
        return user_input
    else: 
        sys.exit("Not a Python file")
        

def countLines(user_input):
    count = 0
    with open (user_input[1]) as file:
        for i in file:
            if not (i.lstrip().startswith("#") or i.strip() == ""):
               count +=1
    return count

if __name__ == "__main__":
    main()
