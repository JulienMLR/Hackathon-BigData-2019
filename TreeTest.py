# -*- coding: utf-8 -*-
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

#dotfile = open("dt.dot", 'w')
#tree.export_graphviz(clf, out_file=dotfile, feature_names=df.columns)
#dotfile.close()




#################################################

import numpy as np
import pandas as pd
import io
from IPython.display import clear_output
from matplotlib import pyplot as plt

import requests
url = 'https://raw.githubusercontent.com/SergeGuillemart/Hackathon-BigData-2019/master/ressources/Traite/Finished/Total3.csv'
myfile = requests.get(url)
open('./test.csv', 'wb').write(myfile.content)
f = open('./test.csv',encoding="utf-16")
df = pd.read_csv(f,sep=',')

df.pop('DATE')
df.pop('MIN')
df.pop('CODE_POSTAL')
df.pop('LOCALITE')


df.pop('LANGUE2')
df.pop('LANGUE3')
df.pop('LANGUE4')
df.pop('LANGUE5')

df.pop('PAYS')
df = df.dropna()
#df.pop('KM')
L1 = df.pop('LANGUE1')
y = df.pop('COMMENT_NOUS_AVEZ_VOUS_DECOUVERT')

print(y)
display(df)




from sklearn import tree
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree.export import export_text

enc = OneHotEncoder(handle_unknown='ignore',sparse=True)
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


clf = tree.DecisionTreeClassifier(max_depth=5)
clf = clf.fit(L1bis, y)
tree.plot_tree(clf.fit(L1bis,y),feature_names=L1list) 

print(export_text(clf))
