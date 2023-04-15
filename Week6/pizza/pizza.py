import sys
from tabulate import tabulate

def main():
    file = userInput()
    pizza = fileReading(file)
    createTable(pizza)
    
       

def createTable(pizza):
        print(tabulate(pizza, headers="firstrow", tablefmt="grid"))
        


def fileReading(file):
    try:
        #create a empty list, later: for the dict per line in a list
        pizzas = []
        with open(userInput()) as file:
            for line in file:
                pizza, small, large = line.rstrip().split(",")
                #create a dic for the splited lines from csv file
                dic = {"pizza": pizza, "small": small, "large": large,}
                #append dic to list (for every line there is a dic)
                pizzas.append(dic)
        return pizzas
    
    except FileNotFoundError:
        sys.exit("File does not exist")

def userInput():
        user_input = sys.argv
        if len(user_input) <= 0:
            sys.exit("Too few command-line arguments")
        elif len(user_input) != 2:
            sys.exit("Too many command-line arguments")
        elif not (user_input[1].endswith(".csv")):
            sys.exit("Not a csv File")
        else:
            return user_input[1]
        


if __name__ == "__main__":
    main()