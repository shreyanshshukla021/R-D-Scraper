from google_play_scraper import app, Sort, reviews_all

# Replace 'com.nextbillion.groww' with the package name of the Groww app
package_name = 'com.nextbillion.groww'

# Fetch app details
app_details = app(package_name)

# Fetch all reviews for the Groww app
reviews = reviews_all(
    package_name,
    sleep_milliseconds=0,  # optional, defaults to 0
    lang='en',  # optional, defaults to 'en'
    country='us',  # optional, defaults to 'us'
    sort=Sort.NEWEST,  # optional, defaults to Sort.MOST_RELEVANT
)

# Display some app details
print(f"Groww App Title: {app_details['title']}")
print(f"Number of Reviews: {len(reviews)}")

# Display the details of a few reviews
for review in reviews[:5]:
    print(f"\nReview ID: {review['reviewId']}")
    print(f"User Name: {review['userName']}")
    print(f"Rating: {review['score']}")
    print(f"Review Date: {review['at']}")
    print(f"Review Title: {review['title']}")
    print(f"Review Text: {review['content']}")
    print(f"Thumbs Up: {review['thumbsUpCount']}")
    print(f"Developer Reply: {review['replyContent']}")
    print(f"Developer Reply Date: {review['repliedAt']}\n")
