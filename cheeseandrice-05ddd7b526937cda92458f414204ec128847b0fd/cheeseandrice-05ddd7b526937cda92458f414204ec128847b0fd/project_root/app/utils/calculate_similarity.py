
from sklearn.metrics.pairwise import cosine_similarity
from app.utils.word_to_vector import vectorize_words

def calculate_similarity(matrix):
    similarity_matrix = cosine_similarity(matrix)
    return similarity_matrix

def get_top_similar_words(matrix, top_n=10):
    similarity_matrix = calculate_similarity(matrix)
    top_similar = []
    for idx, row in enumerate(similarity_matrix):
        top_indices = row.argsort()[-top_n:]
        top_similar.append((idx, top_indices))
    return top_similar
