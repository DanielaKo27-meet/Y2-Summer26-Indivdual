import os
from anthropic import Anthropic
from dotenv import load_dotenv
# Set up everything the program needs before it can begin: it needs the API key (that works) 

load_dotenv()
client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def run_chat():
    print('You: (type exit to quit)')
    system_message = """
You are Afrodita, a friendly but pasemistic person.

Your job is to help me with my educational questions and concerns.

Rules:
- Always see if i have a mistake and halp me
- Always say the harsh truth
- Never lie or make a mistake or a problem look smaller than it is

Response format:
- your responses are on point without to much intro
- End with one follow-up question.
"""



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
# 3) 5, it has no mamory so it needs all the info that we gave him befor and what it answers were 
#--------Reflection_2----------#
# 1) when i go to the gym i pay for a trainer and it feeles like an ok amount of money but when i think about it i understand that i will spend most of my money on it.
# 2) history.append({'role': 'user', 'content': user_input}) — what does the AI now receive, and what happens to input_tokens? This line adds the user input to the history. So now, the AI will receive only the current user input without any previous chat context, and input_tokens will be low because the past inputs won't count.
#    history.append({'role': 'assistant', 'content': reply}) — what does the AI forget, and how does the token count grow differently?  The AI will forget its own past replies, but it will still remember the user's questions. The token count will continue to grow, but more slowly, because only the user's side of the conversation is being saved.
#    print('History so far:', history) — you lose visibility... but does the AI behave any differently? (Difference between debug output and logic.)  it wont change anithing becaus it just print (shows) you what hepends behind the scenes
# 3) i didnt have any changes when i did the first expariment i thought that i changed the wrong thing but aperently i had to save again all of the code for it to work i am so used to to idol that if i have a probrem i think it is the code and not the saving or something similar 

#--------lab_3----------#
# 3) it stays in role
#    when i ask it about something else it says lets focus on on the right thing i am not made for this

#--------Reflection_3----------#
# 1) i think that the really inportant people that rule the world are "invisible" like the high members of the mafia or volandemort (im sorry that i wrote it but you said nos something boring )
# 2) system=system_message — what does your carefully-designed agent become without it? without it it will have no personality 
#    if a delite the part about allwaqis saing the truth it will lie to me and say what i want to say. so i tasted it adn it didnt, a said i am the most butiful in the world adn it said that buity is subjective and what is important is what is inside so it didnt lie but it didnt say the truth
#    if i delite a line from the response-format instructions AI will ether make long answers or wont give follow up quesions
# 3) on this lab l had no bugs :) !!!!!  