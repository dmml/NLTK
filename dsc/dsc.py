import nltk, re, pprint
from nltk import word_tokenize
from nltk import FreqDist
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer

f = open('title.txt', encoding="latin-1")
raw_title = f.read()
sample = 1700
# type
type(raw_title)
tokens = word_tokenize(raw_title)
type(tokens)
len(tokens)
text_title = nltk.Text(tokens)  # nltk text
type(text_title)


# remove non-alphabetic
def remove_stopwords(text):
    word = [w.lower() for w in text if w.isalpha()]
    return [w for w in word if w not in stopwords.words('english') and w != '']


# lemma
def lemma(text):
    lmtzr = WordNetLemmatizer()
    return [lmtzr.lemmatize(w) for w in text]

nostop_title = lemma(remove_stopwords(text_title))
# check the collocations of text
nostop_title = nltk.Text(nostop_title)
nostop_title.collocations()
fdist_title = FreqDist(nostop_title)  # Frequency distribution of text
fdist_title.most_common(50)  # most common 50
fdist_title['science']  # return count of a given word
fdist_title.max()  # max counts
fdist_title.plot(50, cumulative=True)  # plot
fdist_title.plot(50)
fdist_title.tabulate(50)  # tabulate
total_words = len(set(nostop_title))
print("The total number of words in title of dsc is: " + str(total_words))
avg_words = fdist_title.N() / total_words
print("Each word appears in title of dsc is: " + str(int(avg_words)))


# stem function that only keep stem of the words
def stem(word):
    regexp = r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$'
    stem, suffix = re.findall(regexp, word)[0]
    return stem


def lexical_diversity(text):
    return len(text) / len(set(text))


# process for author######
f = open('author.txt', encoding="latin-1")
raw_author = f.read()
author_list = [a for a in (re.split(r'[\t\n]+', raw_author)) if 2 < len(a) < 29]
author_list = nltk.Text(author_list)

fdist_author = FreqDist(author_list)
fdist_author.max()
fdist_author.freq('Vincent Granville')
fdist_author.tabulate(10)
fdist_author.plot(50, cumulative=True)
fdist_author.most_common(10)
popular_author = ['Vincent Granville', 'Michael Walker', 'Mirko Krivanek', 'Don Philip Faithful', 'William Vorhies',
                  'Bernard Marr']
total_author = len(set(author_list))
print("The total number of author in dsc is: " + str(total_author))
avg_post = 1700 / len(set(author_list))
print("Each author post " + str(int(avg_post)) + " blogs in dsc")

# process for text #############
f = open('text.txt', encoding="latin-1")
raw_text = f.read()
# type
type(raw_text)
tokens = word_tokenize(raw_text)
type(tokens)
len(tokens)
# nltk text
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
print("The total number of words in text of dsc is: " + str(total_textwords))
avg_text = fdist_text.N() / total_textwords
print("Each word appears in text " + str(int(avg_text)) + " times")