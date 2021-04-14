import os
import subprocess

def _test():
    choice = input("Enter your choice\n1 --> for ipconfig\n2 --> for system IP\nq --> to quit\n")
    if choice=='q':
        exit(0)
    else:
        while True:
            try:
                c = int(choice)
                if c==1 or c==2:
                    execute(c)
                    break
                else:
                    raise NameError
            except NameError:
                print("Nah, Please choose 1 or 2 or q. Try, it's very simple")
                break
            except ValueError:
                print("omg! No please, Bruh! Choose 1 or 2 or q to exit")
                break
    _test()

def execute(choice, cmd='ipconfig'):
        if choice == 1:
            os.system(cmd)
        elif choice == 2:
            e = subprocess.Popen(cmd, stdout=subprocess.PIPE)
            handle = e.stdout.readlines()
            for line in handle:
                if "IPv4" in str(line):
                    l = str(line).split(":")
                    print("Your system IP is:", l[-1].replace('\\r\\n', ''))
            print("Executed using Subprocess.Popen\n", "The End".center(20,'*'))
            return 0

if __name__ == "__main__":
    _test()
