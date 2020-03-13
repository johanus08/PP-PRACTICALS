#!/usr/bin/python3

import smtplib
import getpass

content='hello,sending mail from python code'
mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()

passwd = getpass.getpass()

mail.login('sender@gmail.com',passwd)
mail.sendmail('sender@gmail.com','receiver@gmail.com',content)

mail.close()
