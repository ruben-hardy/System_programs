import smtplib
def mail(srv, f, t, s, b):
    BODY = "\r\n".join((
        "From: %s" % f,
        "To: %s" % t,
        "Subject: %s" % s,
        "", b
    ))
username = "rubansoftengg@gmail.com"
password = "Sowmiy@2379"
server = smtplib.SMTP(srv)
server.login(username, password)
server.sendmail(FROM, [TO], BODY)
server.quit()
if __name__ = "__main__":
    srv = "smtp.gmail.com"
    f = "rubansoftengg@gmail.com"
    t = "rubenhardy.ca@gmail.com"
    s = "This is a test"
    b = "Hello!! How are you doing today"
    mail(srv, f, t, s, b)
