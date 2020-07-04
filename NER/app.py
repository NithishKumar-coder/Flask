from flask import Flask,render_template,url_for,request
import pos_tagger  #create module 
import os
import sys
import json
from tld import get_fld
from logging.handlers import RotatingFileHandler

app = Flask(__name__,template_folder="template")


@app.route('/')
def index():
	return render_template("index.html")

file_handler=RotatingFileHandler("error.log",maxBytes=1024*1024*100)
app.logger.addHandler(file_handler)

def read_json(file_name):
  with open('./data/'+file_name+'.json', 'r') as f:
          json_data=json.loads(f.read())
  return json_data

def get_entity_namelist(json_data):
    entity=[]
    names=[]
    num_of_results=[]
    results=[]
    for data in json_data:
        value_list=[]
        for key,value in data.items():
             value_list.append(value)
        res={value_list[0]:value_list[1]}
        results.append(res) 
    return results
##usage of relative path to store it in the same directory 
start=os.getcwd()
path="\\data"
data=os.path.relpath(path, start) 
def create_folder():
  new_path = r'data' 
  if not os.path.exists(new_path):
    os.makedirs(new_path)
  return "data"

#exception handling
@app.errorhandler(500)
def Iserror(exception):
  app.logger.error(exception)
  return "<h1>Unable to give output due to server error</h1>"

@app.route("/process",methods =['POST', 'GET'])
def process():
    if request.method == 'POST':
        url = request.form['url']
        folder_name=create_folder()
        
        file_name = get_fld(url, fail_silently=True)
        pos_tagger.send(url,folder_name) 
        json_data=read_json(file_name)
        results=get_entity_namelist(json_data)
              
        return render_template("index.html",results=results)

if __name__ == '__main__':
	app.run()
    


    
