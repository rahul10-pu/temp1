from flask import Flask, render_template
# from app import app
app = Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Rahul'}
    profiles = [
        {
            'name': {'username': 'Rahul'},
            'linkdin': 'https://www.linkedin.com/in/rahul10-pu/'
        },
        {
            'name': {'username': 'Rohit'},
            'linkdin': 'https://www.linkedin.com/in/rahul10-pu/'
        }
    ]
    return render_template('index_all.html', title='Home', user=user, profiles=profiles)

if __name__ == '__main__':
   app.run(debug = True)