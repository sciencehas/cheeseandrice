```python
from sklearn.metrics.pairwise import cosine_similarity
from .calculate_similarity import calculate_similarity
from .merge_data import merge_data

def similarity_analysis(matrix, threshold=0.8):
    """
    Function to perform similarity analysis on the matrix.
    It iterates through the matrix to find all related content that are at least x% similar,
    where x is defined arbitrary again.
    """
    similar_content = []
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            similarity = calculate_similarity(matrix[i], matrix[j])
            if similarity >= threshold:
                similar_content.append((i, j, similarity))
    return similar_content

def find_similar_documents(documents, threshold=0.8):
    """
    Function to find similar documents in the given list of documents.
    It uses the similarity_analysis function to find similar content.
    """
    matrix = merge_data(documents)
    similar_content = similarity_analysis(matrix, threshold)
    similar_documents = []
    for i, j, similarity in similar_content:
        if similarity >= threshold:
            similar_documents.append((documents[i], documents[j], similarity))
    return similar_documents
```