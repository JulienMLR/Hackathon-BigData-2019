# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:48:12 2019

@author: THIBAULT Sébastien
"""

import numpy as np
import pandas as pd
import io
from IPython.display import clear_output
from matplotlib import pyplot as plt

f = open('ressources\\Traite\\Finished\\Total3.csv',encoding="utf-16")

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
df = df.dropna()

L1 = df.pop('PAYS')



#df.pop('KM')


y = df.pop('COMMENT_NOUS_AVEZ_VOUS_DECOUVERT')


for i in range(len(y)):
    if (y.values[i].endswith('visite')):
        y.values[i] = "Xeme_Visite"

classes = list(dict.fromkeys(y))
print(classes)

#print(y)
#display(df)



from sklearn import tree
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree.export import export_text

enc = OneHotEncoder(handle_unknown='ignore',sparse=False)
L1 = L1.values.reshape(-1,1)
enc.fit(L1)
L1bis = enc.transform(L1)
#print(L1bis)
L11 = []
for i in L1:
  L11 = L11+ [ ""+i[0]+""]

#print(L11)
L1list = list(dict.fromkeys(L11))
print(L1list)

df2 = np.append(L1bis,df,axis=1)


clf = tree.DecisionTreeClassifier(max_depth=4)
clf = clf.fit(df2, y)
tree.plot_tree(clf.fit(df2,y),feature_names=L1list+["KM"]) 

print(export_text(clf,feature_names=L1list+["KM"]))



dotfile = open("dt.dot", 'w')
tree.export_graphviz(clf, out_file=dotfile,feature_names=L1list+["KM"],class_names = clf.classes_,impurity=False)
dotfile.close()

#######################

clf2 = tree.DecisionTreeClassifier(max_depth=4)
clf2 = clf2.fit(df, y)
tree.plot_tree(clf2.fit(df,y),feature_names=["KM"]) 

print(export_text(clf2))



dotfile = open("dt.dot", 'w')
tree.export_graphviz(clf2, out_file=dotfile,feature_names=["KM"],class_names = clf2.classes_,impurity=False)
dotfile.close()

#######################

clf3 = tree.DecisionTreeClassifier(max_depth=4)
clf3 = clf3.fit(L1bis, y)
tree.plot_tree(clf3.fit(L1bis,y),feature_names=L1list) 

print(export_text(clf3))



dotfile = open("dt.dot", 'w')
tree.export_graphviz(clf3, out_file=dotfile,feature_names=L1list,class_names = clf3.classes_,impurity=False)
dotfile.close()

#######################

y4 = y
y4.values = []
df4 = df2
df4.values = []

for j in range(len(y)):
    if(y.values[j]!="Xeme_Visite"):
        y4.values += y.values[j]
        df4.values += df.values[j]

clf4 = tree.DecisionTreeClassifier(max_depth=4)
clf4 = clf4.fit(df2, y)
tree.plot_tree(clf4.fit(df2,y),feature_names=L1list+["KM"]) 

print(export_text(clf4,feature_names=L1list+["KM"]))



dotfile = open("dt.dot", 'w')
tree.export_graphviz(clf4, out_file=dotfile,feature_names=L1list+["KM"],class_names = clf4.classes_,impurity=False)
dotfile.close()

