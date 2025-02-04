from flask import Flask, request, redirect, url_for, render_template, session
from pymongo import MongoClient
from werkzeug.security import check_password_hash
import uuid

app = Flask(__name__)
app.secret_key = 'your_secret_key' 


client = MongoClient("mongodb://localhost:27017/")
db = client['ECE_DPT']
student_collection = db['student_mail_pass']
teacher_collection = db['teacher_mail_pass']
student_preod_collection=db['student_pre_od']

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user_type = request.form.get('user_type')
        collection = teacher_collection if user_type == 'teacher' else student_collection
        user = collection.find_one({'email': email})
        if user and user['password'] == password:
            session['user'] = email
            return redirect(url_for('index'))
        else:
            return 'Invalid credentials', 401
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)  
    return redirect(url_for('login'))  


@app.route('/onduty', methods=['GET'])
def onduty():
    
    if 'user' not in session:
        return redirect(url_for('login'))
    email = session['user']
    teacher = teacher_collection.find_one({'email': email})
    student = student_collection.find_one({'email': email})
    
    if teacher:
        return redirect(url_for('teachersonduty'))
    elif student:
        return redirect(url_for('studentonduty'))
    else:
        return 'User type not found', 401

@app.route('/teachersonduty')
def teachersonduty():
    email=session['user']
    students = student_preod_collection.find({"teacheremail":email})  
    return render_template('teachersonduty.html', students=students)

@app.route('/approve/<application_id>', methods=['POST'])
def approve_student(application_id):
    
    student_preod_collection.update_one({'application_id': application_id}, {'$set': {'approved': True}})
    return redirect(url_for('teachersonduty'))


@app.route('/studentonduty')
def studentonduty():
    return render_template('studentonduty.html')


@app.route('/preodform', methods=['GET', 'POST'])
def preodform():
    if request.method == 'POST':
        register_number = request.form.get('register_number')
        name = request.form.get('name')
        date_from = request.form.get('date_from')
        date_to = request.form.get('date_to')
        time_from = request.form.get('time_from')
        time_to = request.form.get('time_to')
        purpose = request.form.get('purpose')
        event_name = request.form.get('event_name')
        venue = request.form.get('venue')
        class_advisor = request.form.get('class_advisor')
        studentemail = request.form.get('studentemail') 
        teacheremail = request.form.get('teacheremail')  

        data = {
            'application_id': str(uuid.uuid4()),  
            'register_number': register_number,
            'name': name,
            'date_from': date_from,
            'date_to': date_to,
            'time_from': time_from,
            'time_to': time_to,
            'purpose': purpose,
            'event_name': event_name,
            'venue': venue,
            'class_advisor': class_advisor,
            'studentemail': studentemail,
            'teacheremail':teacheremail, 
            'approved': False  
        }
        student_preod_collection.insert_one(data)
        return redirect(url_for('onduty'))
    
    return render_template('form.html')


@app.route('/getstudentpreoddetails', methods=['GET', 'POST'])
def getstudentpreoddetails():
    email = session['user']
    students = list(student_preod_collection.find({"studentemail": email}))
    return render_template('studentpreodlist.html', students=students)



@app.route('/faculty', methods=['GET'])
def faculty():
    return render_template('faculty.html')

@app.route('/seminarbooking', methods=['GET'])
def seminarbooking():
    return render_template('seminarbooking.html')

@app.route('/achievements', methods=['GET'])
def achievements():
    return render_template('achievements.html')
@app.route('/labview')
def labview():
    return render_template('labview.html')


if __name__ == '__main__':
    app.run(debug=True)

