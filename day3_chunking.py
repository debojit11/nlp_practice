from nltk import pos_tag, word_tokenize, RegexpParser

# Example sentence
sentence = "The little brown dog barked at the noisy cat in the garden."

# Tokenize and POS tag the sentence
words = word_tokenize(sentence)
tags = pos_tag(words)

# Define a grammar for noun phrases (NP)
grammar = "NP: {<DT>?<JJ>*<NN>}"

# Create a chunk parser
chunk_parser = RegexpParser(grammar)

# Parse the sentence to extract chunks
chunked_sentence = chunk_parser.parse(tags)

# Print the chunked sentence
print(chunked_sentence)