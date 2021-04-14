def stat(port):
    file = r"C:\Users\ruban.kumar\Desktop\Python\Python\switch.txt"
    if int(port) <= 10:
        p = "port" + str(port)
        with open(file, "r") as fh:
            for line in fh:
                if p in line:
                    if "UP" in line:
                        print('port %s is up' % port)
                        break
                    else:
                        print('port %s is down' % port)
                        break
    else:
        print("Invalid port number entered\nAvailable ports -> 1 to 10")

def main():
    port = input("Enter a port number to check status\n")
    stat(port)


if __name__ == "__main__":
    main()