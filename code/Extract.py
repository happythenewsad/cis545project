import spacy
import pandas as pd

class Extract:
# vectorizer = DictVectorizer()
    # features = []

    # raw_text_col = 0
    # LABEL_COL = -1

    @staticmethod
    def punc_feats(txt):
        punc_dict = {}
        punc_data = {'colon':':', 'semicolon': ';', 'lparen':'(',
                    'ellipse': '...', 'quote': "'", 'bang': "!"}
        
        for key in punc_data.keys():
            punc_dict[key+'_count'] = txt.count(punc_data[key])

        return punc_dict

    @staticmethod
    def feats(txt, spacy, seq_up_to=None, feat_whitelist=None):
        feature_dict = {}
        if feat_whitelist != None:
            for f in feat_whitelist:
                feature_dict[f] = 0
                
        pos_dict = {'NOUN_count': 0, 'ADV_count': 0, 'VERB_count': 0, 
                    'ADJ_count': 0, 'adv_verb_ratio': 0, 'adj_noun_ratio': 0
                   }
    
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
          
        if seq_up_to:
            pos_sequence = pos_sequence[:seq_up_to] # shortening the num of features to reasonable
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
        feature_dict.update(Extract.punc_feats(txt))

        # removes features not in whitelist
        if feat_whitelist != None:
            for key in list(feature_dict.keys()):
                if not key in feat_whitelist:
                    feature_dict.pop(key, None)

        return feature_dict

    @staticmethod
    def gram_feats(text_series, feat_whitelist=None, seq_up_to=None):
        spacy_model = spacy.load('en_core_web_sm')
        features = []
        for _,text in enumerate(text_series):
            features.append(Extract.feats(text, spacy_model, seq_up_to, feat_whitelist))
        gram_feats_df = pd.DataFrame(features)
        return gram_feats_df


    # for row_idx,_ in enumerate(raw):
    #     features.append(extract_feats(row_idx, raw))

    # X = vectorizer.fit_transform(features)

