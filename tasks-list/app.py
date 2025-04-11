from flask import Flask, render_template, request, jsonify, redirect
from task import Task

app = Flask(__name__)

task_list = {}

@app.route("/")
def home():
    return render_template("index.html", tasks=task_list.values())


@app.route("/criar", methods=['POST'])
def create_task():

    id = request.form['id']
    name =request.form['name']
    description = request.form['description']


    task = Task(id,name,description)
    task_list[name] = task

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)


