from nltk import ne_chunk, pos_tag, word_tokenize, RegexpParser
from nltk.tree import Tree

# Example sentence
sentence = "Barack Obama was born in Hawaii and became the President of the United States."

# Tokenize and POS tag the sentence
words = word_tokenize(sentence)
tags = pos_tag(words)

# Perform named entity chunking
ner_chunks = ne_chunk(tags)

# Extract named entities from the chunks
named_entities = []
for chunk in ner_chunks:
    if isinstance(chunk, Tree):
        named_entities.append(" ".join(c[0] for c in chunk))


print("Named Entities:", named_entities)

# the above code doesnt handle name as a single entity but as two entities as we wre using ne_chunk
# but the below code will handle it as a single entity


# # Perform named entity chunking using general NER
# ner_chunks_general = ne_chunk(tags)

# # Custom grammar for full names
# grammar = "PERSON: {<NNP>+}"  # Matches sequences of proper nouns as a single entity
# chunk_parser = RegexpParser(grammar)

# # Perform named entity chunking using custom grammar
# ner_chunks_custom = chunk_parser.parse(tags)

# # Extract named entities from both chunkings
# named_entities_general = []
# named_entities_custom = []

# for chunk in ner_chunks_general:
#     if isinstance(chunk, Tree):
#         named_entities_general.append(" ".join(c[0] for c in chunk))

# for chunk in ner_chunks_custom:
#     if isinstance(chunk, Tree):
#         named_entities_custom.append(" ".join(c[0] for c in chunk))

# # Merging both results into a single list
# combined_named_entities = named_entities_general + named_entities_custom

# print("Combined Named Entities:", combined_named_entities)