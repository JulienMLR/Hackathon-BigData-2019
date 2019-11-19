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
