import openai
from translate import Translator
import os

openai.api_key = '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'


def get_api_response(prompt: str) -> str | None:
    text: str | None = None

    try:
        response: dict = openai.Completion.create(
            model='text-davinci-003',
            prompt=prompt,
            temperature=0.9,
            max_tokens=2400,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=[' Human:', ' AI:']
        )

        choices: dict = response.get('choices')[0]
        text = choices.get('text')

    except Exception as e:
        print('ERROR:', e)

    return text


def update_list(message: str, pl: list[str]):
    pl.append(message)


def create_prompt(message: str, pl: list[str]) -> str:
    p_message: str = f'\nHuman: {message}'
    update_list(p_message, pl)
    prompt: str = ''.join(pl)
    return prompt


def get_bot_response(message: str, pl: list[str]) -> str:
    prompt: str = create_prompt(message, pl)
    bot_response: str = get_api_response(prompt)

    if bot_response:
        update_list(bot_response, pl)
        pos: int = bot_response.find('\nAI: ')
        bot_response = bot_response[pos + 5:]
    else:
        bot_response = 'Something went wrong...'

    return bot_response


def main():
    prompt_list: list[str] = ['You\'re an AI and you respond to everything I say, your name is Friday and you just call me sir',
                              '\nHuman: What time is it?',
                              '\nAI: Hello Sir, it is now 12:00']

    while True:


        
        

        user_input: str = input('You: ')
        response: str = get_bot_response(user_input, prompt_list)
        if 'Crie uma lista' in user_input:
            with open('list_file.txt','w') as f:
                f.write(response)
                os.startfile('D:\Projetos\Friday - IA\list_file.txt')
        print(f'Bot: {response}')


        


if __name__ == '__main__':

    main()