from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define Todo model directly in app.py
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), nullable=False, default='Pending')

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

with app.app_context():
    # Execute db.create_all() within the application context
    db.create_all()

# @app.route('/')
# def index():
#     return render_template('index.html')


@app.route('/' , methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        title= request.form['title']
        desc= request.form['desc']
        todo= Todo(title= title, desc=desc)
        db.session.add(todo)
        db.session.commit()
    allTodo= Todo.query.all()
    return render_template('index.html', allTodo=allTodo)


@app.route('/show')
def products():
    allTodo= Todo.query.all()
    print(allTodo)
    return 'This is product page!'

@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    if request.method=='POST':
        title= request.form['title']
        desc= request.form['desc']
        todo= Todo.query.filter_by(sno=sno).first()
        todo.title=title
        todo.desc=desc
        db.session.add(todo)
        db.session.commit()
        return redirect('/')

    todo= Todo.query.filter_by(sno=sno).first()
    return render_template('update.html', todo=todo)

@app.route('/delete/<int:sno>')
def delete(sno):
    todo= Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')

@app.route('/status/<int:sno>')
def status(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    todo.status = 'Completed'
    db.session.commit()
    return redirect('/')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__=="__main__":
    app.run(debug=True, port=8000)

# today its 13/5/24 now im  installing sqlalchemy to create db and all that stuff































# from flask import Flask, render_template, request, redirect
# from flask_sqlalchemy import SQLAlchemy
# # so here i am importing SQLAlchemy
# from datetime import datetime
# # from app import app, db
# from flask_migrate import Migrate


# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///todo.db"
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= FALSE
# # HERE IM USING SQLITE DB if u want u can use mysql also and here have changed the name to todo.db
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# from models import Todo

# class Todo(db.Model):
#     sno = db.Column(db.Integer, primary_key=True)
#     title =  db.Column(db.String(200), nullable=False)
#     desc = db.Column(db.String(500), nullable=False)
#     date_created = db.Column(db.DateTime, default=datetime.utcnow)
#     status=db.Column(db.String(20), nullable=False, default='Pending')

#     def __repr__(self) -> str:
#         return f"{self.sno} - {self.title}"

# # from models import Todo, User

# # Use app.app_context() to create an application context
# with app.app_context():
#     # Execute db.create_all() within the application context
#     db.create_all()


# @app.route('/' , methods=['GET', 'POST'])
# def hello_world():
#     if request.method == 'POST':
#         title= request.form['title']
#         desc= request.form['desc']
#         todo= Todo(title= title, desc=desc)
#         db.session.add(todo)
#         db.session.commit()
#     allTodo= Todo.query.all()
#     return render_template('index.html', allTodo=allTodo)


# @app.route('/show')
# def products():
#     allTodo= Todo.query.all()
#     print(allTodo)
#     return 'This is product page!'

# @app.route('/update/<int:sno>', methods=['GET', 'POST'])
# def update(sno):
#     if request.method=='POST':
#         title= request.form['title']
#         desc= request.form['desc']
#         todo= Todo.query.filter_by(sno=sno).first()
#         todo.title=title
#         todo.desc=desc
#         db.session.add(todo)
#         db.session.commit()
#         return redirect('/')

#     todo= Todo.query.filter_by(sno=sno).first()
#     return render_template('update.html', todo=todo)

# @app.route('/delete/<int:sno>')
# def delete(sno):
#     todo= Todo.query.filter_by(sno=sno).first()
#     db.session.delete(todo)
#     db.session.commit()
#     return redirect('/')

# @app.route('/status/<int:sno>')
# def status(sno):
#     todo = Todo.query.filter_by(sno=sno).first()
#     todo.status = 'Completed'
#     db.session.commit()
#     return redirect('/')


# if __name__=="__main__":
#     app.run(debug=True, port=8000)

# # today its 13/5/24 now im  installing sqlalchemy to create db and all that stuff



