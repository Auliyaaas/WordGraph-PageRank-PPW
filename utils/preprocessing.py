import re
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.util import ngrams

def get_stopwords():
    return set(stopwords.words('english') + stopwords.words('indonesian'))

def sentences_from_text(text):
    return sent_tokenize(text)

def build_terms(text):
    stop_words = get_stopwords()

    words = word_tokenize(text.lower())
    words = [
        w for w in words
        if w.isalpha() and len(w) > 1 and w not in stop_words
    ]

    unigrams = words
    bigrams = [f"{a}_{b}" for a, b in ngrams(words, 2)]

    return unigrams + bigrams
