class CountVectorizer():
    def __init__(self):
        self.vocabulary={}

    def get_feature_names(self):
        return list(self.vocabulary.keys())
        
    def fit_transform(self, text):
        list_of_dictionaries=[]
        text_splited=text.copy()
        for isentence, sentence in enumerate(text_splited):
            sentence_splited = sentence.split()
            text_splited[isentence]=[words.lower() for words in sentence_splited]
        for sentence in text_splited:
            dictionary = {word: 0 for sentence in text_splited for word in sentence}
            self.vocabulary=dictionary
            for word in sentence:
                dictionary[word]+=1
            list_of_dictionaries.append(list(dictionary.values()))
        return list_of_dictionaries       


if __name__ == '__main__':
    corpus = [
 'Crock Pot Pasta Never boil pasta again',
 'Pasta Pomodoro Fresh ingredients Parmesan to taste'
]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
#Out: ['crock', 'pot', 'pasta', 'never', 'boil', 'again', 'pomodoro',
#_ 'fresh', 'ingredients', 'parmesan', 'to', 'taste']
    print(count_matrix)
#Out: [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
# [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]