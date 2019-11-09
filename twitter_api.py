import tweepy
# Authenticate to Twitter
auth = tweepy.OAuthHandler("n3rpM5i1xDH4X7tWcg51wK5Gd", "WMPDYP87KwsGZCT4dx8Tsun0Yn9HxGtGCL0wpL2F20lmgpPR9d")
auth.set_access_token("1192516987894714368-4wdTTFvVYq13mSxr0sknyf4i6RfweG","gngDz0JcBrwiT4sG99QN9tqP6dbXco1cSXkKAGPi3XCvO")

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True,
                parser=tweepy.parsers.JSONParser())

# test authentication
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

api.search(q="fire", lang="en", until="2019-10-10", count = 10)
