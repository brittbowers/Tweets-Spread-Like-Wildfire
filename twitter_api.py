import tweepy
import csv
# Authenticate to Twitter
auth = tweepy.OAuthHandler("n3rpM5i1xDH4X7tWcg51wK5Gd", "WMPDYP87KwsGZCT4dx8Tsun0Yn9HxGtGCL0wpL2F20lmgpPR9d")
auth.set_access_token("1192516987894714368-4wdTTFvVYq13mSxr0sknyf4i6RfweG","gngDz0JcBrwiT4sG99QN9tqP6dbXco1cSXkKAGPi3XCvO")

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# test authentication
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

with open('data/wildfire_recent.csv', 'w', newline = '') as csv_file:
    new_search = "wildfire" + " -filter:retweets"
    for tweet in tweepy.Cursor(api.search, q=new_search, lang="en").items():
        csv_writer = csv.writer(csv_file, delimiter = ',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([tweet.created_at, tweet.text, tweet.user.screen_name,
            tweet.user.followers_count, tweet.user.location])
