import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# smtp server
server = smtplib.SMTP("smtp.gmail.com", 25)
server.ehlo()

# import password from password.txt file
with open('password.txt', 'r') as f:
    password = f.read()

# login to a smtp server with email and password
server.login('mailtesting@gmail.com', password)

# parts of email
msg = MIMEMultipart()
msg['FROM'] = "Rale"
msg['TO'] = "radosrale@gmail.com"
msg['Subject'] = "Just a test mailng server"

# message from txt file which we need to send
with open('message.txt', 'r') as f:
    message = f.read()

# set attachment of email
msg.attach(MIMEText(message, 'plain'))

# importing picture
filename = "picture.jpg"
attachment = open(filename, 'rb')

# creating payload object
p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()

server.sendmail('mailtesting@gmail.com', 'radosrale@gmail.com', text)
