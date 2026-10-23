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
#issue
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

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(ngram_range=(1,2))
X = cv.fit_transform(corpus)
y = data_train["label"]
#hyper - parameter - tuning
parameters = {
    "max_features" : ("auto","sqrt"),
    "n_etimators" : [500,1000,1500],
    "max_depth" : [5,10,None],
    "min_samples_leaf" : [1,2,5,10],
    "bootstrap" : [True,False]
}
from sklearn.model_selection import GridSearchCV 
from sklearn.ensemble import RandomForestClassifier
gscv = GridSearchCV(RandomForestClassifier(),parameters, cv = 5, return_train_score=True, n_jobs=-1 )
print(gscv.best_params_)
rfc = RandomForestClassifier(max_features = gscv.best_params_["max_features"],
                             n_etimators = gscv.best_params_["n_etimators"],
                             max_depth = gscv.best_params_["max_depth"],
                             min_samples_leaf = gscv.best_params_["min_samples_leaf"],
                             bootstrap = gscv.best_params_["bootstrap"],)
rfc.fit(X,y)

