import uuid


class Client:

    def __init__(self, name, company, email, position, uid=None):
        self.name = name
        self.company = company
        self.email = email 
        self.position = position
        self.uid = uid or uuid.uuid4() #Genera id unicas


    def to_dict(self):
        return vars(self) #Nos permite acceder a una representacion de nustro diccionario 

    @staticmethod #declaracion del esquema
    def schema():
        return ['name', 'company', 'email', 'position', 'uid']

