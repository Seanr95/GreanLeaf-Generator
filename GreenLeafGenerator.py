from flask import Flask, render_template, request, redirect, send_file
from openpyxl import load_workbook
from datetime import datetime
import re
import io
from Helper import generate_unique_glid, glid_exists, save_glid, delete_glid

app = Flask(__name__, template_folder='templates', static_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_glid')
def generate_glid():
    # Generate a new GLID
    glid = generate_unique_glid()
    # Save the GLID to the Excel file
    save_glid(glid)
    return render_template('index.html', generated_glid=glid)

@app.route('/add_glid', methods=['POST'])
def add_glid():
    # Retrieve GLID from the form
    glid = request.form['glid']

    # Validate the GLID using the regex pattern
    if not re.match(r'^[0-9a-fA-F]{4}$', glid):
        return render_template('index.html', error="Invalid GLID. Please enter a 4-digit hexadecimal value.", generated_glid=glid)

    # Check if GLID already exists
    if not glid_exists(glid):
        # Save the GLID to the Excel file
        save_glid(glid)

    return redirect('/')

@app.route('/delete_glid', methods=['POST'])
def delete_glid_entry():
    # Retrieve GLID from the form
    glid = request.form['glid']

    # Validate the GLID using the regex pattern
    if not re.match(r'^[0-9a-fA-F]{4}$', glid):
        return render_template('index.html', error="Invalid GLID. Please enter a 4-digit hexadecimal value.")

    if not glid_exists(glid):
        return render_template('index.html', error="GLID does not exist.")

    delete_glid(glid)
    return redirect('/')

@app.route('/download_glids')
def download_glids():
    return send_file('glids.xlsx', as_attachment=True)

if __name__ == '__main__':
    app.run()
