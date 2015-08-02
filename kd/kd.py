import nltk, re, pprint
from nltk import word_tokenize
from nltk import FreqDist
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer


f = open('kdtitle.txt', encoding="latin-1")
raw_title = f.read()
sample = 1700
type(raw_title)
tokens = word_tokenize(raw_title)
type(tokens)
len(tokens)
# nltk text
text_title = nltk.Text(tokens)
type(text_title)


# remove non-alphabetic
def remove_stopwords(text):
    word = [w.lower() for w in text if w.isalpha()]
    return [w for w in word if w not in stopwords.words('english') and w != '']


# lemma
def lemma(text):
    lmtzr = WordNetLemmatizer()
    return [lmtzr.lemmatize(w) for w in text]


# stem of word
def stem(word):
    regexp = r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$'
    stem, suffix = re.findall(regexp, word)[0]
    return stem


def lexical_diversity(text):
    return len(text) / len(set(text))

nostop_title = lemma(remove_stopwords(text_title))
nltk.Text(nostop_title).collocations()
# Frequency distribution of text
fdist_title = FreqDist(nostop_title)
fdist_title.most_common(50)
fdist_title.max()
fdist_title.plot(50, cumulative=True)#plot
fdist_title.plot(50)
total_words = len(set(nostop_title))
print("The total number of words in title of KD is: " + str(total_words))
avg_words = fdist_title.N()/total_words
print("Each word appears in title of KD is: " + str(int(avg_words)))


# process for text
f = open('kdtext.txt', encoding="latin-1")
raw_text = f.read()
# type
type(raw_text)
tokens = word_tokenize(raw_text)
type(tokens)
len(tokens)
text = nltk.Text(tokens)
type(text)
nostop_text = lemma(remove_stopwords(text))
nltk.Text(nostop_text).collocations()
fdist_text = FreqDist(nostop_text)
fdist_text.most_common(50)
fdist_text.max()
fdist_text.plot(50, cumulative=True)
fdist_text.plot(50)
total_textwords = len(set(nostop_text))
print("The total number of words in text of KD is: " + str(total_textwords))
avg_text = fdist_text.N()/total_textwords
print("Each word appears in text " + str(int(avg_text)) + " times")
    
    
    

