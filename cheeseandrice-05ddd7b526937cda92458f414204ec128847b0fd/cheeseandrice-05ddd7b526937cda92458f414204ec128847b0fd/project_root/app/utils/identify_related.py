from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def identify_related_text_elements(document_list):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(document_list)
    cosine_similarities = cosine_similarity(tfidf_matrix, tfidf_matrix)

    related_text_elements = {}
    for idx, doc in enumerate(document_list):
        similar_indices = cosine_similarities[idx].argsort()[:-100:-1]
        similar_items = [(cosine_similarities[idx][i], document_list[i]) for i in similar_indices]

        related_text_elements[doc] = similar_items[1:]

    return related_text_elements
