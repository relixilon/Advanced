from flask import *  
import sqlite3
app = Flask(__name__)  
db = sqlite3.connect("SD.db")
Connection = db.cursor()

# Connection.execute('''DROP TABLE Users''')

@app.route('/')  
def customer():  
   return render_template('login.html')  
  
@app.route('/test',methods = ['POST', 'GET'])  
def login():
    #checking first if the method is POST as well as the fields were both filled 
    msg=''
    if (request.method == 'POST') and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        
    
        db = sqlite3.connect("SD.db")
        Connection = db.cursor()
        Connection.execute(
              """CREATE TABLE if not exists Users (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                Clearance_level INTEGER NOT NULL)
                """) 
        Connection.execute("""INSERT INTO Users VALUES(1,'nurse','1234',1)""")
        Connection.execute("""INSERT INTO Users VALUES(2,'son','5678',2)""")
        Connection.execute('SELECT * FROM Users WHERE username = ? and password= ?', (username,password, ))
        account = Connection.fetchone()
        print(account)
        if account:
            
            msg=account[1]
            
            return render_template('test.html',msg=msg)
        else:
            msg = 'Incorrect username / password !'
            return render_template('login.html', msg = msg)