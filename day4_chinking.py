from nltk import pos_tag, word_tokenize, RegexpParser

# Example sentence
sentence = "The tall and very energetic boy ran quickly to the park."

# Tokenize and POS tag the sentence
words = word_tokenize(sentence)
tags = pos_tag(words)

# Manually correct any POS tagging issues (if needed)
tags = [
    ("The", "DT"), 
    ("tall", "JJ"), 
    ("and", "CC"), 
    ("very", "RB"), 
    ("energetic", "JJ"), 
    ("boy", "NN"), 
    ("ran", "VBD"), 
    ("quickly", "RB"), 
    ("to", "TO"), 
    ("the", "DT"), 
    ("park", "NN"), 
    (".", ".")
]

# Refine the grammar to include conjunctions and sequences of adjectives
grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>}   # Chunk determiners, adjectives, and nouns
        {<DT><JJ.*>*}          # Explicitly chunk determiner + adjectives
        }<CC|RB|TO>+{          # Chink out conjunctions, adverbs, and "to"
"""

chunk_parser = RegexpParser(grammar)

# Apply the parser
chunks = chunk_parser.parse(tags)

# Print the resulting chunk tree
print(chunks)