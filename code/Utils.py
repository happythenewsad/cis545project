import spacy
import nltk
from nltk.corpus import stopwords
import functools as fn
from nltk.stem.porter import PorterStemmer


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
    def stem_n_stop(text, spacy, stemmer):
        wordlist = []
        tokens = spacy(text)
        for token in tokens:
            wordlist.append(stemmer.stem(token.text))
        return wordlist



