from nltk import word_tokenize, pos_tag, RegexpParser

# Example sentence
sentence = "The quick brown fox jumped over the lazy dog."

# tokenize and pos tag the sentence
words = word_tokenize(sentence)
tags = pos_tag(words)

# Define a more complex grammar
grammar = r"""
    NP: {<DT>?<JJ.*>*<NN.*>}       # Noun phrase: Determiner + adjectives + noun
    VP: {<VB.*><NP|PP|PRP>*}       # Verb phrase: Verb + noun phrases or prepositional phrases
    PP: {<IN><NP>}                 # Prepositional phrase: Preposition + noun phrase
"""

chunk_parser = RegexpParser(grammar)

chunks = chunk_parser.parse(tags)

# Print the resulting chunk tree
print(chunks)


# Define an updated custom grammar for chunking
grammar2 = r"""
    NP: {<DT>?<JJ.*>*<NN.*>}   # Noun phrase: determiners, adjectives, and nouns
    VP: {<VB.*><NP|PP|RB>*}     # Verb phrase: verbs followed by optional noun phrases, prepositional phrases, or adverbs
    CLAUSE: {<NP><VP>}          # Clause: noun phrase followed by verb phrase
    PP: {<IN><NP>}              # Prepositional phrase: preposition followed by a noun phrase
"""

chunk_parser2 = RegexpParser(grammar2)

chunks2 = chunk_parser2.parse(tags)

# Print the resulting chunk tree
print(chunks2)