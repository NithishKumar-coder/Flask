from flask import Flask, render_template, request
import random, copy
import sqlite3
from logging.handlers import RotatingFileHandler

app = Flask(__name__,template_folder="template")
sqliteconnection=sqlite3.connect('quiz.db')

file_handler=RotatingFileHandler("error.log",maxBytes= 1024 * 1024 *100)
app.logger.addHandler(file_handler)

original_questions = {
 'Taj Mahal':['Agra','New Delhi','Mumbai','Chennai'],
 'Great Wall of China':['China','Beijing','Shanghai','Tianjin'],
 'Petra':['Jordan','Amman','Zarqa','Jerash'],
 'Machu Picchu':['Cuzco Region','Lima','Piura','Tacna'],
 'Egypt Pyramids':['Giza','Suez','Luxor','Tanta'],
 'Colosseum':['Rome','Milan','Bari','Bologna'],
 'Christ the Redeemer':['Rio de Janeiro','Natal','Olinda','Betim']
}

questions = copy.deepcopy(original_questions)

def conn(name):
    #this function is to create connection to database and create a table in it
    sqliteConnection = sqlite3.connect('quiz.db')
    cursor = sqliteConnection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS details (name text, score integer)")
    sqliteConnection.commit()
    return sqliteConnection

def insert(sqliteConnection,insert_details):
    #it is to insert new values into db
    cursor = sqliteConnection.cursor()
    insert_query="""INSERT INTO details(name,score) VALUES(?, ?)"""
    cursor.execute(insert_query, insert_details)
    sqliteConnection.commit()
    print(" Inserted ")

def get(sqliteConnection,name):
    cursor = sqliteConnection.cursor()
    # it is to select the  details of defined  name given by the user
    get_query = """SELECT * from details where name=?"""
    cursor.execute(get_query,[name])
    data= cursor.fetchall()
    return data

def shuffle(q):
 """
 This function is for shuffling 
 the dictionary elements.
 """
 selected_keys = []
 i = 0
 a=list(q.keys())
 while i < len(q):
  current_selection = random.choice(a)
  if current_selection not in selected_keys:
   selected_keys.append(current_selection)
   i = i+1
 return selected_keys

@app.route('/')
def gets():
  return render_template('user.html')

@app.route('/quiz')
def quiz():
 questions_shuffled = shuffle(questions)
 for i in questions.keys():
  random.shuffle(questions[i])
 return render_template('main.html', q = questions_shuffled, o = questions)


@app.route('/score', methods=['POST'])
def quiz_answers():
  correct = 0
  for i in questions.keys():
    answered = request.form[i]
    if original_questions[i][0] == answered:
      correct = correct+1
  name=request.form['name'].lower()
  if name:
    sqliteconnection=conn(name)
    li=[]
    li.append(name)
    li.append(correct)
    insert(sqliteConnection,li)
    deatailss=get(sqliteconnection,name)
  return render_template("second.html",deatailss=deatailss)




@app.errorhandler(500)
def handle_500_error(exception):
    app.logger.error(exception)
    return "<h1> An unknown server error occured</h1>"

@app.errorhandler(400)
def handle_404_error(exception):
    app.logger.error(exception)
    return "<h1>you didn't choose all the options<h1>"

if __name__ == '__main__':
 app.run()

''' correct = 0
 for i in questions.keys():
  answered = request.form[i]
  
  if original_questions[i][0] == answered:
   correct = correct+1'''