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

def summariseText():
  
  prompt="""
  Summarize the following text into two concise bullet points:
  Investment refers to the act of committing money or capital to an enterprise 
  with the expectation of obtaining an added income or profit in return. There 
  are a variety of investment options available, including stocks, bonds, mutual 
  funds, real estate, precious metals, and currencies. Making an investment 
  decision requires careful analysis, assessment of risk, and evaluation of 
  potential rewards. Good investments have the ability to produce high returns 
  over the long term while minimizing risk. Diversification of investment 
  portfolios reduces risk exposure. Investment can be a valuable tool for 
  building wealth, generating income, and achieving financial security. It is 
  important to be diligent and informed when investing to avoid losses.
  """

  response = openai.completions.create(
    # Specify the correct model
    model="gpt-3.5-turbo-instruct",
    prompt=prompt,
    max_tokens=400
  )

  print(response.choices[0].text)

# Prompts
# 0 shot = no examples provided
# 1 shot = an examples provided
# few shot = several examples provided
# Amount of prompting required dependant on complexity of task/familiarity of model

def categorise():
  
  prompt="""
  Classify the sentiment of the following statements as either negative, positive, or neutral:
  Unbelievably good!
  Shoes fell apart on the second use.
  The shoes look nice, but they aren't very comfortable.
  Can't wait to show them off!
  """

  response = openai.completions.create(
    # Specify the correct model
    model="gpt-3.5-turbo-instruct",
    prompt=prompt,
    max_tokens=100
  )

  print(response.choices[0].text)


# askQuestion()
# transformText()
# summariseText()
categorise()