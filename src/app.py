from flask import Flask

app = Flask(__name__)

@app.route('/')
def helloWorld():
    return {
        "message": "Hello guys, this is Kigali babes!"
    }


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
