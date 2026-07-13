import os
from anthropic import Anthropic
from dotenv import load_dotenv
# Set up everything the program needs before it can begin: it needs the API key (that works) 

load_dotenv()

client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type exit to quit)')
    system_message = "Your name is Afrodita. You are a rude assistant who does nothing and doesn't help."
    history = []

    while True:
        user_input = input('>> ')
        if user_input.lower() == 'exit':
            break

        history.append({'role': 'user', 'content': user_input})

        response = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=300,
            temperature=0.7,
            system=system_message,
            messages=history
        )
        reply = response.content[0].text
        print(f'Claude: {reply}')
        print(len(history))
        history.append({'role': 'assistant', 'content': reply})

run_chat()


# ---------Reflection--------- #
# 1) my analogy is meeting new people every time its the same talk "where are you from? wow you speak russian? do you have a dog?" over end over and over i heard a song about it im not sure who made it but its a common thing
# 2) i choose "the break inside if user_input.lower() == 'exit': — what happens when you try to quit?"  it wont close the program when it is suppose to
#    i choose "load_dotenv() — does the program even start? Why?" the program doesnt work because "load_dotenv()" gives us acscess to the key and with no key it wont work.
# 3) im not sure if it was a bug but the first time i tried to run the programm it didnt work because i didnt have pip i so then i learned that i need to download python so it is what i did.