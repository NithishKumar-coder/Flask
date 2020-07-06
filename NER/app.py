from flask import Flask,render_template,url_for,request,jsonify
import pos_tagger  #create module 
import json
from logging.handlers import RotatingFileHandler

app = Flask(__name__,template_folder="template")
file_handler=RotatingFileHandler("error.log",maxBytes= 1024 * 1024 *100)
app.logger.addHandler(file_handler)

@app.route('/')
def index():
	return render_template("index.html")

@app.route("/api/process", methods=['GET'])
def process():
  url=request.args.get("url")
  content = pos_tagger.send(url)
  return jsonify(content)

@app.errorhandler(500)
def handle_500_error(exception):
    app.logger.error(exception)
    return "<h1> An unknown server error occured</h1>"

@app.errorhandler(404)
def handle_404_error(exception):
    app.logger.error(exception)
    return "Not Found"

if __name__ == '__main__':
	app.run()
