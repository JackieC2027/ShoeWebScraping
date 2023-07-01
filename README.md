# Shoe Web Scraping

The Jordan Shoe Scraper is a Python script that scrapes tweets from the Twitter account "SneakerShouts" to find tweets related to Jordan shoes. As an avid shoe collector, I wanted to automate the process of finding new Jordan releases, as these tend to be “sniped” or electronically bought by bots on Twitter. Ensuring that the news in released on a daily basis, I can be one of the first users to access, view, and act on the tweets from this credible shoe news Twitter page.

# Prerequisites
<h3>Python 3.6 or higher</h3>
- snscrape library
- pyinstaller package
- requests library

# Installation

1. Clone the repository or download the script file.
2. Install the required libraries by running the following command:

```pip install snscrape requests pyinstaller```

# Usage
Open the jordanShoeScraper.py file in a text editor.

Modify the script's configuration according to your requirements:

- maxTweetValue: The maximum number of tweets to scrape.
- phone: Your phone number to receive SMS notifications.
- key: Your API key from Textbelt for sending SMS notifications.

Save the changes.

<h3>Run the script by executing the following command in the terminal:</h3>

```python jordanShoeScraper.py```

# Preview

<img src="https://github.com/JackieC2027/shoewebscraping/assets/110410844/61ef70aa-1b21-4713-a031-4a1211cfab18">

# How It Works

Tweets from the Twitter account, "@SneakerShouts" are scraped to gather the freshest releases of Jordans.  

Using the snscrape library and its API endpoints, the Tweets are stored in a list, following several string formations and looping of the tweets themselves. 

Based on certain keywords that are related to Jordans, these specific tweets are organized into a JSON request from Textbelt’s API that works with SMS automation. 

Every day @ 7:30 PM, (23:30 UTC) the script would be running on a CronJob, in cohesion with PyInstaller, to send a message to my personal phone about new releases. 

# Notes

Make sure you have a stable internet connection to scrape tweets and send SMS notifications successfully.
Take into account any rate limits or restrictions imposed by the Twitter API and Textbelt API.
Feel free to customize the script further based on your specific requirements.
Please ensure that you use the script responsibly and comply with the terms of service of the platforms and APIs used.
