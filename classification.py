from pathlib import Path
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

from nltk.tokenize import RegexpTokenizer  
from nltk.stem.snowball import SnowballStemmer
import wordcloud
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.feature_extraction.text import CountVectorizer  
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
df= pd.read_csv("phishing_site_urls.csv")
df.head()
df.isnull().sum()
df = df.drop_duplicates()
tokenizer = RegexpTokenizer(r'[A-Za-z]+')
df['text_tokenized'] = df.URL.map(lambda t: tokenizer.tokenize(t))
root_words = SnowballStemmer("english")
df['root_words'] = df['text_tokenized'].map(lambda l: [root_words.stem(word) for word in l])
df['text_sent'] = df['root_words'].map(lambda l: ' '.join(l))
bad_sites = df[df.Label == 'bad']
good_sites = df[df.Label == 'good']
c = CountVectorizer()
cv = c.fit_transform(df.text_sent)
Xtrain, Xtest, Ytrain, Ytest = train_test_split(cv, df.Label,test_size=0.3, random_state=42)
lr = LogisticRegression(max_iter=507197)
lr.fit(Xtrain,Ytrain)
lr.score(Xtest,Ytest)
ypred = lr.predict(Xtest)
Xtrain, Xtest, Ytrain, Ytest = train_test_split(df.URL, df.Label,test_size=0.3, random_state=42)
pipeline_ls = make_pipeline(CountVectorizer(tokenizer = RegexpTokenizer(r'[A-Za-z]+').tokenize,stop_words='english'), LogisticRegression(max_iter=507197))
pipeline_ls.fit(Xtrain,Ytrain)
phish = [ ]
n = int(input("Enter number of elements : "))
 
for i in range(0, n):
    ele = [input()]
    phish.append(ele)
    result1 = pipeline_ls.predict(ele)
    if(result1=="good"):
        print("Legitimate Site")
    else:
        print("Phishing Site")

# Save model to disk under models/
models_dir = Path(__file__).resolve().parent / 'models'
models_dir.mkdir(parents=True, exist_ok=True)
filename = models_dir / 'model.sav'
joblib.dump(pipeline_ls, filename)

    