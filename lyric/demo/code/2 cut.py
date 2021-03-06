# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 23:44:31 2016

@author: QingLing
"""

import pandas as pd
import jieba

inputfile = 'vae_clean.txt'
outputfile = 'vae_cut.txt'

data = pd.read_csv(inputfile, encoding='utf=8', header=None)
# define the cut function
mycut = lambda s: ' '.join(jieba.cut(s))
# Use space' ' to join the cutted results
data = data[0].apply(mycut)
# data #cutted prefect
data.to_csv(outputfile, index=False, header=False, encoding='utf-8')
