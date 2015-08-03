import nltk, re, pprint
from nltk import word_tokenize
from nltk import FreqDist
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import bigrams
from nltk import trigrams


# remove non-alphabetic
def remove_stopwords(text):
    word = [w.lower() for w in text if w.isalpha()]
    return [w for w in word if w not in stopwords.words('english') and w != '']


# lemma
def lemma(text):
    lmtzr = WordNetLemmatizer()
    return [lmtzr.lemmatize(w) for w in text]


# stem function that only keep stem of the words
def stem(word):
    regexp = r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$'
    stem, suffix = re.findall(regexp, word)[0]
    return stem


def lexical_diversity(text):
    return len(text) / len(set(text))

# input scrapy data and clean, lemma, remove stop words
f = open('title.txt', encoding="latin-1")
raw_title = f.read()
tokens = word_tokenize(raw_title)
text_title = nltk.Text(tokens)
nostop_title_dsc = lemma(remove_stopwords(text_title))
f.close()
f = open('text.txt', encoding="latin-1")
raw_text = f.read()
tokens = word_tokenize(raw_text)
text = nltk.Text(tokens)
nostop_text_dsc = lemma(remove_stopwords(text))
f.close()
f = open('kdtitle.txt', encoding="latin-1")
raw_title = f.read()
tokens = word_tokenize(raw_title)
text_title = nltk.Text(tokens)
nostop_title_kd = lemma(remove_stopwords(text_title))
f.close()
f = open('kdtext.txt', encoding="latin-1")
raw_text = f.read()
tokens = word_tokenize(raw_text)
text_kd = nltk.Text(tokens)
nostop_text_kd = lemma(remove_stopwords(text_kd))
f.close()

# Frequency Distribution
title = nostop_title_dsc + nostop_title_kd
nltk.Text(title).collocations()
fdist_title = FreqDist(title)
fdist_title.most_common(50)
fdist_title.plot(50, cumulative=True)
fdist_title.plot(50)
total_words = len(set(title))
print("The total number of words in title of dsc is: " + str(total_words))
avg_words = fdist_title.N() / total_words
print("Each word appears in title of dsc is: " + str(int(avg_words)))

text = nostop_text_dsc + nostop_text_kd
nltk.Text(text).collocations()
fdist_text = FreqDist(text)
fdist_text.most_common(50)
fdist_text.max()
fdist_text.plot(50, cumulative=True)
fdist_text.plot(50)
total_textwords = len(set(text))
print("The total number of words in text is: " + str(total_textwords))
avg_text = fdist_text.N() / total_textwords
print("Each word appears in text " + str(int(avg_text)) + " times")

# bigrams and trigrams
word_pair_text = list(bigrams(text))
word_triple_text = list(trigrams(text))
bigrams_text = FreqDist(word_pair_text)
trigrams_text = FreqDist(word_triple_text)
bigrams_text.most_common(50)
bigrams_text.plot(50,cumulative=True)
trigrams_text.most_common(20)
bigrams_text.plot(50)
trigrams_text.plot(20)
trigrams_text.plot(50,cumulative=True)

word_pair = list(bigrams(title))
word_triple = list(trigrams(title))
bigrams_title = FreqDist(word_pair)
trigrams_title = FreqDist(word_triple)
bigrams_title.most_common(50)
bigrams_title.plot(50,cumulative=True)
trigrams_title.most_common(20)
bigrams_title.plot(50)
trigrams_title.plot(20)
trigrams_title.plot(50,cumulative=True)
