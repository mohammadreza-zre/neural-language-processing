import re  # regular expression for removing additional symptoms and data cleaning
import requests # sending request to the website and accessing to the content base on html
from bs4 import BeautifulSoup # for partitioning html base on 'p' - 'title' - and ... (html tags)
from nltk import sent_tokenize # separating text to sentences
from nltk import word_tokenize # separating text to words
from nltk.corpus import stopwords # removing words with low importance
import heapq # summarization
import numpy as np



req = requests.get("https://en.wikipedia.org/wiki/SpaceX")
bs4 = BeautifulSoup(req.content,'html.parser')
parag = bs4.find_all('p')

final_text = ""
for p in parag :
    final_text += p.text


print("text...upload")



# removing numbers
final_text = re.sub(r'\[[0-9]*]'," ",final_text)
# removing extra space
final_text = re.sub(r'\s+'," ",final_text)
# removing everything except alphabets
final_text = re.sub(r'[^\w\s.]' ," " , final_text)
# removing extra space
final_text = re.sub(r'\s+' , " ",final_text)
# print("---------------------------------------------------------------------------------")
# print(final_text)
# print("---------------------------------------------------------------------------------")

words = word_tokenize(final_text)
sents = sent_tokenize(final_text)
stops = stopwords.words('english')




word_freq = {}
for word in words :
    if word not  in stops :
        if word not in word_freq :
            # word as keys
            # iteration as values
            word_freq[word] = 1
        else :
            word_freq[word] += 1


# dict standardization
max_freq = max(word_freq.values())
for word in word_freq.keys() :
    word_freq[word] = (word_freq[word] / max_freq)


sents_score = {}
for sent in sents :
    for word in word_tokenize(sent) :
        if word in word_freq.keys() :
            if len(sent.split(' ')) < 30 :
                if sent not in sents_score.keys() :
                    sents_score[sent] = word_freq[word]
                else :
                    sents_score[sent] += word_freq[word]

print('----------------------------first method----------------------------')
scores=sents_score.values()
scores=sorted(scores , reverse=True)[:5]
for (i,score) in enumerate(scores) :
    for dict_scores in sents_score.values():
        if score == dict_scores :
            vals = list(sents_score.values())
            keys = list(sents_score.keys())
            ind = vals.index(score)
            print(keys[ind])
print('----------------------------second method----------------------------')


summary = heapq.nlargest(5 , sents_score , key=sents_score.get)
print(summary)
summary = " ".join(summary)
print(summary)





