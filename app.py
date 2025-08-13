from flask import Flask, request, render_template, redirect
import sqlite3
import uuid
import smtplib

app = Flask(__name__)

@app.route('/send_phish/<email>')
def send_phish(email):
    token = str(uuid.uuid4())
    link = f"http://yourdomain.com/phish/{token}"
    store_token(email, token)
    send_email(email, link)
    return f"Phishing email sent to {email}"

@app.route('/phish/<token>')
def phish_page(token):
    log_click(token)
    return render_template('phish.html')

@app.route('/report/<token>')
def report_email(token):
    log_report(token)
    return "Thanks for reporting!"

def store_token(email, token):
    conn = sqlite3.connect('db.sqlite')
    conn.execute("INSERT INTO tokens (email, token) VALUES (?, ?)", (email, token))
    conn.commit()

def log_click(token):
    conn = sqlite3.connect('db.sqlite')
    conn.execute("UPDATE tokens SET clicked=1 WHERE token=?", (token,))
    conn.commit()

def log_report(token):
    conn = sqlite3.connect('db.sqlite')
    conn.execute("UPDATE tokens SET reported=1 WHERE token=?", (token,))
    conn.commit()

def send_email(to, link):
    # Use SMTP or SendGrid API
    pass

if __name__ == '__main__':
    app.run(debug=True)
