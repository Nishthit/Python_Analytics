# -*- coding: utf-8 -*-
"""
Created on Tue May 18 21:03:01 2021

@author: nisht
"""

import wikipedia

#Creating a function to get desired data from wikipedia
def get_wiki(query):
    title = wikipedia.search(query)[0]
    page = wikipedia.page(title)
    return page.content

print (get_wiki("IIM Shillong"))

#print (get_wiki("hhvhsgkaxgk"))

from wordcloud import WordCloud, STOPWORDS

stopword = STOPWORDS
    
wc = WordCloud(width = 800, height = 800, 
                   background_color="White",
                   mask=None,
                   max_words=200,
                   stopwords=stopword,
                   min_font_size = 10).generate(get_wiki("IIM Shillong"))

import matplotlib.pyplot as plt
plt.imshow(wc)

wc.to_file("C:/Users/nisht/Desktop/CPBA/wordcloud_wiki.png")