import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Input sentence
sarcastic_sentence = "Oh great, another rainy day."

# Parse the sentence
doc = nlp(sarcastic_sentence)

# Detect sarcasm clues using dependency parsing
sarcasm_detected = False

# Define positive and negative words
positive_words = ["great", "amazing", "wonderful"]
negative_words = ["rainy", "terrible", "awful"]

# Find the root of the sentence
root = [token for token in doc if token.head == token][0]  # The root word

# Check if the root is connected to a positive word
for token in doc:
    if token.text.lower() in positive_words and token.head == root:
        # Check if any descendant of the root is a negative word
        for descendant in root.subtree:
            if descendant.text.lower() in negative_words:
                sarcasm_detected = True

# Print result
print("Sarcasm Detected" if sarcasm_detected else "No Sarcasm Detected")