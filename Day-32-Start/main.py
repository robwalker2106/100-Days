import smtplib
import datetime as dt
from random import choice

my_email = "robwalker8280@gmail.com"
password = '$xr%M4Z99@A6'
to_addrs = 'robwalker2106@gmail.com'
to_sarai = 'saraigomezco18@gmail.com'

now = dt.datetime.now()

if now.weekday() == 1:
    with open('quotes.txt') as data:
        lines = data.readlines()
        quote = choice(lines)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_addrs,
                            msg=f"Subject: Papi's Quote of the Day\n\n{quote}")
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_sarai,
                            msg=f"Subject: Today's Quote\n\n{quote}\nBrought to you by Papi's programming studies.")

