import yagmail
import pandas
from news import NewsFeed
import datetime
import time

while True:
    if datetime.datetime.now().hour == 17 and datetime.datetime.now().minute == 51:
        df = pandas.read_excel('people.xlsx')
        for index, row in df.iterrows():
            
            today = datetime.datetime.now().strftime('%Y-%m-%d')
            yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
            
            news_feed = NewsFeed(row['interest'], from_date=yesterday, to_date=today)
            
            email = yagmail.SMTP(user="alamgir500hossain@gmail.com", password="")
            email.send(to=row['email'],
                    subject=f"Hi {row['interest']} news for today",
                    contents=f"Hi, {row['name']} see whats' on about {row['interest']}. Today. {news_feed.get()} \nArdit",
                    attachments="design.txt")  
        
    time.sleep(60)