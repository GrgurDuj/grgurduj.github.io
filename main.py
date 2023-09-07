from flask import Flask

app = Flask("main")

@app.route("/main")
def hello_world():
    return "Hello, World!"