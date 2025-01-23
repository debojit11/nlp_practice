from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
sentence = "I love learing NLP with Python!"

tokens=word_tokenize(sentence)

print("Tokens:",tokens)

stop_words = set(stopwords.words('english'))
fs= [word for word in tokens if word.lower() not in stop_words]
print("Filtered Tokens:",fs)