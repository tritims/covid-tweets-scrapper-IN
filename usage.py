from scrapetweeets import TwitterScraper as ts 
import pandas as pd 
import datetime as dt

# sc = Scraper()
# data = ts.get_news_and_notfications(dt.date(2021, 4, 27))
# print('===============================================')
# print(data)
# print('================================================')
# print(len(data))
# pd.DataFrame(data=data).to_csv('27_04_2021_n.csv')

data = ts.get_public_reaction(dt.date(2021, 4, 27))
print('===============================================')
print(data)
print('================================================')
print(len(data))
pd.DataFrame(data=data).to_csv('27_04_2021_r.csv')