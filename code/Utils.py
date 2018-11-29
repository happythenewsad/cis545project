import spacy
import nltk
from nltk.corpus import stopwords
import functools as fn



class Utils:
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
    def stem_n_stop(text, spacy):
        wordlist = []
        tokens = spacy(text)
        for token in tokens:
            wordlist.append(token.text)
        return wordlist
        # nlp = spacy.load('en_core_web_sm')
        # doc = nlp(u'Apple is looking at buying U.K. startup for $1 billion')
