# Imports
import pickle
from tqdm import tqdm
from textblob import TextBlob
import pandas as pd
import numpy as np

# Get all data from df
with open('data/fire_clean.pickle', 'rb') as read_file:
    df = pickle.load(read_file)

# Split by fire
kincade_pre_split = df.loc[df['fire'] == 'kincade', :].reset_index(drop = True)
kincade_split = kincade_pre_split.loc[10000:,:].reset_index(drop = True)
nca_pre_split = df.loc[df['fire'] == 'nca_2017', :].reset_index(drop = True)
nca_split = nca_pre_split.loc[10000:,:].reset_index(drop=True)
camp_pre_split = df.loc[df['fire'] == 'camp', :].reset_index(drop = True)
camp_split = camp_pre_split.loc[5000:,:].reset_index(drop=True)
shasta_pre_split = df.loc[df['fire'] == 'shasta_2018', :].reset_index(drop = True)
shasta_split = shasta_pre_split.loc[5000:,:].reset_index(drop=True)
sb_pre_split = df.loc[df['fire'] == 'sb_2017', :].reset_index(drop = True)
sb_split = sb_pre_split.loc[5000:,:].reset_index(drop=True)
all_splits = [shasta_split, sb_split, kincade_split, nca_split]

# Function - get senitment and language information
def get_sentiment(df, file_name):
    sentiment_lst = []
    sent_num = []
    language = []
    spell_trans_lst = []
    for i,tweet in tqdm(enumerate(df['text'])):
        if len(tweet) <= 3:
            df = df.drop(i)
        else:
            ana = TextBlob(tweet)
            sent_num.append(float(ana.sentiment.polarity))
            lang = str(ana.detect_language())
            language.append(lang)
            if lang != 'en':
                try:
                    translate = str(ana.translate(from_lang=lang, to ='en'))
                    new_analysis = TextBlob(translate)
                    spell_trans = str(new_analysis.correct())
                except:
                    spell_trans = np.nan
            else:
                spell_trans = str(ana.correct())
            spell_trans_lst.append(spell_trans)
            if ana.sentiment.polarity > 0:
                sentiment = 'positive'
            elif ana.sentiment.polarity == 0:
                sentiment = 'neutral'
            else:
                sentiment = 'negative'
            sentiment_lst.append(sentiment)
    df = df.reset_index(drop = True)
    if len(sentiment_lst) != len(df['text']):
        new_df = pd.DataFrame({'sentiment':sentiment_lst, 'sent_num':sent_num, 'language':language, 'spell_trans':spell_trans_lst})
        with open('data/not_equal.pickle', 'wb') as to_write:
            pickle.dump(new_df, to_write)
    else:
        df['sentiment'] = sentiment_lst
        df['sent_num'] = sent_num
        df['language'] = language
        df['spell_trans'] = spell_trans_lst
        with open('data/{}.pickle'.format(file_name), 'wb') as to_write:
            pickle.dump(df, to_write)

# Loop through df chunks by fire
for fire in all_splits:
    ind = 5001
    chunk = fire.loc[0:ind,:].reset_index(drop = True)
    filename = '{}_{}'.format(chunk.loc[0,'fire'],ind)
    print(filename)
    get_sentiment(chunk, filename)
