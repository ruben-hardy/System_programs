def Lst(c):
    if c == 1:
        print(l)
    elif c == 2:
        l = []
        k = int(input("Enter number of value to be added to the list"))
        print("Enter value one by one")
        for i in range(k):
            v = input()
            l.append(v)
        print(l)
    elif c == 3:
        d = input("Enter value to be deleted\n")
        del l[d]
        print(l)
    elif c == 4:
        l.clear()
        print("List cleared")
        print(l)
    else:
        print("Invalid Choice!!!")
while True:
    c = int(input("Choose from the menu\n1. View the list\n2. Add a value to list\n3. Remove an item from list\n4. clear list\n\n"))
    Lst(c)
    ret = str(input("Press Y to return"))
    if ret != 'Y':
        break