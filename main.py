from flask import Flask, render_template , request , redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    reg =  db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"
    

@app.route('/', methods=['GET','POST'])
def loging():
    return render_template("index.html")

@app.route('/about', methods=['GET','POST'])
def about():
    return render_template("about.html")

@app.route('/society_members', methods=['GET','POST'])
def society_members():
    return render_template("society_members.html")

@app.route('/academic_council', methods=['GET','POST'])
def academic_council():
    return render_template("academic_council.html")

@app.route('/finance_committee', methods=['GET','POST'])
def finance_committee():
    return render_template("finance_committee.html")

@app.route('/rti', methods=['GET','POST'])
def rti():
    return render_template("rti.html")

# people
@app.route('/faculty', methods=['GET','POST'])
def faculty():
    return render_template("faculty.html")

@app.route('/staff', methods=['GET','POST'])
def staff():
    return render_template("staff.html")

# more
@app.route('/library', methods=['GET','POST'])
def library():
    return render_template("library.html")

@app.route('/student_corner', methods=['GET','POST'])
def student_corner():
    return render_template("student_corner.html")

@app.route('/marksheet2nd', methods=['GET','POST'])
def marksheet():
    return render_template("file_download.html")

# Gallery
@app.route('/gallery', methods=['GET','POST'])
def gallery():
    return render_template("gallery.html")

@app.route('/admin',methods=['GET', 'POST'])
def admi():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if(username == "S" and password == "1"):
                return redirect("/admine")
        else:
            return redirect("/admin")
        
    return render_template("Loginpage.html")

@app.route('/admine', methods=['GET', 'POST'])
def admin():
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        reg = request.form['reg']
        todo = Todo(title=title, desc=desc ,reg = reg)
        db.session.add(todo)
        db.session.commit()
           
    allTodo = Todo.query.all() 
    return render_template('admin.html', allTodo=allTodo)

@app.route('/student', methods=['GET', 'POST'])
def student():
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        reg = request.form['reg']
        todo = Todo(title=title, desc=desc ,reg = reg)
        db.session.add(todo)
        db.session.commit()
        
    allTodo = Todo.query.all() 
    return render_template('student.html', allTodo=allTodo)

@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        reg = request.form['reg']
        todo = Todo.query.filter_by(sno=sno).first()
        todo.title = title
        todo.desc = desc
        todo.reg = reg
        db.session.add(todo)
        db.session.commit()
        return redirect("/admine")
        
    todo = Todo.query.filter_by(sno=sno).first()
    return render_template('update1.html', todo=todo)

@app.route('/delete/<int:sno>')
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/admine")

if __name__ == "__main__":
    app.run(debug=True, port = 1234)