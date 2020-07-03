import re
from newspaper import Article  
from bs4 import BeautifulSoup
import spacy
import json
# create Entity module
import Entity

#load the language model instance in spacy
nlp =spacy.load('en_core_web_sm') 

#Create lable list
Label_list=["DATE","PERSON","NORP","FAC","ORG","LOC","PRODUCT","EVENT","WORK_OF_ART","LAW","LANGUAGE","TIME","PERCENT","MONEY","QUALITY","ORDINAL","GPE"]

#function return list of name text and their associated entity label
def content_text(content):
#create data_list to store all entities 
    data_list=[]

    doc = nlp(content)
#itrate each entity and append in list 
    for ent in doc.ents:
            data_list.append({"Name":ent.text,"Entity":ent.label_})
#remove repeated name and their entity 
    res = [] 
    [res.append(x) for x in data_list if x not in res ]
    return res
     

def data(fname,folder_name):
#open text file in read mode
    with open ("./"+folder_name+"/"+fname+".txt","r",encoding="utf-8") as fi:
#read it using read() function
        content=fi.read()
#fumction to return list of name and their entity
        data=content_text(content)   
#create new all_entities.json file 
        with open("./"+folder_name+"/all_entities.json", "w") as f:
#write all the entites data in json
            f.write(json.dumps(data, sort_keys=False, indent=2, separators=(',', ': ')))
    
    print("all_entities.json file is created!!!!\nThis is use to store name and entity type of each tokenized words.\n ")
#iterate Label_list
    data_list=[]
    for label in Label_list:
#passing arguments to Entity module
        data= Entity.Get_Entity(label,fname,folder_name)
        if data:
             data_list.append(data)

    with open ("./"+folder_name+"/"+fname+".json","w") as f:
                f.write(json.dumps(data_list, sort_keys=False, indent=2, separators=(',', ': '))) 
    print(fname+".json file is created!!!!\nThis is use to store entity and their associated list of names.\n")
