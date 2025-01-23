from nltk import pos_tag, word_tokenize, RegexpParser, ne_chunk
from nltk.tree import Tree
from nltk.tokenize import sent_tokenize

def analyze_paragraph(paragraph):
    # Tokenize into sentences
    sentences = sent_tokenize(paragraph)

    # initialize the results
    pos_tags =[]
    noun_phrases = []
    named_entities = []


    # Define chunk grammar for noun phrases
    grammar = "NP: {<DT>?<JJ>*<NN>}"
    chunk_parser = RegexpParser(grammar)


    for sentence in sentences:
        # Tokenize into words
        words = word_tokenize(sentence)
        tags = pos_tag(words)
        pos_tags.append(tags)

        # Extract noun phrases
        chunks = chunk_parser.parse(tags)
        for chunk in chunks:
            if isinstance(chunk, Tree) and chunk.label() == "NP":
                noun_phrases.append(" ".join(c[0] for c in chunk))

        
        # Extract named entities
        ner_chunks = ne_chunk(tags)
        for chunk in ner_chunks:
            if isinstance(chunk, Tree):
                named_entities.append(" ".join(c[0] for c in chunk))

        
    return{
        "POS Tags": pos_tags,
        "Noun Phrases": noun_phrases,
        "Named Entities": named_entities
    }


# Example paragraph
paragraph = """Barack Obama was born in Hawaii. He became the President of the United States. The White House is located in Washington, D.C."""

result = analyze_paragraph(paragraph)

print("POS tags:", result["POS Tags"])
print("Noun Phrases:", result["Noun Phrases"])
print("Named Entities:", result["Named Entities"])