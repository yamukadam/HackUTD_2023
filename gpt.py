import openai
openai.api_key = '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'
messages = [ {"role": "system", "content":  
              "You are a intelligent assistant."} ] 
while True: 
    input_file = open("article.txt","r")
    my_list = []
    for line in input_file:
        my_list.append(line)
    my_string = "".join(my_list)
    message = "read the following article: " + my_string + ". how do you think this will affect the oil market?"
    if message: 
        messages.append( 
            {"role": "user", "content": message}, 
        ) 
        chat = openai.ChatCompletion.create( 
            model="gpt-3.5-turbo", messages=messages 
        ) 
    reply = chat.choices[0].message.content 
    print(f"ChatGPT: {reply}") 
    messages.append({"role": "assistant", "content": reply})