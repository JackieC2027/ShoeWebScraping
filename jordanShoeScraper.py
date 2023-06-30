import snscrape.modules.twitter as sntwitter
import requests

maxTweetValue = 1000
dateAndContent = []
contentList = []
tweetContentList = []
jordanTweetList = []

for tweetCounter, tweet in enumerate(sntwitter.TwitterUserScraper("SneakerShouts").get_items()):
    if tweetCounter > maxTweetValue:
        break
    else:
        dateAndContent.append([tweet.date, tweet.rawContent])
      
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

for eachCompletedTweet in tweetContentList:
    for eachWord in eachCompletedTweet.split():
        if "jordan" in eachWord.lower():
            jordanTweetList.append(eachCompletedTweet)
for eachTweet in jordanTweetList:
    resp = requests.post('https://textbelt.com/text', {
  'phone': '6097726637',
  'message': eachTweet,
  'key': 'c09f74dc93d4b4f2963c7a81aa6e4369da6afd117pCYOS2jUsXP8heLj7DAmJq60',
})