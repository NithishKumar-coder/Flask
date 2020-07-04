import pos_tagger  #create module 
import os
import sys
import argparse


def com(url,folder_name):
    if "http" or "www" in url:
        pos_tagger.send(url,folder_name)         
    else:
        print("You have entered an invalid url")

#Function to return usage message 
def msg():
    message='''You failed to provide url as input on command line'''
    return message
    
#Creating a parser
parser = argparse.ArgumentParser(usage=msg())
#Adding arguments
parser.add_argument("\"You must provide url on command line\"")
#Parsing arguments
args = parser.parse_args()

#getting the path of current directory
data=os.getcwd()

#creating new  data folder directory
new_path = r'data' 
if not os.path.exists(new_path):
    os.makedirs(new_path)
folder_name="data"
print("Directory '% s' is built!!!!\n" % new_path)

com(sys.argv[1],folder_name)
