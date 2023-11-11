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


## Providing example questions and answers can train the model
# in what you are expecting of it without the user being made aware
def fineTune():
  response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "system",
        "content": "You are a data science tutor who speaks concisely."
      },
      {
        "role": "user",
        "content": "How do you define a Python list?"
      },
      {
        "role": "assistant",
        "content": "Lists are defined by enclosing a comma-separated sequence of objects inside square brackets [ ]."
      },
      {
        "role": "user",
        "content": "What is the difference between mutable and immutable objects?"
      }
    ]
  )

  print(response.choices[0].message.content)

#categorise()
fineTune()