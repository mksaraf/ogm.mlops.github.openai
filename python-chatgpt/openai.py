import os
import openai

OPENAI_API_KEY = "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"
api_endpoint = "https://api.openai.com/v1/completions"
api_key = os.getenv("OPENAI_API_KEY")
# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.completions.create(
    model="text-davinci-003", prompt="Say this is a test", temperature=0, max_tokens=7)
