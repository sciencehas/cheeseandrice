```python
import numpy as np
from .word_to_vector import WordToVector

class MergeData:
    def __init__(self):
        self.word_to_vector = WordToVector()

    def merge_data(self, cleaned_data):
        vectors = []
        for data in cleaned_data:
            vector = self.word_to_vector.create_vector(data)
            vectors.append(vector)
        matrix = np.vstack(vectors)
        return matrix
```