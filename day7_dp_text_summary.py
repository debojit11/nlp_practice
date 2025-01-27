import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Input sentence
sentence = "The Eiffel Tower, located in Paris, is a major tourist attraction."

# parse the sentence
doc = nlp(sentence)

# Extract main clause
main_clause = []
for token in doc:
    if token.dep_ in ["nsubj", "ROOT", "attr"]:
        main_clause.append(token.text)


# Extract additional details (e.g., location)
location = []
for token in doc:
    if token.dep_ == "prep":  # Look for prepositional modifiers
        for child in token.children:
            if child.dep_ == "pobj":  # Look for the object of the preposition
                location.append(f"{token.text} {child.text}")


# Generate summary
summary = f"{' '.join(main_clause)} {' '.join(location)}."
print("Summary:", summary)