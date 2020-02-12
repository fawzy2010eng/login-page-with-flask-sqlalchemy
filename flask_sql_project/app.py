from flask import Flask, render_template, url_for, redirect ,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///C:/Users/Ahmed/PycharmProjects/flask_sql_project/fawzy.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class PERSON(db.Model):
    email = db.Column(db.String(80),primary_key=True)
    password = db.column(db.String(20))
    
    def __init__(self,email,password):
        self.email = email
        self.password = password

def selectByMail(mail):
    rows = PERSON.query.all()
    for person in rows:
        if person.email == mail:
            return person.password
    db.session.commit()        

        
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
#        email = request.form.get('mail')
#        passw = request.form['pass']
        return selectByMail('ahmedfawzy_civil@yahoo.com')

    else:
        return 'sex'

@app.route('/login',methods=['GET', 'POST'])
def login():
    return 'seven'

if (__name__) == "__main__":
    app.run(debug = True)
        
        