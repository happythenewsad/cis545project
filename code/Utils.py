import spacy
import nltk
from nltk.corpus import stopwords
import functools as fn
import pickle
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction import DictVectorizer


class Utils:

    @staticmethod
    def tokenize(sentence):
        return sentence.split(' ')

    @staticmethod
    def build_lexicon(sents):
        lex = {}
        for sent in sents:
            words = Utils.tokenize(sent)
            for word in words:
                word = word.lower()
                if word in lex:
                    lex[word] = lex[word] + 1
                else:
                    lex[word] = 1
        return sorted(lex.items(), key=lambda x: x[1], reverse=True)

    @staticmethod
    def persist_obj(X, name):
        with open(name, 'wb') as f:
            pickle.dump(X, f, pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def check_for_nulls(df):
        nulls_dict = {}
        for col in df.columns:
            mask = df[col].isnull()
            counter = 0
            for cell in mask:
                if cell == True:
                    counter = counter + 1
            nulls_dict[col] = counter
        return nulls_dict
            
    @staticmethod
    def stem_n_stop(text, spacy, stemmer):
        wordlist = []
        tokens = spacy(text)
        for token in tokens:
            wordlist.append(stemmer.stem(token.text))
        return wordlist





    
