#lemmatization
from nltk.stem import WordNetLemmatizer
from nltk import download

#download wordnet data
download('wordnet')
download('omw-1.4') # For multilingual WordNet support
# already downloaded for me

# Initialize the lemmatizer
lematizer= WordNetLemmatizer()

# Example words
words=["running", "played", "happily", "studies", "better"]

# Lemmatize each word
lemmas = [lematizer.lemmatize(word) for word in words]
print("Original Words:", words)
print("Lemmatized Words:", lemmas) 
