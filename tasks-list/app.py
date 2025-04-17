from flask import Flask, render_template, request, redirect
from task import Task
from write_read_tasks import read_task_json, create_task_json
from topological_ordering import topological_sort

app = Flask(__name__)

# Inicialização com arquivo padrão
FILE_NAME = "tasks-list/tasks.json"
task_list = read_task_json(FILE_NAME)
cenario_atual = FILE_NAME  # para exibir no HTML qual cenário está em uso


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", tasks=task_list.values(), cenario_atual=cenario_atual)


@app.route("/criar", methods=['POST'])
def create_task():
    global task_list

    # Dados do formulário
    id = request.form['id']
    name = request.form['name']
    description = request.form['description']
    deps_itens = request.form.get('dependencies', '')

    dependencies = []
    for dependencie in deps_itens.split(","):
        dependencie = dependencie.strip()
        if dependencie:
            dependencies.append(dependencie)

    # Cria e adiciona a tarefa
    task = Task(id, name, description, dependencies)
    task_list[id] = task

    # (Opcional) Salva no JSON se quiser persistir
    # create_task_json(FILE_NAME, task_list)

    return redirect("/")


@app.route("/ordenar", methods=["GET"])
def ordenar_tarefas():
    try:
        ordenadas = topological_sort(task_list)
        tarefas_ordenadas = [task_list[id] for id in ordenadas]
        return render_template("ordenadas.html", tasks=tarefas_ordenadas)
    except ValueError as e:
        return f"<h2 style='color:red'>Erro: {e}</h2><br><a href='/'>Voltar</a>"


@app.route("/carregar-json", methods=["POST"])
def carregar_json():
    global task_list
    global cenario_atual

    escolha = request.form.get("cenario")

    if escolha == "ordenavel":
        arquivo = "cenarios/cenario_ordenavel.json"
    elif escolha == "com_ciclo":
        arquivo = "cenarios/cenario_com_ciclo.json"
    else:
        return "Cenário inválido", 400

    task_list = read_task_json(arquivo)
    cenario_atual = arquivo

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
