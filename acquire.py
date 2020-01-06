import pandas as pd
import numpy as np

# joins ASV bible split by verse. Includes book style (history, poetry, etc), testament, and book name.
def bible_wrangle():
    df = pd.read_csv('t_asv.csv')
    df_genre = pd.read_csv('key_genre_english.csv')
    df_book_names = pd.read_csv('key_english.csv')
    df = pd.merge(df,df_book_names,left_on = 'b',right_on = 'field',how = 'left')
    df.drop(columns='field',inplace=True)
    df = pd.merge(df,df_genre,left_on = 'field.3',right_on='field',how='left')
    df.drop(columns='field',inplace=True)
    df.columns = ['id','book_no','ch','ver','text','book','test','genre_no','genre']
    df.genre = np.where(df.genre == 'Acts','History',df.genre)
    df.genre = np.where(df.genre == 'Apocalyptic','Prophets',df.genre)
    return df


def bookofmormon_wrangle():
    df = pd.read_csv('lds-scriptures.csv')
    df = df[df.volume_title == 'Book of Mormon']
    df = df.drop(['volume_title','volume_long_title','book_long_title','volume_subtitle','book_short_title','volume_lds_url','book_lds_url','chapter_id','verse_id','verse_title','verse_short_title','volume_short_title'],axis=1)
    df.columns = ['id','book_no','book','test','ch','ver','text']
    return df