#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
from heapq import nlargest
from collections import defaultdict


# In[2]:


def Summarize(strFile):
    with open(strFile) as f:
        data = f.read()
        replace = {
            ord('\f') : ' ',
            ord('\t') : ' ',
            ord('\n') : ' ',
            ord('\r') : None
        }

    data = data.translate(replace)

    stop_words = set(stopwords.words('english') + list(punctuation))
    words = word_tokenize(data.lower())

    word_tokens = [word for word in words if word not in stop_words] 
    sentence_tokens = sent_tokenize(data)

    word_freq = FreqDist(word_tokens)

    ranking = defaultdict(int)

    for i, sentence in enumerate(sentence_tokens):
        for word in word_tokenize(sentence.lower()):
            if word in word_freq:
                ranking[i] += word_freq[word]

    indexes = nlargest(5, ranking, key=ranking.get)
    final_sentences = [sentence_tokens[j] for j in sorted(indexes)]
    return ' '.join(final_sentences)


# In[3]:


print(Summarize('d:\\docker\\youtube-dl\\20200216.txt'))


# In[ ]:




