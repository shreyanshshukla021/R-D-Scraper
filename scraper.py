from google_play_scraper import app, reviews_all
import pandas as pd

# Replace 'com.nextwealth.groww' with the actual package name for the Groww app
package_name = 'com.nextbillion.groww'

# Fetch app details
app_details = app(package_name)

# Fetch all reviews for the app
reviews = reviews_all(
    package_name,
    sleep_milliseconds=0,  # optional, defaults to 0
    lang='en',  # optional, defaults to 'en'
    country='us',  # optional, defaults to 'us'
)

# Create a DataFrame from the reviews data
reviews_df = pd.DataFrame(reviews)

# Export the DataFrame to a CSV file
csv_filename = 'groww_reviews.csv'
reviews_df.to_csv(csv_filename, index=False)

print(f"Reviews exported to {csv_filename}")
