__author__ = 'XGen'
import imaplib

mailServer = imaplib.IMAP4_SSL('imap.gmail.com', 993)
username = 'xgenosama'
password = '#############'
mailServer.login(username, password)
status, count = mailServer.select('Inbox')
status, data = mailServer.fetch(count[0], '(UID BODY[TEXT])')

print(data[0][1].split('</div>')[0].split('>')[1])

mailServer.close()

mailServer.logout()
