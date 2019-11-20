# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 15:46:05 2019

@author: THIBAULT Sébastien
"""

from pymongo import MongoClient
# pprint library is used to make the output look more pretty




client = MongoClient('localhost', 27017)
db=client.Hackathon
collection = db.Total




docx = collection.find()

for doc in docx:
    if (type(doc['KM'])=="str" and doc['KM']!=''):
        doc['KM']= float(doc['KM'])
    if (type(doc['MIN'])=="str" and doc['MIN']!=''):
        doc['MIN']= float(doc['MIN'])
    collection.save(doc)
