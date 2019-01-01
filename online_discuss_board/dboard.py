from flask import Flask, render_template, request
from datetime import datetime

class Entry(object):
     
    def __init__(self, author, date, content):
        self.author = author
        self.date = date
        self.content = content

# create an instance of Flask. (a "Flask process")
app = Flask(__name__) 

post_file = "entries.txt"
password_file = "users.txt"

def read_posts():
    pass

def create_post(author, date, content):
    pass

def check_password(user, passwd):
    pass
        

@app.route('/')  
def dboard():
        
    return render_template("dboard.html")
    
@app.route('/compose')  
def compose():    
    return render_template("newpost.html")
        
    
if __name__ == "__main__":
    app.run(debug=True, port=7774)
