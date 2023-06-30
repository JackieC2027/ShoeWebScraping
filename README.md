# Shoe Web Scraping

The Jordan Shoe Scraper is a Python script that scrapes tweets from the Twitter account "SneakerShouts" to find tweets related to Jordan shoes. As an avid shoe collector, I wanted to automate the process of finding

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

![unnamed](https://github.com/JackieC2027/shoewebscraping/assets/110410844/efd2b154-a08e-4cc8-922f-6ef566977efb)

# How It Works

Tweets from the Twitter account, "@SneakerShouts" are scraped to gather the freshest releases of Jordans. Using the scrape library and API endpoints, the tweets are scraped on a daily basis and sorted to find keywords that are related to Jordan shoes.

# Notes

Make sure you have a stable internet connection to successfully scrape tweets and send SMS notifications.
Take into account any rate limits or restrictions imposed by the Twitter API and Textbelt API.
Feel free to customize the script further based on your specific requirements.
Please ensure that you use the script responsibly and comply with the terms of service of the platforms and APIs used.
