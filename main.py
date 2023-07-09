import smtplib
import pandas
import random
from datetime import datetime

today = datetime.now()
today_tuple = (today.month, today.day)
my_email = "YOUR EMAIL"
pwd = "YOUR PASSWORD"

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthdays_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthdays_person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=pwd)
        connection.sendmail(
            to_addrs=birthdays_person["email"],
            from_addr=my_email,
            msg=f"Subject:HAPPY BIRTHDAY\n\n{contents}"
        )

    print("Birthday email sent")
