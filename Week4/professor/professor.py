import random
import sys

def main():
    score = 0
    rounds = 10
    trys = 0
    level = int(get_level())
    while rounds != 0:
        x, y = generate_integer(level) 
        while True:
            print(x, "+", y, "=", end="")
            try:
                mathP_user = int(input(" "))
            except ValueError:
                continue
            mathP_com = x + y
            try:
                if mathP_com == mathP_user:
                    score += 1
                    trys = 0
                    break
                elif mathP_com != mathP_user and trys < 2:
                    print("EEE")
                    trys += 1
                    continue
                elif mathP_com != mathP_user and trys == 2:
                    raise ValueError
            except ValueError:
                print("The correct answer is:", mathP_com)
                break    
        rounds -= 1
    print(score)
    sys.exit(0)

    
    
def get_level():
    while True:
        try:
            n = int(input("Level: "))
        except ValueError:
            pass
        else:
            if n in (1, 2, 3):
                break
    return n       

def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10 ,99)
    elif level == 3:     
        x = random.randint(100, 999)
        y = random.randint(100 ,999)
    return x, y
    

if __name__ == "__main__":
    main()

# bug trys counter will not be reseted
