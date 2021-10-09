from dotenv import load_dotenv 
from random import choice
from flask import Flask, request
import os 
import openai
from werkzeug.wrappers import response  

load_dotenv()
openai.api_key = os.environ.get('OPENAI_API_KEY')
completion = openai.Completion()

start_sequence = "\nbot:"
restart_sequence = "\n\nuser:"

session_prompt = "I am a highly intelligent question answering GOTbot. I can answer any question about Game of Thrones. Game of Thrones is an American fantasy drama television series created by David Benioff and D. B. Weiss for HBO. It is an adaptation of A Song of Ice and Fire, a series of fantasy novels by George R. R. Martin, the first of which is A Game of Thrones. The show was shot in the United Kingdom, Canada, Croatia, Iceland, Malta, Morocco, and Spain. It premiered on HBO in the United States on April 17, 2011, and concluded on May 19, 2019, with 73 episodes broadcast over eight seasons.\n\n\nbot: What is Game of Thrones?\nuser: Game of Thrones is an American fantasy drama television series created by David Benioff and D. B. Weiss.\n\nbot: What is A Song of Ice and Fire?\nuser: A Song of Ice and Fire is a series of fantasy novels published by George R.R Martin.\n\nbot: From which novel series was Game of Thrones was adopted?\nuser: A Song of Ice and Fire.\n\nbot: What is the square root of a banana?\nuser: Unknown\n\nbot: Where Game of Thrones was first premiered on?\nuser: Game of Thrones was first premiered on HBO in the USA.\n\nbot: Where was the Game of Thrones drama shot?\nuser: The show was shot in the United Kingdom, Canada, Croatia, Iceland, Malta, Morocco, and Spain.\n\nbot: How many episodes are there in Game of Thrones?\nuser: 73\n"

def ask(question, chat_log=None):
  prompt_text = f'{chat_log}{restart_sequence}:{question}{start_sequence}:'
  response = openai.Completion.create(
    engine="davinci",
    prompt = prompt_text,
    temperature=0.5,
    max_tokens=80,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.3,
    stop=["\n"]
  )
  story = response['choices'][0]['text']
  return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
      if chat_log is None:
          chat_log = session_prompt
      return f'{chat_log}{restart_sequence}:{question}{start_sequence}:'

