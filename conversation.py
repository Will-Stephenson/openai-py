### source .env first

import os
import openai

openai.api_key = os.getenv("OPEN_AI_API_KEY")

## Chats
# Much cheaper than completions currently
#   gpt-3.5-turbo is 10x cheaper than gpt-3.5-turbo-instruct
# Designed for multi-turn conversations but also performs well on single turn tasks
# More customisable thanks to roles

## Conversation
# Because the OpenAI API is stateless, it is necessary to 
# feed all of the established context back into each request
# 
# This involves saving all messages to and from the endpoint
# to a persistent variable which can hold the data in the
# role/content format used by the model
# 
# Any new messages and responses are appended to this persitent
# variable and included in subsequent interactions 
#

messages = [
  {
    "role": "system",
    "content": "You are a Python tutor who provides concise answers to student questions"
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
    "content": "Introduce youself and ask how you can be of assitance"
  }
]

while (list(messages)[-1]['content'] != 'exit'): 
  
  response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages
  )
  print('\n' + response.choices[0].message.content + '\n\n')

  userInput = input("Enter question: ")
  messages.append({ "role" : "user", "content": userInput })


