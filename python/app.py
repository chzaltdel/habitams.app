import os
from flask import Flask, render_template

current_dir = os.path.dirname(os.path.abspath(__file__))

parent_dir = os.path.dirname(current_dir)

web_dir = os.path.join(parent_dir, 'web')

app = Flask(__name__, 
            template_folder=web_dir, 
            static_folder=os.path.join(web_dir, 'styles'),
            static_url_path='/styles')

@app.route('/')
def home(): 
    return render_template('home.html')

@app.route('/habits')
def habits():
    return render_template('habits.html')

@app.route('/collect')
def collect():
    return render_template('collect.html')

if __name__ == '__main__':
    app.run(debug=True)