class Task:
      def __init__(self, name, description, precedency = None,subsequence = None):
        self.name = name
        self.description = description
        self.precedency = precedency
        self.subsequence = subsequence
