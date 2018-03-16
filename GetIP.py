import os
import subprocess

def _test(cmd="ipconfig"):
    while True:
        choice = raw_input("Enter your choice to check system IP\nPress 1 for os.system\nPress 2 for subprocess\nPress 3 to quit\n")
        try:
            if int(choice) == 1:
                os.system(cmd)
                print("Exectuted using os.sytem")
                return 0
            elif int(choice) == 2:
                e = subprocess.Popen(cmd, stdout=subprocess.PIPE)
                handle = e.stdout.readlines()
                for line in handle:
                    if "IPv4" in line:
                        l = line.split(":")
                        print "Your system IP is:", l[1]
                print "Executed using Subprocess.Popen"
                return 0
            elif int(choice) == 3:
                continue
        except NameError, ValueError:
            print "Input only numbers"


if __name__ == "__main__":
    _test()
