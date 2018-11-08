
# coding: utf-8

# In[2]:


import json
from konlpy.tag import Kkma
from konlpy.utils import pprint
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC,LinearSVC,SVR
from sklearn.metrics import accuracy_score,mean_squared_error,roc_auc_score
import numpy as np
from sklearn.linear_model import LogisticRegression,SGDClassifier
import codecs

REVIEWS = "all_reviews"


f = codecs.open("" + REVIEWS + ".txt","r",encoding="utf-8").readlines()

for line in f[:1]:
    course = json.loads(line)
    review_text = course["review_text"].strip()
    first_word = review_text.split(" ")[0]
    # first_word = "안녕"
    print(first_word)
    print(first_word.encode("utf-8"))
    print(first_word)
    

