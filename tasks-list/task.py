class Task:
      def __init__(self,id, name, description, dependencies = None):
        self.id = id
        self.name = name
        self.description = description
        self.dependencies = dependencies or [] # se for None, vira []
        
      def to_dict(self):
          return{
              "id":self.id,
              "name": self.name,
              "description":self.description,
              "dependencies": self.dependencies
          }
      
      def from_dict(dict):
          return Task(dict["id"],dict["name"],dict["description"],dict["dependencies"])