import csv
def wr(content, csv_file):
    """
    We are trying to write some content to a CSV file using writer and DictWriter methods.
    Lets get started
    :param csv_file:
    :return:
    """
    with open(csv_file, "wt") as file:
        writer = csv.writer(file, delimiter=",", newline=' ')
        for line in content:
            writer.writerow(line)
def re(csv_file):
    """
    Reading the CSV file we just created
    :param csvfile: 
    :return: 
    """
    with open(csv_file, "r") as content:
        read = csv.reader(content)
        for row in read:
            print(" ".join(row))
if __name__ == "__main__":
    print("Enter number of row\n")
    r = int(input())
    data = []
    for i in range(r):
        s = input()
        data.append(s.split())
print("Enter file name without any extensions\n")
name = str(input())
wd=r"C:\Users\ruban.kumar\Downloads\\"
path = wd + name + ".csv"
wr(data, path)
re(path)