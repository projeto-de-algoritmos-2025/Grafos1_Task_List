
def topological_sort(task_list):
    # cada chave é uma tarefa e os valores são as tarefas que dependem dela
    graph = {}
    # Dicionário com o número de dependências (grau de entrada-"setas chegando no nó") de cada tarefa
    in_degree = {}

    #inicializando o grafo e os graus de entrada
    for task in task_list.values():
        graph[task.id] = []
        in_degree[task.id] = 0
    
    #: fila de tarefas que não têm dependências
    queue = []

    #Alimenta o dicionário graph e in_degree
    for id, task in task_list.items():
        graph[task.id] = {"dependencies": task.dependencies}
        node_deps = task.dependencies.__len__()
        in_degree[task.id] = {"node_dependencies": node_deps}

        if not(task.dependencies):
            queue.append(task.id)

    sorted_tasks = []

    # TODO: Processar a fila e construir a ordenação topológica
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