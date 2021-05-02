import twint
import json
import copy
import datetime as dt
import pandas as pd

class Scraper:
    def __init__(self):
        self.news_handles = ['ndtv', 'indiatoday', 'republic', 'timesnow', 'ddindialive', 'cnnnews18', 
                             'the_hindu', 'toiindianews', 'httweets', 'theprintindia', 'thewire_in',
                             'indiatimes', 'firstpost', 'opindia_com', 'livemint', 'thequint', 'scroll_in']
        
        self.news_agencies = ['ani', 'ians_india', 'pti_news', 'uniindianews']
        self.govt_handles = ['COVIDNewsByMIB', 'MoHFW_INDIA', 'mygovindia']
        self.search_terms = ['covid', 'covid-19', 'coronavirus', 'vaccine', 'vaccination', 'lockdown', 'remdesivir',
                             'oxygen', 'cryogenic', 'pandemic']
        
        self.cities = ['mumbai', 'delhi', 'bangalore', 'hyderabad', 'chennai', 'kolkata', 'indore', 'guwahati']

        # Define limits per keyword 
        self.tweets_reaction_limit = 20 # per city
        self.tweets_news_limit = 100 # per handle

    def __scrape__(self, keyword, from_date, to_date, location, limit, username='', only_news=False):
        c = twint.Config()
        c.Search = keyword
        if(only_news):
            c.Username = username
        c.Since = str(from_date)
        c.Until = str(to_date)
        c.Limit = limit
        c.Lang = 'en'
        c.Popular_tweets = True
        c.Store_object = True
        c.Near = location
        twint.run.Search(c)
        res_list = []
        for tweet in twint.output.tweets_list:
            try:
                res_list.append({
                    'id': tweet.id,
                    'date': str(from_date),
                    'tweet': tweet.tweet,
                    'tweeted_by': tweet.username,
                    'link': tweet.link.split('/')[-1],
                    'loc': tweet.near,
                    'type': 'news' if only_news else 'react'
                })
            except:
                pass
        return res_list

    def remove_duplicates(self, a):
        df = pd.DataFrame(a)
        df.drop_duplicates(subset=['id'], inplace=True)
        return json.loads(df.to_json(orient='records'))
        

    def get_public_reaction(self, date):
        res = []
        for location in self.cities:
            for key in self.search_terms:
                try:
                    res = res + self.__scrape__(key, 
                                                date, 
                                                date + dt.timedelta(days=1), 
                                                location, 
                                                self.tweets_reaction_limit, 
                                                only_news=False)
                except:
                    pass
        return self.remove_duplicates(res) 

    def get_news_and_notfications(self, date):
        res = []
        for outlet in self.news_agencies:
            for key in self.search_terms:
                try: 
                    res = res + self.__scrape__(key,
                                                date, 
                                                date + dt.timedelta(days=1), 
                                                'india',
                                                self.tweets_news_limit, 
                                                outlet, 
                                                only_news=True)
                except:
                    pass
        # print('>>>>>>>>>>>>>>>>>>>')
        # print(res)
        return self.remove_duplicates(res)

TwitterScraper = Scraper()

