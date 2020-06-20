def Takescreenshot_sendemail():
  """This function greets to the person passed in asa parameter"""    

import smtplib
import ssl
import pyautogui
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

strFrom = 'bnbishar@gmail.com'
strTo = 'bisharbn@nrl.ae,sajina.jml@gmail.com'
pyautogui.screenshot("c:\\data\\screen.png")

# Create the root message and fill in the from, to, and subject headers
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'Screenshot associated to this email'
msgRoot['From'] = strFrom
msgRoot['To'] = strTo
msgRoot.preamble = 'This is a multi-part message in MIME format.'

# Encapsulate the plain and HTML versions of the message body in an
# 'alternative' part, so message agents can decide which they want to display.
msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

msgText = MIMEText('This is the alternative plain text message.')
msgAlternative.attach(msgText)

# We reference the image in the IMG SRC attribute by the ID we give it below
msgText = MIMEText('<b>Some <i>HTML</i> text</b> and an image.<br><img src="cid:image1"><br>', 'html')
msgAlternative.attach(msgText)

# This example assumes the image is in the current directory
fp = open('c:\\data\\screen.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# Define the image's ID as referenced above
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)



smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "bnbishar@gmail.com"
password = "Bishar{123"#input("Type your password and press enter: ")""
receiver_email = "bisharbn@nrl.ae"
#message = "Test email from python"

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msgRoot.as_string())
    server.quit() 
except Exception as e:
    # Print any error messages to stdout
    print(e)


def Takescreenshot():
      """This function greets to the person passed in asa parameter"""    

import pyautogui
pyautogui.screenshot("C:\\Data\\video\\screen.png")

