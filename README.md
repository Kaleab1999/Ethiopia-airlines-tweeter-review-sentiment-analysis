# Ethiopia-airlines-tweeter-review-sentiment-analysis
This project performs sentiment analysis on Twitter (now known as X) data related to Ethiopian Airlines. The goal is to classify a collection of tweets as either positive, neutral, or negative to gauge public opinion and customer satisfaction.

![image](https://user-images.githubusercontent.com/102003804/201592681-16861c99-d522-4524-85f1-b45239ff4a8b.png)



1. Project Overview
The project is divided into two main parts:

Data Scraping: Collecting relevant tweets from X.

Sentiment Classification: Analyzing the text content of each tweet and assigning a sentiment label (Positive, Neutral, or Negative).

The final output is a CSV file containing the original tweets, a sentiment score, and the classified sentiment.

2. Methodology
2.1. Data Scraping
Due to API limitations, this project relies on a conceptual non-API based web scraping approach. The code is structured to use a library like twikit to search for tweets containing the keywords "Ethiopian Airlines" or the hashtag "#EthiopianAirlines".

Note: The provided Python code contains a placeholder for the scraped data, as live scraping of Twitter/X data can be complex and requires specific library installations and potentially authentication.

2.2. Sentiment Classification
The sentiment analysis is performed using the VADER (Valence Aware Dictionary and sEntiment Reasoner) lexicon from the nltk library. VADER is a rule-based sentiment analyzer that is specifically tuned to analyze sentiments expressed in social media. It is quick, does not require training data, and performs well on short, informal text.

The classification process involves these steps:

Preprocessing: Cleaning the tweet text by removing URLs, mentions, hashtags, punctuation, and stopwords to prepare it for analysis.

Scoring: Applying the VADER analyzer to the cleaned text to get a compound score between -1 and +1.

Classification: Assigning a final sentiment label based on the compound score:

Positive: compound score >= 0.05

Neutral: -0.05 < compound score < 0.05

Negative: compound score <= -0.05
