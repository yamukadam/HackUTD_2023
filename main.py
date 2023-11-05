import openai
import os
from dotenv import load_dotenv
from prompter import prompter
prompter()
load_dotenv()
api_key = os.environ['API_KEY']
openai.api_key = api_key
messages = [ {"role": "system", "content":  
              "You are a intelligent assistant."} ] 

companies = ["Exxon", "Saudi Aramco", "Shell"]
for company in companies:
    promptfile = open(f'{company}prompt.txt','r')
    message = promptfile.read()
    if message: 
        messages.append( 
            {"role": "user", "content": message}, 
        ) 
        chat = openai.ChatCompletion.create( 
            model="gpt-3.5-turbo-16k", messages=messages 
        ) 
    reply = chat.choices[0].message.content 
    print(f"ChatGPT: {reply}") 
    messages.append({"role": "assistant", "content": reply})
    print("")