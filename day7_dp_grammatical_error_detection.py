import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Input sentence
sentence = "She do not likes coffee."

# Parse the sentence
doc = nlp(sentence)

# Detect grammatical errors
errors = []


# Detect grammatical errors
errors = []
for token in doc:
    # Check for incorrect auxiliary verb
    if token.dep_ == "aux" and token.text != "does" and token.head.text == "likes":
        errors.append(f"Incorrect auxiliary verb: {token.text}")
    # Check for subject-verb agreement (relaxed condition)
    if token.dep_ == "nsubj" and token.head.text == "likes":
        errors.append(f"Subject-verb agreement error: {token.head.text}")

# Print detected errors
if errors:
    print("Errors detected:")
    for error in errors:
        print("-", error)

# Suggest corrections
corrected = sentence.replace("do not likes", "does not like")
print("Suggested Correction:", corrected)