#http requests
import requests
#web scraping
from bs4 import BeautifulSoup
#send mail
import smtplib
#email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#System date and time
import datetime
now = datetime.datetime.now()

#email content placeholder
content = ''
