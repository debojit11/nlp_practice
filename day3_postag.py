from nltk import pos_tag, word_tokenize

# Function to get POS tags for a sentence
def pos_tag_sentence(sentence):
    """ POS tag a sentence """
    words = word_tokenize(sentence)
    tagged_words = pos_tag(words)
    return tagged_words

# Example sentence
sentence = "The big cat chased a mouse through the garden."

# Get POS tags for the sentence
tags = pos_tag_sentence(sentence)

print("POS tags for sentence:", tags)