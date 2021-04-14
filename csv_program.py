import csv
def csv_reader(csv_file):
    """
    readng a CSV file and Printing its content
    :param csv_file: .csv file
    :return: File content
    """
    file = csv.reader(csv_file)
    for row in file:
       print(" ".join(row))
def csv_dictreader(csv_file,s):
    file = csv.DictReader(csv_file, delimiter = ",")
    for line in file:
        print(line[s])
if __name__ == "__main__":
    with open(r"C:\Users\ruban.kumar\Downloads\csv_sample.csv", "r") as csv_file:
        print("Enter your option\n1. Use Reader method\n2. Use DictReader method")
        c = int(input())
        if c == 1:
            csv_reader(csv_file)
        elif c == 2:
            print("Enter String\n")
            s = input()
            csv_dictreader(csv_file,s)
        else:
            print("Invalid option selected, Please correct")
