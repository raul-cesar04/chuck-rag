### Implementação dos métodos de RAG, para retrieving 
from Vector import Database, EMBEDDING_MODEL
from Utils import cosine_similiarity

import ollama

DATA_FILE_LOCATION = 'data/chuck_facts.txt'

class Rag:
    def __init__(self):
        self.dataset = []
        self.database = Database() # Placeholder
        self.load_dataset()
    
    def load_dataset(self):
        print('[RAG]->Loading dataset...')

        with open(DATA_FILE_LOCATION) as file:
            self.dataset = file.readlines()
            print(f'[RAG]->Loaded {len(self.dataset)} entries.')
        
        ## Save to database (Placeholder)
        for i, chunk in enumerate(self.dataset):
            self.database.add_chunk_to_database(chunk)
            print(f'[RAG]->Added chunk {i+1}/{len(self.dataset)} to the database.')
    
    def retrieve(self, query: str, top_n: int = 3)->list:
        query_embedding = ollama.embed(model=EMBEDDING_MODEL, input=query)['embeddings'][0]

        similiarities = []

        for chunk, embedding in self.database.database:
            similiarity = cosine_similiarity(query_embedding, embedding)
            similiarities.append((chunk, similiarity))

        similiarities.sort(key=lambda x:x[1], reverse=True)

        return similiarities[:top_n]