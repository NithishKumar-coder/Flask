import re

from newspaper import Article  

from bs4 import BeautifulSoup

import nltk

import NER #create module



#function to extract content from url and return list of the all noun phrase sentence

def content_extract(url):

    article = Article(url, language="en") # en for English 



#To download the article 

    article.download() 

    html=article.html

    

# Passing the source code to BeautifulSoup to create a BeautifulSoup object for it.

    soup = BeautifulSoup(html,"lxml")

    data = soup.findAll(text=True)

    

    def visible(element):

#including elements in style,script,head 

        if element.parent.name in ['style', 'script', '[document]', 'head', 'title']:

            return False

#for returning texts

        elif re.match('<!--.*-->', str(element.encode('utf-8'))):

            return False

        return True

    sentence =list(filter(visible, data)) #The filter() function returns  text were the items are filtered through visible() function to test if the item is accepted or not.





#create a nouns list and append noun phrase sentence 

    nouns=[]

    for sent in sentence:

        tokenized = nltk.sent_tokenize((sent))

        [nouns.append(word) for (word, pos) in nltk.pos_tag(tokenized) if(pos[:2] == 'NN' )]

    

    return nouns

    



def send(web):



#function returns list of noun pharse sentence

    content=content_extract(web)       



    n=NER.data(content)

    return n