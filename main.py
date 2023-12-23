from flask import Flask, render_template, request
import smtplib
import datetime
import os

my_email = os.environ.get("email")
password = os.environ.get("password")

app = Flask(__name__)



@app.route('/')
def index():
    current_year = datetime.datetime.now().year
    return render_template('index.html', year=current_year)

@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            print("hh")
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email,
                                msg=f"Subject:Contact \n\n{name} filled the contact form on your portfolio website.\nEmail: {email}\nPhone: {phone}\nMessage: {message}")
        return render_template('success.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)