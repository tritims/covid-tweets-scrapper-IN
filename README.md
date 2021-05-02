# covid-tweets-scrapper-IN
Scrape COVID-19 related tweets from India including news, notifications and public reaction from major cities

## Usage Example
```
from scrapetweeets import TwitterScraper as ts 
import pandas as pd 
import datetime as dt

# Get news by date
data = ts.get_news_and_notfications(dt.date(2021, 4, 27))
pd.DataFrame(data=data).to_csv('27_04_2021_n.csv')

# Get public reaction by date
data = ts.get_public_reaction(dt.date(2021, 4, 27))
pd.DataFrame(data=data).to_csv('27_04_2021_r.csv')
```
