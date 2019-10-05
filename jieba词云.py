import jieba.analyse
import jieba
import wordcloud
# import pandas as pd
f=open('D:/词频/白云山2015.txt')
t=f.read()
f.close()
ls=jieba.lcut(t)
txt="".join(ls)
w=wordcloud.WordCloud(font_path='msyh.ttc', width=1000,height=700, background_color='white')
w.generate(txt)
w.to_file('D:/词频/白云山2015.png')
