from bs4 import BeautifulSoup
import requests
import pandas as pd
import smtplib
from email.message import EmailMessage

URL = 'Website URL'

responce = requests.get(URL)

soup = BeautifulSoup(responce.text)


def Announcesment_news():

    Announces = soup.find_all('h6')
    Announces_titles = [title.get_text() for title in Announces]
    ALL_URLS = [url.a['href'] for url in Announces if url.a]

    for _ in zip(Announces_titles, ALL_URLS): 
        body_msg = f'New Annonce: {Announces_titles[0]}\nCheck it Now: {ALL_URLS[0]}'
        email_alert("Mr. Aziz FSA-AM New Announcement! 😊", body_msg, "messageto_who@gmail.com")#email that send msg to
        break

def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg['subject'] = subject
    msg['to'] = to

    user = "youremail@gmail.com" #email that send msg from
    msg['from'] = user
    email_pss = "Email_AppKey"

    # Initialize the server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, email_pss)
    server.send_message(msg)
    server.quit()

if __name__ == '__main__':
    Announcesment_news()