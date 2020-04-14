from flask import Flask, render_template, url_for, request, redirect
import csv


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<page_name>')
def html_page(page_name = 'index.tml'):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:

            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            return "Database didn't respond"
    return 'form failed'

def write_to_csv(data):
    with open('./database.csv', mode="a", newline='') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
