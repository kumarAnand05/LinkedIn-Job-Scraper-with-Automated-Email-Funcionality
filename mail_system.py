import smtplib
import datetime as dt
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def date_suffix(today):
    if 11 <= today <= 13:
        suffix = 'th'
    else:
        last_digit = today % 10
        if last_digit == 1:
            suffix = 'st'
        elif last_digit == 2:
            suffix = 'nd'
        elif last_digit == 3:
            suffix = 'rd'
        else:
            suffix = 'th'
    return f"{today}{suffix}"


user_mail = 'yourmailid@goeshere.com'
passcode = 'yourapppasscode'
recipient = 'receivingmailid@goeshere.com'
today = dt.date.today()
sub = f'Job Listings {date_suffix(int(today.strftime("%d")))} {today.strftime("%b")}'


def mail_sub(csv_file):
    msg = MIMEMultipart()
    msg['From'] = user_mail
    msg['To'] = recipient
    msg['Subject'] = sub
    attachment = MIMEApplication(csv_file, _subtype='csv')
    attachment.add_header('Content-Disposition', 'attachment', filename=f'{sub}.csv')
    msg.attach(attachment)
    domain = user_mail.strip().split('@')[-1]

    if domain == 'gmail.com':
        server = smtplib.SMTP('smtp.gmail.com', 587)
    elif domain == 'yahoo.com':
        server = smtplib.SMTP('smtp.mail.yahoo.com', 587)
    elif domain == 'outlook.com':
        server = smtplib.SMTP('smtp-mail.outlook.com', 587)

    server.starttls()
    server.login(user_mail, passcode)
    text = msg.as_string()
    server.sendmail(user_mail, recipient, text)
    server.quit()
