# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 23:43:45 2016

@author: QingLing
"""

import pandas as pd

inputfile = 'vae.txt'
vae_raw = pd.read_csv(inputfile, encoding = 'utf-8', header = None,
                      error_bad_lines = False)

"""
清晰原始数据中重复的歌词
"""
l_raw = len(vae_raw)
outputfile = 'vae_clean.txt'
vae_cleaned = pd.DataFrame(vae_raw[0].unique())
l_cleaned = len(vae_cleaned)

deleted = (l_raw - l_cleaned)

vae_cleaned.to_csv(outputfile, index=False, header=False, encoding='utf-8')
