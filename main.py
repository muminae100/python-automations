#http requests
from urllib import response
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

#extracting Hacker News Stories
def extract_news(url):
    print('Extracting Hacker News Stories')
    cnt = ''
    cnt += ('<b>HN Top Stories:</b>\n' + '<br>' + '-'*50+'<br>')
    response = requests.get(url)
    content = response.content
    soup  = BeautifulSoup(content, 'html.parser')
    for i,tag in enumerate(soup.find_all('td', attrs={'class':'title','valign':''})):
        cnt += ((str(i+1)+' :: '+ tag.text + "\n" + '<br>') if tag.text != 'More' else '')
    return (cnt)

cnt = extract_news('https://news.vcombinator.com/')
content += cnt
content += ('<br>-------<br>')
content += ('<br><br>End of Message')

