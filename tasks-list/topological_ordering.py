from write_read_tasks import create_task_json , read_task_json
from task import Task

def topological_sort(task_list):
    # cada chave é uma tarefa e os valores são as tarefas que dependem dela
    graph = {}
    # Dicionário com o número de dependências (grau de entrada-"setas chegando no nó") de cada tarefa
    in_degree = {}

    #inicializando o grafo e os graus de entrada
    for task in task_list.values():
        graph[task.id] = []
        in_degree[task.id] = 0

    # TODO: criar um for para preencher o graph(os IDs de dependencias de cada task sendo a CHAVE e o VALOR sendo as tarefas que dependem desse ID)
    ### ao final somar 1 no valor do ID da tarefa no in_degree
    

    sorted_tasks = []

    for id, task in task_list.items():
        graph[task.id] = {"dependencies": task.dependencies}
        node_deps = task.dependencies
        node_deps = node_deps.__len__()
        in_degree[task.id] = {"node_dependencies": node_deps}

        if not(task.dependencies):
            sorted_tasks.append(task.id)

   


    # TODO: fila de tarefas que não têm dependências
    
    ## supondo que tenha um array chamado 'queue'

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