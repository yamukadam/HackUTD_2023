import openai
import os
from dotenv import load_dotenv
from prompter import prompter
load_dotenv()
api_key = os.environ['API_KEY']
openai.api_key = api_key
def run(ind):
    prompter(ind)
    messages = [ {"role": "system", "content":  
                "You are a intelligent assistant."} ] 
    companies = ["Exxon", "Saudi Aramco", "Shell"]
    company = companies[ind]
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
    return reply
output_txt2 = run(2)
output_file2 = open("shell_output.txt", "w")
output_file2.write(output_txt2)

output_txt1 = run(1)
output_file1 = open("aramco_output.txt", "w")
output_file1.write(output_txt1)

output_txt0 = run(0)
output_file0 = open("exxon_output.txt", "w")
output_file0.write(output_txt0)


