from nltk.stem import PorterStemmer, WordNetLemmatizer

# Initialize the stemmer
stemmer = PorterStemmer()

# Initialize the lemmatizer
lematizer = WordNetLemmatizer()

# Example words
words=["playing", "learned", "studies", "gaming", "better", "worst", "gone"]

# Stem each word
stems=[stemmer.stem(word) for word in words]

# Lemmatize each word
lemmas=[lematizer.lemmatize(word) for word in words]

# lemmatize each word as verb, pos=v
lemmas_with_pos = [lematizer.lemmatize(word, pos='v') for word in words]

print("Original Words:", words)
print("Stemmed Words:", stems)
print("Lemmatized Words:", lemmas)# doesn't work properly for all words as by default it considers noun
print("Lemmatized Words with pos=v:", lemmas_with_pos) # works properly for all words as we have specified pos=v

# n	       Noun	            cat, table, freedom
# v	       Verb	            run, play, learn
# a	       Adjective        good, beautiful, tall
# r	       Adverb	        quickly, happily, yesterday
# s	  Adjective Satellite	better, worst, bigger

# How do stemming and lemmatization differ in their approach to simplifying words?
#ANS: Stemming is the process of reducing a word to its base form. It removes suffixes from words to reduce them to their root form.
#     Lemmatization is the process of reducing a word to its base or root form. It reduces words to their dictionary form or lemma.
#     Lemmatization is more sophisticated than stemming because it considers the context of the word in the sentence.
#     Stemming is faster than lemmatization, but lemmatization is more accurate.

# Can you think of use cases where stemming might be better than lemmatization?
#ANS: Stemming is better than lemmatization when we need to reduce words to their base form quickly and do not require high accuracy.
#     Stemming is used in search engines to index words and retrieve documents quickly, text analysis to identify patterns and relationships between words.
#     Stemming is used in text mining to extract information from large volumes of text data.

# Which technique gives more meaningful results, and why?
#ANS: Lemmatization gives more meaningful results than stemming because it reduces words to their dictionary form or lemma.
#     Lemmatization considers the context of the word in the sentence and provides more accurate results.
#     Lemmatization is used in natural language processing tasks such as sentiment analysis, named entity recognition, and text classification.
#     Lemmatization is used in information retrieval tasks such as search engines and text mining.