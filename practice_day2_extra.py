from nltk import word_tokenize, pos_tag
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet


# Function to map NLTK POS tags to WordNet POS tags
def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN
    
# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Example paragraph
paragraph = "The quick brown foxes were jumping over the lazy dogs happily."

# Tokenize the paragraph
words = word_tokenize(paragraph)

# Get the POS tags for each word
tagged_words = pos_tag(words)

# Lemmatize each word with its POS tag
lemmatized_words = []
for word, tag in tagged_words:
    wordnet_pos = get_wordnet_pos(tag) # Convert POS tag to WordNet format
    if wordnet_pos:
        lemmatized_words.append(lemmatizer.lemmatize(word, pos=wordnet_pos))
    else:
        lemmatized_words.append(lemmatizer.lemmatize(word)) # Default to noun


print("Orginal Words:", words)
print("POS_tags:", tagged_words)
print("Lemmatized Words:", lemmatized_words)
