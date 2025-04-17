from write_read_tasks import read_task_json


def topological_sort(task_list):
    # cada chave é uma tarefa e os valores são as tarefas que dependem dela
    graph = {}
    # Dicionário com o número de dependências (grau de entrada-"setas chegando no nó") de cada tarefa
    in_degree = {}
    #Lista de candidatos com grau 0
    queue = []
    #Lista da ordenação topológica
    sorted_tasks = []

    #inicializando o grafo e os graus de entrada
    for task in task_list.values():
        graph[task.id] = []
        in_degree[task.id] = 0

    # Cria chves com o ids dos nós e os nós que dependem deste
    for task in task_list.values():
        for dep in task.dependencies:
            graph[dep].append(task.id)
            in_degree[task.id] += 1

    # Cria um array com os nós candidatos com grau 0
    queue = [task_id for task_id, deg in in_degree.items() if deg == 0]

    # Realiza um loop que faz a ordenação topológica decrementando uma unidade dos nós dependentes do nó candidato sendo iterado
    while queue:
        current = queue.pop(0)
        sorted_tasks.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
        
    # Verificação de ciclo: se não ordenou tudo, tem dependência circular
    if len(sorted_tasks) != len(task_list):
        raise ValueError("Ciclo detectado! Não é possível ordenar as tarefas.")

    return sorted_tasks