### source .env first

import os
import openai

openai.api_key = os.getenv("OPEN_AI_API_KEY")

def askQuestion():
  response = openai.completions.create(
    model="gpt-3.5-turbo-instruct",
    prompt="Who developed ChatGPT? Give details",
    temperature=1 # range 0-2 (0 = near deterministic, 2 = random)
    # max_tokens=100 # for more verbose output - default is 30?
  )

  print(response.choices[0].text)

def transformText():
  
  prompt="""
  Update name to Steve, pronouns to he/him, and job title to janitor

  Tracy is a Software developer at S4S. Her favourite programming language is Python.
  """

  response = openai.completions.create(
    # Specify the correct model
    model="gpt-3.5-turbo-instruct",
    prompt=prompt,
  )

  print(response.choices[0].text)


askQuestion()
# transformText()