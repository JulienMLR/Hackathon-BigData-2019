# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 15:10:34 2019

@author: THIBAULT Sébastien
"""

import numpy as np
import pandas as pd
from IPython.display import clear_output
from matplotlib import pyplot as plt

df = pd.read_csv('ressources/Traite/Finished/InfoVis2017.csv')
y = dftrain.pop('COMMENT_NOUS_AVEZ_VOUS_DECOUVERT')


-------------------- COLLAB

import numpy as np
import pandas as pd
import io
from IPython.display import clear_output
from matplotlib import pyplot as plt
import requests

url = 'https://raw.githubusercontent.com/SergeGuillemart/Hackathon-BigData-2019/master/ressources/Traite/Finished/InfoVis2017.csv'

myfile = requests.get(url)

open('./test.csv', 'wb').write(myfile.content)

f = open('./test.csv')


df = pd.read_csv(f,sep=',')

df.pop('DATE')
df.pop('MIN')
df.pop('CODE')
df.pop('LOCALITE')
df = df.dropna()
y = df.pop('COMMENT_NOUS_AVEZ_VOUS_DECOUVERT')


from sklearn import tree
from sklearn.preprocessing import OneHotEncoder

enc = OneHotEncoder(handle_unknown='ignore')
enc.fit(df)
print(enc.transform(df).toarray())
#display(df)

#clf = tree.DecisionTreeClassifier()
#clf = clf.fit(df, y)
#tree.plot_tree(clf.fit(df,y)) 


