import pandas as pd

data_train = pd.read_csv("train.txt",delimiter=";",names=["text","label"])
#data_test = pd.read_csv("train.txt",delimiter=";",names=["text","label"])
print(data_train.info())
print(data_train["label"].value_counts())

def encoder_c(data):
    data.replace(to_replace = "joy",value = 1,inplace = True)
    data.replace(to_replace = "sadnesss",value = 0,inplace = True)
    data.replace(to_replace = "anger",value = 0,inplace = True)
    data.replace(to_replace = "fear",value = 0,inplace = True)
    data.replace(to_replace = "love",value = 1,inplace = True)
    data.replace(to_replace = "serprise",value = 1,inplace = True)
encoder_c(data_train["label"])

import re
import nltk 
nltk.download("stopwords")
nltk.download("wordnet")
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

lm = WordNetLemmatizer()
def text_transformation(data):
    corpus = []
    for sentence in data:
        new_item = re.sub('[^a-zA-Z]',' ',str(sentence))
        new_item = new_item.lower()    
        new_item = new_item.split()
        new_item = [lm.lemmatize(word) for word in new_item if word not in set(stopwords.words("english"))]
        corpus.append(" ".join(str(x)for x in new_item))
    return corpus

corpus = text_transformation(data_train["text"])
print(corpus[0])