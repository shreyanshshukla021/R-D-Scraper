# Import necessary libraries
import pandas as pd
import numpy as np
from google_play_scraper import app, Sort, reviews_all

# Define function to scrape reviews for a specific country and language combination
def scrape_reviews(country, lang):
    reviews = reviews_all(
        'in.upstox.app',
        sleep_milliseconds=0,
        lang=lang,
        country=country,
        sort=Sort.NEWEST
    )
    reviews_df = pd.DataFrame(reviews)
    try:
        reviews_df = reviews_df[['reviewId', 'userName', 'userImage', 'content', 'score', 'thumbsUpCount', 'reviewCreatedVersion', 'at', 'replyContent', 'repliedAt']].assign(Country_name=df.loc[df['country'] == country, 'Country_name'].iloc[0], Language=lang)
    except KeyError:
        reviews_df = pd.DataFrame()
    return reviews_df

# Define dataframe containing country and language combinations
data = {'Country_name': ['Belgium', 'Belgium', 'Belgium', 'Belgium', 'Czechia', 'Czechia', 'Denmark', 'Denmark', 'Germany', 'Germany', 'Greece', 'Greece', 'Spain', 'Spain', 'France', 'France', 'Croatia', 'Croatia', 'Italy', 'Italy', 'Hungary', 'Hungary', 'Netherlands', 'Netherlands', 'Austria', 'Austria', 'Poland', 'Poland', 'Portugal', 'Portugal', 'Romania', 'Romania', 'Switzerland', 'Switzerland', 'Switzerland', 'Switzerland', 'Switzerland', 'Slovakia', 'Slovakia', 'Slovenia', 'Slovenia', 'Sweden', 'Sweden', 'Finland', 'Finland'],
        'country': ['BE', 'BE', 'BE', 'BE', 'CZ', 'CZ', 'DK', 'DK', 'DE', 'DE', 'GR', 'GR', 'ES', 'ES', 'FR', 'FR', 'HR', 'HR', 'IT', 'IT', 'HU', 'HU', 'NL', 'NL', 'AT', 'AT', 'PL', 'PL', 'PT', 'PT', 'RO', 'RO', 'CH', 'CH', 'CH', 'CH', 'CH', 'SK', 'SK', 'SI', 'SI', 'SE', 'SE', 'FI', 'FI'],
        'Language': ['Dutch', 'French', 'German', 'English', 'Czech', 'English', 'Danish', 'English', 'German', 'English', 'Greek', 'English', 'Spanish', 'English', 'French', 'English', 'Croatian', 'English', 'Italian', 'English', 'Hungarian', 'English', 'Dutch', 'English', 'German', 'English', 'Polish', 'English', 'Portuguese', 'English', 'Romanian', 'English', 'German', 'French', 'Italian', 'Romansh', 'English', 'Slovak', 'English', 'Slovenian', 'English', 'Swedish', 'English', 'Finnish', 'English'],
        'lang': ['nl', 'fr', 'de', 'en', 'cs', 'en', 'da', 'en', 'de', 'en', 'el', 'en', 'es', 'en', 'fr', 'en', 'hr', 'en', 'it', 'en', 'hu', 'en', 'nl', 'en', 'de', 'en', 'pl', 'en', 'pt', 'en', 'ro', 'en', 'de', 'fr', 'it', 'rm', 'en', 'sk', 'en', 'sl', 'en', 'sv', 'en', 'fi', 'en']
       }


df = pd.DataFrame(data)

reviews_dfs = df.apply(lambda row: scrape_reviews(row['country'], row['lang']), axis=1)
combined_reviews_df = pd.concat(reviews_dfs.to_list(), ignore_index=True)

#remove duplicates
combined_reviews_df = combined_reviews_df.groupby(['content', 'Language']).first().reset_index()
combined_reviews_df