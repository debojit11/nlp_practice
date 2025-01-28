import spacy
from textblob import TextBlob
# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Input sentence
compound_sentence = "The movie was amazing, but the ending was terrible."

# Parse the sentence
doc = nlp(compound_sentence)

# Separate clauses based on conjunctions
clauses = []
current_clause = []
for token in doc:
    if token.dep_ == "cc":  # Conjunction found
        clauses.append(" ".join(current_clause))  # Add the first clause
        current_clause = [token.text]  # Start the second clause with the conjunction
    else:
        current_clause.append(token.text)

# Add the last clause
clauses.append(" ".join(current_clause))

# Analyze sentiment for each clause
for i, clause in enumerate(clauses, 1):
    blob = TextBlob(clause)
    print(f"Clause {i}: {clause.strip()}")
    print(f"  Sentiment Polarity: {blob.sentiment.polarity}")