import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# from email.MIMEMultipart import MIMEMultipart
# from email.MIMEText import MIMEText


fromaddr = 'xgen.osama@gmail.com'
toaddr = 'xgen.osama@gmail.com'
text = 'text message sent from python'
username = 'xgenOsama'
password = '###############'

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'Text'
msg.attach(MIMEText(text))
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.ehlo()
server.login(username, password)
server.sendmail(fromaddr, toaddr, msg.as_string())
server.quit()
