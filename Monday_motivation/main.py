import smtplib
import datetime as dt
import random

my_email = "shuvamdt1230@gmail.com"
password = "gnvsowrqgibgsaeg"

now = dt.datetime.now()
if now.weekday() == 1:
    with open("./quotes.txt") as file:
        quotes = file.read().split("\n")
        quote = random.choice(quotes)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="shuvamdtarcade@gmail.com",
                            msg=f"Subject:Monday quotes\n\n{quote}")