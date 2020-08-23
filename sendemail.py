import smtplib
import requests
import json

conn = smtplib.SMTP("smtp.gmail.com", 587)

# Start connection
conn.ehlo()
conn.starttls()

# Get a random fact
response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
fact = json.loads(response.content)["text"]

# Read credentials from file
with open("sendemail_credentials", "r") as f:
    credentials = f.read().split("\n")
    sender_gmail_email = credentials[0]
    sender_gmail_password = credentials[1]
    receiver_email = credentials[2]

# Login
conn.login(sender_gmail_email, sender_gmail_password)

# Send email
conn.sendmail(sender_gmail_email, receiver_email, "Subject: Hello there!\n\nA random fact for you: {}".format(fact))

# End connection
conn.quit()

