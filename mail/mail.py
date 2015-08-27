import smtplib,os,imaplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def send():
    fromaddr = raw_input('Enter your Email Address : ')
    toaddr = raw_input("Enter the receiver's Email Address : ")
    subject = raw_input('Enter the subject : ')
    text = raw_input('Enter the message :')
    username = raw_input('Enter your username : ')
    password = raw_input('Enter your password : ')

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject
    msg.attach(MIMEText(text))
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username, password)
    server.sendmail(fromaddr, toaddr, msg.as_string())
    server.quit()
    print("Email sent successfully")
    choice = raw_input('Enter x to clear screen: ')
    if choice == 'x':
        os.system('cls')


def read():
    mailServer = imaplib.IMAP4_SSL('imap.gmail.com', 993)
    username = raw_input('Enter your username:')
    password = raw_input('Enter your password:')
    mailServer.login(str(username), str(password))
    status, count = mailServer.select('Inbox')
    status, data = mailServer.fetch(count[0], '(UID BODY[TEXT])')
    print(data[0][1])
    mailServer.close()
    mailServer.logout()
    choice = raw_input('Enter x to clear screen: ')
    if choice == 'x':
        os.system('cls')

while 1:
    os.system('cls')
    print('Email program :')
    print('')
    print("1. read email")
    print("2. send email")
    print("3. Exit")
    choice = raw_input('Enter your choice : ')
    if choice == '1':
        read()
    elif choice == '2':
        send()
    else:
        break



