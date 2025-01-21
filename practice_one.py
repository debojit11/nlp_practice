from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

sentence="Natural Language Processing is fun to learn!"
tokens=word_tokenize(sentence)
print("Tokens:", tokens)

stop_words = set(stopwords.words('english'))
fs = [word for word in tokens if word.lower() not in stop_words]
print("Filtered Tokens:",fs)

sen1="Chatbots are a cool application of NLP."
sen2="Python makes it easier to work with text."
tokens1=word_tokenize(sen1)
tokens2=word_tokenize(sen2)
sw1=set(stopwords.words('english'))
sw2=set(stopwords.words('english'))
fs1=[word for word in tokens1 if word.lower() not in sw1]
fs2=[word for word in tokens2 if word.lower() not in sw2]
print("Tokens1:",tokens1)
print("Filtered TOkens1:",fs1)
print("Tokens2:",tokens2)
print("Filtered Tokens2:",fs2)