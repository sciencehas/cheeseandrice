from sentence_transformers import SentenceTransformer

class Transformer:
    def __init__(self):
        self.model = SentenceTransformer('stsb-mpnet-base-v2')

    def encode(self, documents):
        return self.model.encode(documents)
