### source .env first

import os
import openai

openai.api_key = os.getenv("OPEN_AI_API_KEY")

# Create a request to the Completion endpoint
response = openai.completions.create(
  # Specify the correct model
  model="gpt-3.5-turbo-instruct",
  prompt="Who developed ChatGPT?"
)

print(response)
