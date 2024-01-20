from google_play_scraper import app, Sort, reviews_all
from app_store_scraper import AppStore
import pandas as pd
import numpy as np
import json
import os
import uuid

# Google Play Reviews
g_reviews = reviews_all(
    "com.msf.angelmobiler",
    sleep_milliseconds=0,
    lang='en',
    country='us',
    sort=Sort.NEWEST,
)

# App Store Reviews
a_reviews = AppStore('us', 'angel-one-stocks-mutual-fund', '1060530981')
a_reviews.review()

# Google Play DataFrame
g_df = pd.DataFrame(np.array(g_reviews), columns=['review'])

# Check if there are any reviews before proceeding
if not g_df.empty:
    g_df2 = g_df.join(pd.DataFrame(g_df.pop('review').tolist()))

    # Check if the columns exist before dropping them
    columns_to_drop = ['reviewCreatedVersion', 'userImage']
    columns_to_drop = [col for col in columns_to_drop if col in g_df2.columns]
    g_df2.drop(columns=columns_to_drop, inplace=True, errors='ignore')

    g_df2.rename(columns={'score': 'rating', 'userName': 'user_name', 'reviewId': 'review_id',
                          'content': 'review_description', 'at': 'review_date', 'replyAt': 'developer_response_date',
                          'thumbsUpCount': 'thumbs_up'}, inplace=True)

    # Ensure g_df2 has enough columns before insertion
    if len(g_df2.columns) < 4:
        g_df2.insert(loc=3, column='review_title', value=None)

    g_df2.insert(loc=0, column='source', value='Google Play')
    g_df2['language_code'] = 'en'
    g_df2['country_code'] = 'us'

    # App Store DataFrame
    a_df = pd.DataFrame(np.array(a_reviews.reviews), columns=['review'])
    a_df2 = a_df.join(pd.DataFrame(a_df.pop('review').tolist()))

    a_df2.drop(columns={'isEdited'}, inplace=True)
    a_df2.insert(loc=0, column='source', value='App Store')
    a_df2['developer_response_date'] = None
    a_df2['thumbs_up'] = None
    a_df2['language_code'] = 'en'
    a_df2['country_code'] = 'us'
    a_df2.insert(loc=1, column='review_id', value=[uuid.uuid4() for _ in range(len(a_df2.index))])
    a_df2.rename(columns={'review': 'review_description', 'userName': 'user_name', 'date': 'review_date',
                          'title': 'review_title', 'developerResponse': 'developer_response'}, inplace=True)

    a_df2 = a_df2.where(pd.notnull(a_df2), None)

    # Concatenate DataFrames
    result = pd.concat([g_df2, a_df2])
    print(result)
else:
    print("No reviews found on Google Play.")
