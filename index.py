from flask import Flask

app = Flask (__name__)

@app.route('/')
def index():
    return 'Hola'
    pass

if __name__ == '__name__':
    app.run()