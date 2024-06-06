# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template, redirect
import x
import db

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def home():

    return render_template('index.html')

@app.route('/details')
def details():
    data =  db.retrieve()
    show = [] 
    for i in data:
        show.append(i['trend'])

    return render_template('details.html', show= show)
# main driver function
@app.route('/run')
def run():
    x.main()

    return redirect('/details')

if __name__ == '__main__':

    # run() method of Flask class runs the application 
    # on the local development server.
    app.run(port=5000)
