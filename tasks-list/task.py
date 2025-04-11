class Task:
      def __init__(self,id, name, description, dependencies = None):
        self.id = id
        self.name = name
        self.description = description
        self.dependencies = dependencies or [] # se for None, vira []
        
