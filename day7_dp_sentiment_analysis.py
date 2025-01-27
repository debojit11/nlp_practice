from textblob import TextBlob
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")


# Input sentence
sentence = "The movie was not bad."

# Parse the sentence
doc = nlp(sentence)


# Check for negation and associated adjectives
negated_adjective = None
for token in doc:
    # Look for adjectives (acomp) with negation (neg) modifying their auxiliary verb (cop)
    if token.dep_ == "acomp" and any(child.dep_ == "neg" for child in token.head.children):
        negated_adjective = token.text
        print("Detected negated adjective:", negated_adjective)

# Calculate sentiment using TextBlob
blob = TextBlob(sentence)
print("Polarity Score:", blob.sentiment.polarity)

# Adjust polarity for negation
if negated_adjective:
    print("Adjusted Sentiment: Neutral-to-Positive")