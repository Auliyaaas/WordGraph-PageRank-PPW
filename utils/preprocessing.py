from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.util import ngrams

STOPWORDS = set(stopwords.words('english') + stopwords.words('indonesian'))

def sentences_from_text(text):
    return sent_tokenize(text)

def build_terms(sentences):
    words = word_tokenize(" ".join(sentences).lower())
    unigrams = [w for w in words if w.isalpha() and len(w) > 1 and w not in STOPWORDS]
    bigrams = [f"{a}_{b}" for a, b in ngrams(unigrams, 2)]
    return unigrams + bigrams