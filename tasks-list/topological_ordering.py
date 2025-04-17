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



    # TODO: fila de tarefas que não têm dependências
    
    sorted_tasks = []

    # TODO: Processar a fila e construir a ordenação topológica


    # Verificação de ciclo: se não ordenou tudo, tem dependência circular
    if len(sorted_tasks) != len(task_list):
        raise ValueError("Ciclo detectado! Não é possível ordenar as tarefas.")

    return sorted_tasks
