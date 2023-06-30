mport snscrape.modules.twitter as sntwitter
import requests

maxTweetValue = 1000
dateAndContent = []     # List to store tweet dates and content
contentList = []        # List to store filtered tweet content
tweetContentList = []   # List to store final tweet content
jordanTweetList = []    # List to store tweets related to Jordan

# Scrape tweets from the Twitter user "SneakerShouts" and store date and content in dateAndContent list
for tweetCounter, tweet in enumerate(sntwitter.TwitterUserScraper("SneakerShouts").get_items()):
    if tweetCounter > maxTweetValue:
        break
    else:
        dateAndContent.append([tweet.date, tweet.rawContent])
      
# Filter tweets based on time (hour) and store the content in contentList
for value in range(len(dateAndContent)):
    tweet = dateAndContent[value]
    maxValue = int(tweet[0].strftime("%H"))
    if maxValue <= 23 and maxValue >= 0:
        contentList.append(tweet[1])

        if value + 1 < len(dateAndContent):
            nextTweet = dateAndContent[value + 1]
            nextValue = int(nextTweet[0].strftime("%H"))

            if maxValue >= nextValue:
                continue
            else:
                break
    else:
        break

# Extract desired tweet content from contentList
for content in contentList:
    desiredContent = content
    desiredPhrase = desiredContent.split("\n")
    firstString = desiredPhrase[0]
    firstWord = firstString.split()[0]
    if firstWord.lower() == "release":
        if len(desiredPhrase) > 1:
            tweetContentList.append(desiredPhrase[1])
    elif firstWord.lower() == "rt":
        break
    else:
        tweetContentList.append(desiredPhrase[0])

# Check if each tweet in tweetContentList contains the word "jordan" (case insensitive)
# If it does, add it to the jordanTweetList
for eachCompletedTweet in tweetContentList:
    for eachWord in eachCompletedTweet.split():
        if "jordan" in eachWord.lower():
            jordanTweetList.append(eachCompletedTweet)

# Send each tweet in jordanTweetList as a text message using the Textbelt API
for eachTweet in jordanTweetList:
    resp = requests.post('https://textbelt.com/text', {
        'phone': '6097726637',   # Replace with desired phone number
        'message': eachTweet,
        'key': 'REDACTED',        # Replace with your Textbelt API key
    })
