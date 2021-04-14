import datetime
import sys
def TimeCal(inHour, inMinutes):
    Ctime = datetime.datetime.today()
    LoginTime = datetime.datetime(Ctime.year, Ctime.month, Ctime.day, inHour, inMinutes, Ctime.second)
    print("Login Time: %s" % LoginTime.strftime("%Y-%m-%d   %H:%M:%S"))
    print("Logout Time: %s" % Ctime.strftime("%Y-%m-%d   %H:%M:%S"))
    delta = Ctime - LoginTime
    type(delta)
    print("Total time in office: %s" % delta)
    a = inHour * 60
    t = a + inMinutes
    s = int(Ctime.hour) * 60
    p = int(Ctime.minute) + s
    total = p - t
    rem = 480 - total
    rh = rem // 60
    rm = rem % 60
    print("Remaining %s hours and %s minutes" % (rh,rm))
if __name__ == "__main__":
    option = sys.argv
    inHour = int(option[1])
    inMinutes = int(option[2])
    #print("Enter login time in 24 hours format")
    #inHour=int(input("Enter Hours:"))
    #inMinutes=int(input("Enter Minutes:"))
    TimeCal(inHour, inMinutes)

