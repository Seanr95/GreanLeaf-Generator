# GreenLeaf Generator

GreenLeaf Generator is a web application built with Flask that allows users to generate, add, and delete unique GLIDs (Global Leaf Identifiers). GLIDs are 4-digit hexadecimal values used to identify and track leaves in the GreenLeaf system.

![GreenLeaf Generator Screenshot](screenshot.png)

## Features

- Generate a new unique GLID.
- Add a custom GLID to the system.
- Delete an existing GLID from the system.
- Download the list of GLIDs as an Excel file.

## Prerequisites

Before running the application, make sure you have the following installed:

- Python 3.x
- Flask (can be installed via `pip install flask`)
- openpyxl (can be installed via `pip install openpyxl`)

## Installation and Usage

1. Clone this repository to your local machine:

```bash
git clone https://github.com/Seanr95/greenleaf-generator.git

1. Change into the project directory:
cd greenleaf-generator

2. Install the required dependencies:
pip install -r requirements.txt

3. Run the Flask application:
python GreenLeafGenerator.py

4. Open your web browser and go to http://127.0.0.1:5000/ to access the GreenLeaf Generator.
