from flask import Flask, render_template, request, jsonify
from task import Task

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

task_list = {}

@app.route("/criar", methods=['POST'])
def create_task():


    id = request.form['id']
    name =request.form['name']
    description = request.form['description']


    task = Task(id,name,description)

    task_list[name] = task

    return f"{id} {name} {description}"

if __name__ == "__main__":
    app.run(debug=True)


