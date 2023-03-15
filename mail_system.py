import smtplib
import datetime as dt
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


user_mail = 'yourmailid@goeshere.com'
passcode = 'yourapppasscode'
recipient = 'receivingmailid@goeshere.com'
today = dt.date.today()
sub = f'Job Listings {today.strftime("%d")}th {today.strftime("%b")}'


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
