#stemming
from nltk.stem import PorterStemmer

# Initialize the stemmer
stemmer = PorterStemmer()

# Example words
words=["running", "played", "happily", "studies", "better"]

# Stem each word
stems = [stemmer.stem(word) for word in words]
print("Original Words:", words)
print("Stemmed Words:", stems)