from flask import Flask, render_template, request, jsonify, redirect
from task import Task
from write_read_tasks import read_task_json, create_task_json

app = Flask(__name__)

FILE_NAME = "tasks-list/tasks.json"

task_list = read_task_json(FILE_NAME)

@app.route("/",methods=["GET"])
def home():
    return render_template("index.html", tasks=task_list.values())


@app.route("/criar", methods=['POST'])
def create_task():

    #resgata dados do form
    id = request.form['id']
    name =request.form['name']
    description = request.form['description']
    deps_itens = request.form.get('dependencies', '')

    dependencies = []

    # de "1, 3, 4,5 , " vai para [1,3,4,5]
    for dependencie in deps_itens.split(","):
        dependencie = dependencie.strip()
        if dependencie:
            dependencies.append(dependencie)

    task = Task(id,name,description, dependencies)
    task_list[id] = task

    create_task_json(FILE_NAME,task_list)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)


