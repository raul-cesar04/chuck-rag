### Implementação dos métodos de Chatbot

from Rag import Rag
import ollama

LANGUAGE_MODEL = 'hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF'

class Chatbot:
    def __init__(self):
        self.rag = Rag()
    
    def ask(self, question: str)->ollama.ChatResponse:
        retrieved_knowledge = self.rag.retrieve(question)

        instruction_prompt = f'''
            You are a joking chatbot.
            Your role is to humorousisly provide exaggerated Chuck Norris facts. Only get information from this context and not elsewhere:
            {'\n'.join([f'- {chunk}' for chunk, similiarity in retrieved_knowledge])}
        '''

        stream = ollama.chat(
            model=LANGUAGE_MODEL,
            messages=[
                {'role': 'system', 'content': instruction_prompt},
                {'role': 'user', 'content': question}
            ],

            stream=True
        )

        return stream