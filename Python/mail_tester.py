import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.login('rexina0007@gmail.com','xxxxxxx')
server.sendmail('rexina0007@gmail.com','subhamkundu486@gmail.com','Subject: My subject \n\nDear subham,\n I am test my email through python.\n\n-Rex')
server.close()