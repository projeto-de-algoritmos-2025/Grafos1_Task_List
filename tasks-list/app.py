from flask import Flask, render_template, request
from task import Task

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

task_list = {}

@app.route("/criar", methods=['POST'])
def create_task():

    name = request.form['name']
    description = request.form['description']

    task = Task(name,description)

    task_list[name] = task

    return f"A tarefa {name} foi cadastrada com sucesso, com a descrição {description}."


if __name__ == "__main__":
    app.run(debug=True)


