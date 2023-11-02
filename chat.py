import os
import pandas as pd
from flask import Flask, render_template, request

dataSet=pd.read_csv("DataSet.csv",encoding= 'unicode_escape')

def get_response(input):
    
    #preprocessing 
    input = input.lower().split(" ")
    
    matchInput=False
    isFound=False
    
    #dept first search to find the first meet key word then return the response
    for i in range(len(dataSet)-1):
        for j in dataSet["Keyword"][i].split(","):
            if j in input:
                return dataSet["Response"][i]
                
                matchInput=True
                isFound=True
                
                break
                           
        if(isFound):
            break

    if(not matchInput):
        return "Sorry! I didn't get what you saying. Can you re-phrase that?"  
    return ""       

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userInput = request.args.get('botMsg')
    return str(get_response(userInput))


if __name__ == "__main__":
    os.system("start http://127.0.0.1:5000/")
    app.run()