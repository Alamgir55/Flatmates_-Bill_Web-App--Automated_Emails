# 975297128b834d3da8d7bd4dcb4eefc0

import requests
from pprint import pprint


class NewsFeed:
    base_url = "https://newsapi.org/v2/everything?"
    api_key = "975297128b834d3da8d7bd4dcb4eefc0"
     
    def __init__(self, interest, from_date, to_date, language='en'):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language
    
    def get(self):
        url = f"{self.base_url}" \
              f"qInTitle={self.interest}&" \
              f"from={self.from_date}&" \
              f"to={self.to_date}&" \
              f"language={self.language}&" \
              f"apiKey={self.api_key}"
            
        response = requests.get(url) 
        content = response.json()
        articles = content['articles']

        email_body = ''
        for article in articles:
            email_body = email_body + article['title'] + "\n" + article['url'] + "\n\n"
    
        return email_body
    
    
if __name__ == "__main__":
        
    news_feed = NewsFeed(interest='nasa', from_date='2023-08-01', to_date='2023-08-05', language='en')

    print(news_feed.get()) 