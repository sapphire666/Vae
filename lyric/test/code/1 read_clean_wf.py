# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

inputfile = 'wangfeng.txt'
data_raw = pd.read_csv(inputfile, encoding = 'utf-8', header = None,
                      error_bad_lines = False)
            
            
l_raw = len(data_raw)

outputfile = 'wangfeng_clean.txt'
data_cleaned = pd.DataFrame(data_raw[0].unique())

l_cleaned = len(data_cleaned)

deleted = (l_raw - l_cleaned)

data_cleaned.to_csv(outputfile, index=False, header=False, encoding='utf-8')            