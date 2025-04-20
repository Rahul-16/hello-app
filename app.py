from flask import Flask, request, render_template
import sqlite3


app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')
   
@app.route('/greet',methods=['POST'])
def greet():
   name = request.form['name']
   
   conn = sqlite3.connect('data.db')
   c = conn.cursor()
   c.execute('CREATE TABLE IF NOT EXISTS greetings (name TEXT)')
   c.execute('INSERT INTO greetings (name) VALUES (?)', (name,))
   conn.commit()
   conn.close()
   return f"<h2>Hello, {name}!</h2><br><a href='/'>Go back</a>"

@app.route('/all')
def all_greetings():
   conn = sqlite3.connect('data.db')
   c = conn.cursor()
   c.execute('SELECT name FROM greetings')
   names = c.fetchall()
   conn.close()
   return "<br>".join(name[0] for name in names)
   
if __name__ == '__main__':
   init_db()
   app.run(debug=True)