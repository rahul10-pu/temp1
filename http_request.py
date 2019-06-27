from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name
#If GET is present, Flask automatically adds support for the HEAD method and handles HEAD requests according to the HTTP RFC
@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      print("In POST")
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      print("in Get")
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(debug = True)