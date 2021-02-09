import smtplib

my_email = "rob100python@yahoo.com"
password = 'bocchmlhwyeprhsw'
to_addrs = 'rob100python@gmail.com'

with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=to_addrs, msg="Subject:Hello Test\n\nTesting")
