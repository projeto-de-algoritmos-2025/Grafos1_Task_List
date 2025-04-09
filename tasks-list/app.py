from flask import Flask, render_template
from task import Task

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("criar")
def create_task():
    task = Task(name, description, precedency)
    return 


if __name__ == "__main__":
    app.run(debug=True)


