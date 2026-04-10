import os
from flask import Flask, render_template, request
import pyodbc

app = Flask(__name__)

# This name must match the one you set in Azure Environment Variables
conn_str = os.environ.get('AZURE_SQL_CONNECTIONSTRING')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('employee_name')
    # Logic to insert into SQL goes here
    return f"Thanks {name}, your data is being sent to our Azure SQL database!"

if __name__ == '__main__':
    app.run()
  
