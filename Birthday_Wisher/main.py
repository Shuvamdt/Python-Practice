##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas as pd
import random
import smtplib

my_email = "shuvamdt1230@gmail.com"
password = "gnvsowrqgibgsaeg"

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
bDay_csv = pd.read_csv("./birthdays.csv")

bDay_dict = bDay_csv.to_dict(orient="records")
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
for row in bDay_dict:
    if row["month"] == now.month and row["day"] == now.day :
        with open(f"./letter_templates/letter_{random.randint(1,3)}.txt") as letter_file:
            letter = letter_file.read()
            letter = letter.replace("[NAME]", row["name"])
# 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com", port=587) as conn:
            conn.starttls()
            conn.login(user=my_email, password=password)
            conn.sendmail(from_addr=my_email, to_addrs=row["email"], msg= f"Subject: Happy Birthday {row['name']}\n\n{letter}")




