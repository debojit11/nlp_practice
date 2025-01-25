import spacy

# Load the spaCy language model
nlp = spacy.load('en_core_web_sm')

# Input sentence
sentence = "The quick brown fox jumps over the lazy dog."

# process the sentence
doc = nlp(sentence)

# Display dependency parsing
print(f"{'Token':<10}{'Head':<10}{'Dependency':<10}")
print("="*30)
for token in doc:
    print(f"{token.text:<10}{token.head.text:<10}{token.dep_:<15}")

# Visualize the dependency tree (if you're using Jupyter or a GUI-supported tool)
spacy.displacy.serve(doc, style="dep", port=8000)