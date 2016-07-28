# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 10:06:16 2016

@author: QingLing
"""

import pandas as pd
from gensim import corpora,models

inputfile = 'wangfeng_cut.txt'
stoplist = 'stoplist.txt'

data = pd.read_csv(inputfile,encoding = 'utf-8', header =None)
stop = pd.read_csv(stoplist, encoding = 'utf-8', header = None, sep = 'tipdm',engine='python')
stop = [' ', '','里', '中','做','已','想'] + list(stop[0])

data[1] = data[0].apply(lambda s: s.split(' ')) #定义一个分割函数，然后用apply广播
data[2] = data[1].apply(lambda x: [i for i in x if i not in stop]) #逐词判断是否停用词，思路同上


data_dict = corpora.Dictionary(data[2])
data_corpus = [data_dict.doc2bow(i) for i in data[2]]
data_lda = models.LdaModel(data_corpus, num_topics=3, id2word=data_dict)

for i in range(0,data_lda.num_topics - 1):
    #data_lda.show_topic(i) #输出每个主题
    data_lda.print_topic(i)

"""
写入训练出来的主题到本地
"""

#mixture = [dict(data_lda[x]) for x in data_lda.top_topics]
#pd.DataFrame(mixture).to_csv("tpoics.csv")

"""
data_lda.print_topic(0)
'0.014*却 + 0.011*等待 + 0.008*知道 + 0.007*我要 + 0.007*孤独 + 
0.006*明天 + 0.006*已经 + 0.006*感觉 + 0.005*朋友 + 0.005*改变'

data_lda.print_topic(1)
'0.014*爱 + 0.007*生命 + 0.006*无法 + 0.006*真的 + 0.005*一个 + 
0.005*灵魂 + 0.005*天堂 + 0.005*忘记 + 0.005*永恒 + 0.005*存在'

data_lda.print_topic(2)
'0.010*相信 + 0.009*生命 + 0.009*感觉 + 0.008*曾经 + 0.007*听到 + 
0.007*一天 + 0.005*一次 + 0.005*再 + 0.004*总是 + 0.004*亲爱'
"""



"""
data_lda.show_topic(0)

[('却', 0.014015182197407444),
 ('等待', 0.010949027650187303),
 ('知道', 0.0081246164246606984),
 ('我要', 0.0074963036736376025),
 ('孤独', 0.0074212622769418849),
 ('明天', 0.0064092879444910059),
 ('已经', 0.0059665917297095005),
 ('感觉', 0.0058765033251896798),
 ('朋友', 0.0052657011091186796),
 ('改变', 0.0051422703871088537)]

data_lda.show_topic(1)

[('爱', 0.013657796799127968),
 ('生命', 0.0070466728167218311),
 ('无法', 0.0058385469056192263),
 ('真的', 0.0056596320941366034),
 ('一个', 0.0054176291382921843),
 ('灵魂', 0.0052433751218678125),
 ('天堂', 0.0048766088254052356),
 ('忘记', 0.0047004362091176014),
 ('永恒', 0.0046988679699649493),
 ('存在', 0.0046948526917250126)]

data_lda.show_topic(2)

[('相信', 0.0095281874579332092),
 ('生命', 0.0091996791346611526),
 ('感觉', 0.008645224435353472),
 ('曾经', 0.0080669839382832096),
 ('听到', 0.0070502920675385309),
 ('一天', 0.0068943826182158675),
 ('一次', 0.0053901610145512639),
 ('再', 0.0049072668444572242),
 ('总是', 0.0044657971052054889),
 ('亲爱', 0.0044131117579484184)]
"""