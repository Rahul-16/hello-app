from flask import Flask, request, render_template

app = Flask(__name__)

import sqlite3

def init_db():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS greetings (name TEXT)')
    conn.commit()
    conn.close()
    
@app.route('/')
def index():
   return render_template('index.html')
   
@app.route('/greet',methods=['POST'])
def greet():
   name = request.form['name']
   
   conn = sqlite3.connect('data.db')
   c = conn.cursor()
   c.execute('INSERT INTO greetings (name) VALUES (?)', (name,))
   conn.commit()
   conn.close()
   return f"<h2>Hello, {name}!</h2><br><a href='/'>Go back</a>"
   
if __name__ == '__main__':
   init_db()
   app.run(debug=True)