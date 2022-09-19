from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('Style1.html')

@app.route('/Page2')
def homepage1():
    return render_template('/Style2.html')

if __name__== '__main__': 
    app.run(debug=False, host='0.0.0.0', port=80)
