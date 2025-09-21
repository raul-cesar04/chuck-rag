### Main

from Chatbot import Chatbot

if __name__ == "__main__":
    chat = Chatbot()

    while True:
        question = input('This is Chuck Norris specialist chat. Ask anything, get any answer.\n')

        if(question.lower() == 'q'):
            print("No more chuck norris facts to ya.")
            break

        print('Chuck response:')
        for chunk in chat.ask(question):
            print(chunk['message']['content'], end='', flush=True)
        print('\n')

