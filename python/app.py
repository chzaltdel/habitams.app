import os
from flask import Flask, render_template

current_dir = os.path.dirname(os.path.abspath(__file__))

parent_dir = os.path.dirname(current_dir)

template_dir = os.path.join(parent_dir, 'web')

app = Flask(__name__, template_folder=template_dir, static_folder=template_dir)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)