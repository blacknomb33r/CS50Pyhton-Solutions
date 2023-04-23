from datetime import date, timedelta
import sys
import re
import inflect


def main():
    birthday = input("Date of Birth: ")
    #use regular expressions to validate the correct date #1995-05-01 (groups) are for later use
    regex = re.compile(r"^((?:19|20)\d{2})\-(1[012]|0?[1-9])\-(3[01]|[12][0-9]|0?[1-9])$")
    if match := regex.search(birthday):
        #convert input to date object 
        birthday = date(int(match.group(1)), int(match.group(2)), int(match.group(3)))
        print(numToWord(convert(birthday)))
    else:
        sys.exit("Invalid Date")
    
def convert(birthday):
    today = date.today()
    #convert total seconds to days -> today - birthday is a timedelta object (you can't convert it easy to int; Solution is totalsecond to days)
    days = int(timedelta.total_seconds(today - birthday) / 86400)
    return days

def numToWord(days):
    inf = inflect.engine()
    #convert days to minutes
    mins = days * 1440
    words = inf.number_to_words(mins, andword='')
    #return f-string
    return f"{words.capitalize()} minutes"


if __name__ == "__main__":
    main()