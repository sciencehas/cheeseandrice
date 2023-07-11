from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords

def create_word_to_vector_instances(cleaned_data):
    vectorizer = CountVectorizer(stop_words=stopwords.words('english'))
    word_vector = vectorizer.fit_transform(cleaned_data)
    return word_vector.toarray(), vectorizer.get_feature_names_out()
