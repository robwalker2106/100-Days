import datetime as dt
import smtplib
from random import randint
import pandas as pd

my_email = "rob100python@yahoo.com"
password = 'bocchmlhwyeprhsw'

birthdays_df = pd.read_csv('birthdays.csv')
today = dt.datetime.now()
todays_birthday = birthdays_df[(birthdays_df.month == today.month) & (birthdays_df.day == today.day)]

for index, row in todays_birthday.iterrows():
    letter = './letter_templates/letter_' + str(randint(1, 3)) + ".txt"

    with open(letter) as file:
        letter_tmpl = file.read()
        letter_tmpl = letter_tmpl.replace("[NAME]", row['name'])

    with smtplib.SMTP('smtp.mail.yahoo.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=row['email'],
                            msg=f'Subject: Happy Birthday\n\n{letter_tmpl}')
    print(f'Email sent to {row["name"]}')





