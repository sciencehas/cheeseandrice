from collections import Counter

def rank_and_sort(bag_of_words):
    word_counts = Counter(bag_of_words)
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_words
