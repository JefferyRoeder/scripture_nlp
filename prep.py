import pandas as pd
import numpy as np
import unicodedata
import time
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords
import re

def basic_clean(string):
    """
    Lowercase the string
    Normalize unicode characters
    Replace anything that is not a letter, number, whitespace or a single quote.
    """
    string = string.lower()
    string = string.replace('c++','cplusplus')
    string = unicodedata.normalize('NFKD', string).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    
    # remove anything not a space character, an apostrophy, letter, or number
    string = re.sub(r"[^a-z0-9'\s]", '', string)

    # convert newlines and tabs to a single space
    string = re.sub(r'[\r|\n|\r\n]+', ' ', string)
    
    string = string.strip()
    return string

def tokenize(s):
    tokenizer = nltk.tokenize.ToktokTokenizer()
    return tokenizer.tokenize(s, return_str=True)



def remove_stopwords(s,extra_words =[], exclude_words = []):
    #Tokenize the string
    s = tokenize(s)
    
    words = s.split()
    stopword_list = stopwords.words('english')
    
    #remove the excluded words fro the stopword list
    stopword_list = set(stopword_list) - set(exclude_words)
    
    #add in the user specified extra words
    stopword_list = stopword_list.union(set(extra_words))
    
    filtered_words = [w for w in words if w not in stopword_list]
    final_string = ' '.join(filtered_words)
    return final_string

def lemmatize(s):
    wnl = nltk.stem.WordNetLemmatizer()
    lemmas = [wnl.lemmatize(word) for word in s.split()]
    string_of_lemmas = ' '.join(lemmas)
    return string_of_lemmas


def stem(s):
    ps = nltk.porter.PorterStemmer()
    stems = [ps.stem(word) for word in s.split()]
    string_of_stems = ' '.join(stems)
    return string_of_stems


def prep_urls(df):
    df['original'] = df.readme_contents
    df['clean'] = df.readme_contents.apply(basic_clean).apply(remove_stopwords)
    df['stemmed'] = df.clean.apply(stem)
    df['lemmatized'] = df.clean.apply(lemmatize)
    
    #df.drop(columns = ['body'], inplace = True)
    return df

def text_join(text):
    return "".join(text)