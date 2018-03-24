#!/usr/bin/env python3
'''
This program will generate an email using your email of choice.
'''
from email.mime.text import MIMEText
import getpass
import smtplib
import sys


def main ():
    smtp_server, smtp_port, smtp_account, smtp_password, email_subject, email_destination = gather_info()
    send_email(smtp_server, smtp_port, smtp_account, smtp_password, email_subject, email_destination)


def gather_info():
    # Gather information for the email
    try:
        smtp_server = input("\nProvide the SMTP Server: ")
        smtp_port = input("Provide the SMTP port: ")
        smtp_account = input("Provide email account for SMTP Server: ")
        smtp_password = getpass.getpass("Enter password for SMTP Server: ")
        email_subject = input("Provide email subject: ")
        email_destination = input("Provide destination emails separated by ',': ")
        return smtp_server, smtp_port, smtp_account, smtp_password, email_subject, email_destination
    except KeyboardInterrupt:
        print("\nEmailer exited by user action.  Email will not be sent")
        sys.exit()


def send_email(smtp_server, smtp_port, smtp_account, smtp_password, email_subject, email_destination):
    # Create email using information provided, and attempt to send.
    email_from = "{}".format(smtp_account)
    email_to = "{}".format(email_destination)
    email_subject = "{}".format(email_subject)

    # Import message text and append from, to, subject
    msg = MIMEText("This is a templated email!")
    msg["From"] = email_from
    msg["To"] = email_to
    msg["Subject"] = email_subject


    # Send the email
    try:
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.ehlo()
        server.login(smtp_account, smtp_password)
        server.sendmail(email_from, email_to.split(","), msg.as_string())
        server.close()
        print("Email Sent Successfully.")
    except Exception as e:
        print("***** EMAIL SEND FAILURE ***** - {}".format(e))


if __name__ == '__main__':
    main()