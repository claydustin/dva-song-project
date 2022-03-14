import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# remove speciall leading and trailing characters
def remove_characters(row):
    return [x.strip(",.!#[]/'") for x in row]

# remove stop words from each list in each row
## use set to remove duplicate words
def remove_stop(row, stop):
    return list(set([x.lower() for x in row if x.lower() not in stop]))

def get_tfidf_dict(str_col: pd.Series, ngram: str = "unigram"):
    """
    input:  str_col - pd.Series -> a column of strings
            ngram   - String    -> ngram option for bigrams
    output: dict      -> dictionary following (key,value) ==> ("<word>", <tfidf-score>)
            ex. {'this': 0.38408524091481483,
                'the': 0.38408524091481483,
                 'second': 0.5386476208856763}
    """
    if ngram == "bigram":
        ngram_range = (2, 2)
    else:
        ngram_range = (1, 1)
    list_col = str_col.tolist()
    tfidf = TfidfVectorizer(stop_words="english", ngram_range=ngram_range).fit(list_col)
    feature_names = tfidf.get_feature_names_out()

    tfidf_matrix = tfidf.transform(list_col)
    tfidf_dict = {}

    for i in range(tfidf_matrix.shape[0]):
        feature_index = tfidf_matrix[i, :].nonzero()[1]
        tfidf_scores = zip([feature_names[j] for j in feature_index], [tfidf_matrix[i, x] for x in feature_index])
        tfidf_dict.update(dict(tfidf_scores))

    return tfidf_dict

def one_hot_encoding(str_col: pd.Series, ngram: str = "unigram"):
    """
    input:  str_col - pd.Series -> a column of strings
            ngram   - String    -> ngram option for bigrams
    output: tuple     -> np.SparseMatrix with one-hot-encoding representation, tokenized and joined list of strings
            ex. ([[1,0,1], [0,0,1]], ["red,blue","blue"])

    vectorizer.inverse_transform() returns a tokenized np.array of tokens.
    ex.  returns -> ['document,first,is,the,this',
             'document,is,second,the,this',
             'and,is,one,the,third,this',
             'document,first,is,the,this']
    """
    if ngram == "bigram":
        ngram_range = (2, 2)
    else:
        ngram_range = (1, 1)

    list_col = str_col.tolist()
    # COMMENT: could add token_pattern = r"\(.*?\)|([^\W_]+[^\s-]*)"
    # COMMENT: sklearn.CountVectorizer -> Removes stop words and punctuation and represents words as list of counts
    vectorizer = CountVectorizer(stop_words="english", binary=True, ngram_range=ngram_range).fit(list_col)

    x = vectorizer.transform(list_col)
    tokenized = [",".join(token_array) for token_array in vectorizer.inverse_transform(x.toarray())]

    return x, tokenized


def find_lyric_similarity(lyric1_col: pd.Series, lyric2_col: pd.Series):
    """
    input:  lyric1_col - pd.Series -> a column of lyrics
            lyric2_col - pd.Series -> a column of lyrics to compare to
    output: list      -> returns a list of scalars representing lyric similarity
            ex. ([0.9993, 0.112]) results 0-1 with 1 being most similar

    """
    lyrics = pd.concat(
        [lyric1_col.reset_index(drop=True), lyric2_col.reset_index(drop=True)],
        ignore_index=True)
    encoded_lyrics = one_hot_encoding(lyrics)[0].toarray()

    lyrics_1 = encoded_lyrics[0:len(lyric1_col)]
    lyrics_2 = encoded_lyrics[len(lyric1_col):]

    cosine_scores = []
    for i in range(lyrics_1.shape[0]):
        score = cosine_similarity([lyrics_1[i]], [lyrics_2[i]])[0]
        cosine_scores.append(score)

    return cosine_scores
