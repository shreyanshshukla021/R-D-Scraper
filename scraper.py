import google_play_scraper
from bs4 import BeautifulSoup
import requests
import pandas as pd


app_id = 'com.nextbillion.groww'  # Replace with the actual app ID
lang = 'en'
country = 'us'
num_reviews = 1000
reviews = google_play_scraper.reviews(
    app_id, lang=lang, country=country,
)

df = pd.DataFrame(reviews)
df.to_csv('app_reviews.csv', index=False)
