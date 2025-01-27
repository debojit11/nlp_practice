import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Input sentence
sentence = "Where is the Eiffel Tower?"

# parse the sentence
doc = nlp(sentence)

# Extract dependencies
print("Token\tHead\tDependency")
print("========================")
for token in doc:
    print(f"{token.text}\t{token.head.text}\t{token.dep_}")

# Extract the main components for the answer
for token in doc:
    if token.dep_== "nsubj": # Find the subject
        subject = token.text
    elif token.dep_ == "ROOT": # Find the main verb
        verb = token.text
    elif token.dep_ == "advmod": # Find the location query
        query = token.text

print("\n")
# Simulate answering
if query.lower() == "where" and subject.lower() == "tower":
    print(f"Answer: The {subject} is in Paris.")