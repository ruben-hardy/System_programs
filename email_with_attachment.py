import os
from configparser import ConfigParser
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.utils import formatdate
import smtplib
def Sendmail(to_addr, body_text, cc_emails, bcc_emails, file_to_attach):
    #Accessing the configuration file
    basepath = os.path.dirname(os.path.abspath(__file__))
    #print(__file__)
    filepath = os.path.join(basepath, "email.ini")
    header = ('Content-Disposition', 'attachment; filename="%s"' % file_to_attach)
    if os.path.exists(filepath):
        cfg = ConfigParser()
        cfg.read(filepath)
    else:
        print("Configuration file is not found!!!")
        sys.exit(1)
    server = cfg.get("server", "name")
    #print("mailbox: %s" % server)
    from_addr = cfg.get("server", "from")
    #Creating message
    msg = MIMEMultipart()
    msg["TO"] = ", ".join(to_addr)
    msg["Subject"] = "This is a test email"
    msg["CC"] = ", ".join(cc_emails)
    msg["BCC"] = ", ".join(bcc_emails)
    msg.attach(MIMEText(body_text))
    msg["DATE"] = formatdate(localtime=True)
    msg["FROM"] = from_addr

    attachment = MIMEBase('application', 'octet-stream')
    try:
        with open(file_to_attach, "rb") as fh:
            data = fh.read()
            attachment.set_payload(data)
            encoders.encode_base64(attachment)
            attachment.add_header(*header)
            msg.attach(attachment)
    except IOError:
        print("unable to read the file. Please check!!")
        sys.exit(1)
    emails = to_addr + cc_emails + bcc_emails
    host = smtplib.SMTP(server)
    host.login(user="rubansoftengg@gmail.com", password="*******")
    host.sendmail(from_addr, emails, msg.as_string())
    host.quit()

if __name__ == "__main__":
    to_addr = ["employee1@domain.com", "employee2@domain.com"]
    cc_emails = ["boss1@domain.com", "manager1@domain.com"]
    bcc_emails = ["admin@domain.com"]
    body_text = "This is a test email for a testing purpose"
    file_to_attach = r"C:\Users\ruban.kumar\Downloads\downloadC5857125830\lab.ovpn"
    Sendmail(to_addr, body_text, cc_emails, bcc_emails, file_to_attach)