# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

inputfile = 'Jay.txt'
jay_raw = pd.read_csv(inputfile, encoding = 'utf-8', header = None,
                      error_bad_lines = False)
                      
"""
清洗原始数据重复
"""

l_raw  = len(jay_raw)

outputfile = 'jay_clean.txt'
jay_cleaned = pd.DataFrame(jay_raw[0].unique())

l_cleaned = len(jay_cleaned)

deleted = (l_raw - l_cleaned)

jay_cleaned.to_csv(outputfile, index=False, header=False, encoding='utf-8')
