import re

from newspaper import Article  

from bs4 import BeautifulSoup

import spacy

import json





#load the language model instance in spacy

nlp =spacy.load('en_core_web_sm') 



#Create lable list

Label_list=["DATE","PERSON","NORP","FAC","ORG","LOC","PRODUCT","EVENT","WORK_OF_ART","LAW","LANGUAGE","TIME","PERCENT","MONEY","QUALITY","ORDINAL","GPE"]



#function return list of name text and their associated entity label

def content_text(content):

#create data_list to store all entities 

    data_list=[]

    for sent in content:

        doc = nlp(sent)

#itrate each entity and append in list 

        for ent in doc.ents:

            data_list.append({"Name":ent.text,"Entity":ent.label_})

#remove repeated name and their entity 

    res = [] 

    [res.append(x) for x in data_list if x not in res ]

    

    return res

        



def data(content):



#fumction to return list of name and their entity

    data=content_text(content)   

#iterate Label_list

    data_list=[]

    for label in Label_list:

        name_list=[]

        for items in data:

            entity=items.get("Entity")

            if entity== label:

                    name_list.append(items.get("Name"))

        if len(name_list):

            data_list.append({"Entity":label,"Name":name_list})

    

    return data_list