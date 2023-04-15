

from random import randrange

while True:
    try:
        user_lvl = int(input("Level: "))
        choice = randrange(1, user_lvl)
        while True:
            # Prompt the user for the second input
            guess = input("Guess: ")
            guess = int(guess)
            if guess > choice:
                    print("Too large!")
                    break
            elif guess < choice:
                    print("Too small!")
                    break
            elif guess == choice:
                    print("Just right!")
                    raise EOFError
    except ValueError:
        pass
    except EOFError:
        break

    
