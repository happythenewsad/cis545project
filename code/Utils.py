import spacy
import nltk
from nltk.corpus import stopwords
import functools as fn
import pickle
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction import DictVectorizer


class Utils:
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





    # vectorizer = DictVectorizer()
    # features = []

    # raw_text_col = 0
    # LABEL_COL = -1

    @staticmethod
    def extract_punc_feats(txt):
        punc_dict = {}
        punc_data = {'colon':':', 'semicolon': ';', 'lparen':'(',
                    'ellipse': '...', 'quote': "'", 'bang': "!"}
        
        for key in punc_data.keys():
            punc_dict[key+'_count'] = txt.count(punc_data[key])

        return punc_dict

    @staticmethod
    # can just pass in row rather than whole df + index
    def extract_feats(row_idx, raw, spacy):
        feature_dict = {}
        pos_dict = {'NOUN_count': 0, 'ADV_count': 0, 'VERB_count': 0, 
                    'ADJ_count': 0, 'adv_verb_ratio': 0, 'adj_noun_ratio': 0
                   }
        txt = str(raw[row_idx][raw_text_col])
        
        feature_dict['sent_len'] = len(txt)
        
        try:
            doc = spacy(txt)
        except IndexError as e:
            print(e)
            print("offending message [{}], len: {}, row idx: {}".format(txt, len(txt), row_idx))
            doc = []

        pos_sequence = []
        for token in doc:
            pos = token.pos_
            pos_dict[pos+'_count'] = pos_dict.get(pos+'_count', 0) + 1
            if pos == 'NOUN' or pos == 'VERB' or pos == 'CCONJ':
                pos_sequence.append(pos)
                
        pos_sequence = pos_sequence[:7] # shortening the num of features to reasonable
        pos_sequence_name = "_".join(pos_sequence)
        feature_dict[pos_sequence_name] = 1


        if pos_dict['NOUN_count'] == 0 or pos_dict['ADJ_count'] == 0:
            pos_dict['adj_noun_ratio'] = 0
        else:
            pos_dict['adj_noun_ratio'] = pos_dict['NOUN_count'] / pos_dict['ADJ_count'] 

        if pos_dict['VERB_count'] == 0 or pos_dict['ADV_count'] == 0:
            pos_dict['adv_verb_ratio'] = 0
        else:
            pos_dict['adv_verb_ratio'] = pos_dict['VERB_count'] / pos_dict['ADV_count'] 
            
        feature_dict.update(pos_dict)
        feature_dict.update(extract_punc_feats(txt))
        
        if row_idx % 1000 == 0:
            print("{} gold: {} {}\n".format(txt, raw[row_idx][LABEL_COL], feature_dict) )
         
        return feature_dict


    # for row_idx,_ in enumerate(raw):
    #     features.append(extract_feats(row_idx, raw))

    # X = vectorizer.fit_transform(features)


