import ftplib
import sys

connect = ftplib.FTP('www.ualr.edu')
connect.login('facstaff\mmmcmillan','meredith26')
data = []
connect.dir(data.append)

connect.close()

for line in data:
    print line
