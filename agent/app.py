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
        print('History:', history)
        response = client.messages.create(
            model='claude-haiku-4-5-20251001',
            max_tokens=300,
            temperature=1,
            system=system_message,
            messages=history
        )
        reply = response.content[0].text
     #   print(response)
        print(f'Claude: {reply}')
      # print(len(history)//2)
        history.append({'role': 'assistant', 'content': reply})

run_chat()


# ---------Reflection--------- #
# 1) my analogy is meeting new people every time its the same talk "where are you from? wow you speak russian? do you have a dog?" over end over and over i heard a song about it im not sure who made it but its a common thing
# 2) i choose "the break inside if user_input.lower() == 'exit': — what happens when you try to quit?"  it wont close the program when it is suppose to
#    i choose "load_dotenv() — does the program even start? Why?" the program doesnt work because "load_dotenv()" gives us acscess to the key and with no key it wont work.
# 3) im not sure if it was a bug but the first time i tried to run the programm it didnt work because i didnt have pip i so then i learned that i need to download python so it is what i did.


#-------------lab_2------------#
# 1) usage.input_tokens means the count of how much tokens the user has used for questions and usage.output_tokens means how much answers the agent sent back
# 2) if i change max_tokens to 50 clouds cuts its answers and i dint see the end of the messege.
#    if i change temperature to 0 i dont really see a difference even though i know it is supposed to make answers more random
#    tempruture controles how random the answer will be
# 3) 
#--------Reflection_2----------#
# 1) when i go to the gym i pay for a trainer and it feeles like an ok amount of money but when i think about it i understand that i will spend most of my money on it.
# 2) history.append({'role': 'user', 'content': user_input}) — what does the AI now receive, and what happens to input_tokens?
#    history.append({'role': 'assistant', 'content': reply}) — what does the AI forget, and how does the token count grow differently?
#    print('History so far:', history) — you lose visibility... but does the AI behave any differently? (Difference between debug output and logic.)
