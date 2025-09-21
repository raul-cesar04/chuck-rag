### Implementação dos métodos do Vector Database

import ollama

EMBEDDING_MODEL = 'hf.co/CompendiumLabs/bge-base-en-v1.5-gguf'

## Placeholder in memory database
class Database:
    def __init__(self):
        self.database = []

    def add_chunk_to_database(self, chunk: str)->None:
        embedding = ollama.embed(model=EMBEDDING_MODEL, input=chunk)['embeddings'][0]
        self.database.append((chunk, embedding))