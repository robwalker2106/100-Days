import smtplib
import datetime as dt
from random import choice

my_email = "rob100python@yahoo.com"
password = 'bocchmlhwyeprhsw'
to_addrs = 'rob100python@gmail.com'

now = dt.datetime.now()

if now.weekday() == 1:
    with open('quotes.txt') as data:
        lines = data.readlines()
        quote = choice(lines)

    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=to_addrs, msg=f"Subject: Today's Quote\n\n{quote}")
    print('email sent')
