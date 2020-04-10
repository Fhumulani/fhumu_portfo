from flask import Flask, render_template, request, redirect
import os
from datetime import datetime
import csv

app = Flask(__name__)


@app.route('/')
def homme_page():
	return render_template('index.html')



@app.route('/<string:name>')
def homme(name):
	return render_template(name)

def write_to_csv(data):
	try:
		with open("database.csv", newline='',mode='a') as file2:
			email = data['email']
			subject = data['subject']
			message = data['message']
			date = datetime.today()
			csv_writer = csv.writer(file2,delimiter=',',quoting=csv.QUOTE_MINIMAL)
			csv_writer.writerow([email,subject,message,date])
			return redirect("index.html")
	except:
		print("fisher weee")



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
    	try:
    		data = request.form.to_dict()
    		write_to_csv(data)
    		return redirect('thankyou.html')
    	except:
    		print("Did not save to database")
    else:
    	print("something went wrong try again")



