from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')
    pass

@app.route('/classes')
def classes():
    return render_template('classes.html')
    pass


if __name__ == '__main__':
    app.run(debug=True)