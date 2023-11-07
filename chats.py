### source .env first

import os
import openai

openai.api_key = os.getenv("OPEN_AI_API_KEY")

## Chats
# Much cheaper than completions currently
#   gpt-3.5-turbo is 10x cheaper than gpt-3.5-turbo-instruct
# Designed for multi-turn conversations but also performs well on single turn tasks
# More customisable thanks to roles

## Roles
# System: controls assistants behaviour
# User: instruct the assistant
# Assistant: responds to user instruction
#   Can also be written by user to provide examples

def categorise():
  response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "system",
        "content": "You are a helpful data science tutor."
      },
      {
        "role": "user",
        "content": "What is the difference between a for loop and a while loop?"
      }
    ]
  )

  print(response)

categorise()