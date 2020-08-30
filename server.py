from flask import Flask, render_template, request, redirect
import os
from sklearn.externals import joblib
from datetime import datetime
import csv

app = Flask(__name__)


@app.route('/')
def homme_page():
    return render_template("index.html")


@app.route('/<string:name>')
def homme(name):
    return render_template(name)


def write_to_file(data):
    with open("database.txt", 'a') as file:
        file.write(str(data['email']) + '\t' + str(data['subject']) + '\t' + str(data['message']) + '\t' + str(
            datetime.today()))


def write_to_csv(data):
    with open("database.csv", mode='a') as file2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        date = datetime.today()
        csv_writer = csv.writer(file2, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message, date])


def class_lang(data):
    text = "fisher"#data['subject']
    #clf = joblib.load("model.pkl")
    #user_text = np.array([text])
    #y_predicted = clf.predict_proba(user_text)
    afri = 1#y_predicted[0][0]
    dut = 2#y_predicted[0][1]
    eng = 3#y_predicted[0][2]
    ger = 4#y_predicted[0][3]
    ven = 5#y_predicted[0][4]
    return text,afri,dut,eng,ger,ven



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("thankyou.html")
        except:
            print("Did not save to database")
    else:
        print("something went wrong try again")


@app.route('/classify', methods=['POST', 'GET'])
def classify():
    message = float(2)
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            text,afri,dut,eng,ger,ven = class_lang(data)
            afrikaans = float(100)
            dutch = float(10)
            english = float(20)
            german = float(45)
            venda = float(60)

            return render_template("language.html", text=text,afrikaans=afrikaans, english=english, dutch=dutch, german=german,
                                   venda=venda)
        except:
            print("Something went wrong")
    else:
        print("something went wrong try again")


@app.route('/clear', methods=['POST', 'GET'])
def clear():
    message = float(2)
    if request.method == 'POST':
        try:
            afrikaans = float(0)
            dutch = float(0)
            english = float(0)
            german = float(0)
            venda = float(0)
            text = ''
            return render_template("language.html", text=text, afrikaans=afrikaans, english=english, dutch=dutch, german=german,
                                   venda=venda)
        except:
            print("Something went wrong")
    else:
        print("something went wrong try again")


"""

@app.route('/index.html')
def my_home():
    return render_template('./index.html')

@app.route('/.html')
def home():
    return render_template('./index.html')

@app.route('/works.html')
def my_work():
    return render_template('./works.html')

@app.route('/about.html')
def about_me():
    return render_template('./about.html')

@app.route('/contact.html')
def contact():
    return render_template('./contact.html')


@app.route('/components.html')
def comp():
    return render_template('./components.html')

@app.route('/blog')
def blog():
    return "These are my thoughts on blogs"


@app.route('/blog/2020/dogs')
def blog2():
    return "These are my dog"
"""
