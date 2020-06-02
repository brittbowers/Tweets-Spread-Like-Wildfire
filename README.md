# Tweets Spread Like Wildfire

The objective of this project is to analyze tweets from the past 3 years of wildfires and conduct topic modeling to predict things like senitment change, discussion shift, and location importance. 

**Dataset:**

The data was collected using a combination of the Twitter API and the GetOldTweets module provided open source on github for collecting older tweets using python. Data was stored in and an EC2 instance on AWS using MongoDB. 

**Write Up**

I wrote a blog about the special kind of short text clustering used in this project [here](https://brittanybowers.com/a-unique-approach-to-short-text-clustering-part-1-algorithmic-theory/) and the NLP tools used for scrubbing and processing tweets [here](https://brittanybowers.com/a-unique-approach-to-short-text-clustering-part-2-tweets-spread-like-wildfire/)

**Conclusions**

There are many interesting findings in this dataset. The NLP exploration here was most fascinating to me where the discussion shifts more in the direction of policy tweets vs reactionary disaster tweets over the 3 years. 