import datetime as dt
import pandas
import random
import smtplib
# #################### Project ######################
# use your email account and app password below
my_email = "youremail@gmail.com"
password = "add password"

# 1. Update the birthdays.csv with your friends & family's details. 

# 2. Check if today matches a birthday in the birthdays.csv
today = (dt.datetime.now().month, dt.datetime.now().day)

birthdays_csv = pandas.read_csv("birthdays.csv", index_col=False)
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in birthdays_csv.iterrows()}

# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and
if today in birthdays_dict:
    birthdays_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as file:
        content = file.read()
        email_content = content.replace("[NAME]", birthdays_person["name"])
# 4. Send the letter generated in step 3 to that person's email address. HINT 1: Gmail(smtp.gmail.com),
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="email_account@yahoo.com",
                                msg=f"Subject: Happy Birthday\n\n{email_content}")

