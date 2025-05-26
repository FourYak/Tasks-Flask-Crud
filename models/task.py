class Task: # Classe que define os atributos de uma Task
    def __init__(self, id, title, description, completed = False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed
    
    def to_dict(self): # Método que converte as informações da classe em um dicionário
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }