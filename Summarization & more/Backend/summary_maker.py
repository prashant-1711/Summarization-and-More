import nltk
#import re
#import requests

from newspaper import Article
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')
def analyze_keywords(url):
    article_name = Article(url, language="en")
    article_name.download()
    article_name.parse()
    article_name.nlp()
    keywords = article_name.keywords
    print("Keywords:", keywords) 
    return keywords

def analyze_summary(url):
    article_name = Article(url, language="en")
    article_name.download()
    article_name.parse()
    article_name.nlp()
    summary = article_name.summary
    clean_summary = summary.replace('\n', ' ')
    return clean_summary


def load_and_preprocess_article(url):
    article_name = Article(url, language="en")
    article_name.download() #Makes an HTTP request to download the article content from the given URL.
    article_name.parse()
    article_name.nlp()
    article = article_name.text
    text_tokens = word_tokenize(article)
    tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
    final_article = " ".join(tokens_without_sw)
    return final_article

def pos_score(final_article):
    score = SentimentIntensityAnalyzer().polarity_scores(final_article)
    return score['pos']

def negative_score(final_article):
    score = SentimentIntensityAnalyzer().polarity_scores(final_article)
    return score['neg']


def getPolarity(final_article):
   return TextBlob(final_article).sentiment.polarity


def analyze_sentiment(final_article):
    pos_score_val = pos_score(final_article)
    neg_score_val = negative_score(final_article)
    
    sentiment = 'positive' if pos_score_val > neg_score_val else 'negative'
    
    result = {
        'sentiment': sentiment,
        'positive_score': pos_score_val,
        'negative_score': neg_score_val,
    }
    
    return result