import os
import json
from task import Task

def read_task_json(name_file):

    if os.path.exists(name_file) and os.path.getsize(name_file) > 0:
        with open(name_file, "r", encoding="utf-8") as f:
            dados = json.load(f)
        return{id: Task.from_dict(t) for id, t in dados.items() }

    return{}

def create_task_json(name_file,task):
    with open(name_file,"w", encoding="utf-8") as f:
        dados = {id: t.to_dict() for id, t in task.items() }
        json.dump(dados, f, indent=4, ensure_ascii=False)
    


