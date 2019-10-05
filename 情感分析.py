txtArr=open('D:/白云山jieba分词与停用词后/白云山2017.txt',encoding='UTF-8') 
worddict=open('D:/sentiment/正面评价词语（中文）.txt',encoding='UTF-8')
for i in txtArr:
    if i in worddict:
        worddict[i] = worddict[i]+1
count(worddict)
