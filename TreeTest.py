# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import io
from IPython.display import clear_output
from matplotlib import pyplot as plt

f = open(here +'\\ressources\\Traite\\Finished\\Total3.csv',encoding="utf-16")

df = pd.read_csv(f)

df.pop('DATE')
df.pop('MIN')
df.pop('CODE_POSTAL')
df.pop('LOCALITE')

df.pop('LANGUE1')
df.pop('LANGUE2')
df.pop('LANGUE3')
df.pop('LANGUE4')
df.pop('LANGUE5')
#df.pop('KM')
df.pop('PAYS')
df = df.dropna()
y = df.pop('COMMENT_NOUS_AVEZ_VOUS_DECOUVERT')

print(y)
display(df)


from sklearn import tree
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree.export import export_text

#enc = OneHotEncoder(handle_unknown='ignore')
#display(df)

clf = tree.DecisionTreeClassifier(max_depth=5)
clf = clf.fit(df, y)
tree.plot_tree(clf.fit(df,y)) 

print(export_text(clf))