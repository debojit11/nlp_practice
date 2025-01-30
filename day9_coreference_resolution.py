from transformers import pipeline

# Set up your Hugging Face Inference API (replace "YOUR_API_KEY" with your actual key)
model_name = "allenai/longformer-large-4096"
coref = pipeline("coreference-resolution", model=model_name, use_auth_token="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")

# Input text
text = "Anna went to the park. She enjoyed her time there."

# Perform coreference resolution
result = coref(text)
print(result)
