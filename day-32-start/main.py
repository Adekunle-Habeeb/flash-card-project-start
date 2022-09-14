# import smtplib
#
# my_email = "bnaqeel@yahoo.com"
# password = "t9T9559U@n"
#
#
# connection = smtplib.SMTP("smtp.mail.yahoo.com")
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs="bnaqeel6@gmail.com", msg="Hello")
# connection.close()

import datetime as dt
import random


now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
