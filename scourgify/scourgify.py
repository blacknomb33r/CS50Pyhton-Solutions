import sys
import csv

def main():
    user = sys.argv
    if len(user) > 3:
        sys.exit("Too many command-line arguments")
    elif len(user) <= 1:
        sys.exit("Too few command-line arguments")
    elif not user[1].endswith(".csv"):
        sys.exit("Not CSV File")
    else:
        readWriteFile(user[1], user[2])

 


def readWriteFile(input, output):
    try:
        #empty list
        students = []
        #open "first File" from CLI as f
        with open(input) as input: 
            #use csv dictreader and clear data
            reader = csv.DictReader(input)
            for line in reader:
                #last, first = split to the two variables the last and first name from line[name]
                last, first = line["name"].split(", ")
                #house to house var
                house = line["house"]
                #create a dic for every student in order (Firstname, Lastname, House)
                student = {"first": first, "last": last, "house": house}
                #append every single student to empty list from the beginning
                students.append(student)
            #sort list with key = lambda x: x[Firstname] -> sort ascend key firstname
            sorted_list = sorted(students, key=lambda x: x['first'])
            #open second file (in that moment after.csv will be created in dir)
            with open(output, "w") as output:
                #create first row
                header = ["first", "last", "house"]
                writer = csv.DictWriter(output, fieldnames = header)
                writer.writeheader()
                #looping through our sorted list to write in exact order to the file
                for student in sorted_list:
                    #write in correct (alphabetical order) the Firstname, Lastname, house (
                    writer.writerow({"first": student['first'], "last": student['last'], "house": student['house']})
                
    except FileNotFoundError:
        sys.exit(f"Could not read {input}")


if __name__ == "__main__":
    main()