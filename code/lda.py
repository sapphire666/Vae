
# coding: utf-8

# In[1]:

import pandas as pd
from gensim import corpora, models
inputfile  = '../raw/cutted.txt'
stop = '../raw/stop.txt'
output = '../raw/theme.txt'


# In[2]:

data = pd.read_csv(inputfile, encoding='utf-8', header=None,engine='python')
stop = pd.read_csv(stop, encoding='utf-8', header=None, sep = 'Ubuntu',engine='python')
stop = [' ', ''] + list(stop[0])
data[1:4]


# In[3]:

stop[1:4]


# In[5]:

data[1] = data[0].apply(lambda x: [i for i in x if i not in stop]) # 逐词判断是否挺用
data[1][0:5]


# In[6]:

data_dict = corpora.Dictionary(data[1])# dictionary
print data_dict


# In[13]:

data_corpus = [data_dict.doc2bow(i) for i in data[1]] # corpus
print data_corpus[0:5]


# In[14]:

data_lda = models.LdaModel(data_corpus, num_topics=3, id2word=data_dict)
print data_lda.print_topic(0)


# In[15]:

print data_lda.print_topic(1)


# In[16]:

print data_lda.print_topic(2)


# In[ ]:



