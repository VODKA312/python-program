words=['look','into','my','AAA','look','into','my','AAA',
       'the','AAA','the','AAA','the','eyes','not','BBB',
       'the','AAA','dont','BBB','around','the','AAA','look',
       'into','BBB','AAA','BBB','under']
from collections import Counter
word_counts = Counter(words)
print(word_counts)
#couner方法会返回一个存储出现次数和对应单词的字典
top_three=word_counts.most_common(3)
print(top_three)
