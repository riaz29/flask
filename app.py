from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html', name="riaz")

@app.route('/about')
def about():
    return render_template('about.html',about = "We are IT Professional")

if __name__ == '__main__':
   app.run()