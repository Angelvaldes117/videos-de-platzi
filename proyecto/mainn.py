import sys
import os
import csv

CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
clients = []

def _initilize_clients_from_storage():
    with open(CLIENT_TABLE, mode='r') as f: 
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

        for row in reader: 
            clients.append(row)


def _save_clients_to_storage(): #Arreglo 
    tmp_table_name = '{}.tmp'.format(CLIENT_TABLE)
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA)
        writer.writerows(clients)

        os.remove(CLIENT_TABLE) #podemos inicializar de  nuestro archivo  
        os.rename(tmp_table_name, CLIENT_TABLE) #podemos guadarlo en nuestro archivo 




def create_client(client):
    global clients  # vamos a utilizar la palabra global y la utilizaremos dentro de nuestra funcion
    if client not in clients: #Se agg a la lista el nombre que ingresamos
        clients.append(client)
    else:
        print('El cliente ya ha sido agregado a la lista')


def list_clients():
    print('uid |  name  | company  | email  | position ')
    print('*' * 50)

    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx,
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position'])) 


def update_client(client_id, update_client):
    global clients
    if len(clients) -1 >= client_id:
        clients[client_id] = update_client
    else:
        print('El cliente no se encuentra')


def delete_client(client_id):
    global clients

    for idx, client in enumerate(clients):
        if idx == client_id:
            del clients[idx]
            break


def search_client(client_name):
    for client in clients:
        if client['name'] != client_name:
            continue
        else:
            return True


def _get_client_field(field_name, message=('¿Cuál es el {} del cliente?')):
        field = None

        while not field: 
            field = input(message.format(field_name))

        return field


def _get_client_from_user():
    client = {
        'name': _get_client_field('Nombre'),
        'company': _get_client_field('Empresa'),
        'email': _get_client_field('Correo'),
        'position': _get_client_field('Puesto'),
        }

    return client



def _print_welcome():
    print('BIENBENIDO A MI PAGINA')
    print('-' * 50)
    print('QUE ES LO QUE DESEAS HACER ')
    print('[C]Crear cliente') #Crear cliente
    print('[U]actualizar cliente') #Actualizar lista
    print('[D]Borrar cliente') #Borrar cliente
    print('[S]Buscar cliente') #Buscar cliente
    print('[L]Lista de cliente') #Lista cliente


if __name__ == '__main__':
    _initilize_clients_from_storage()
    _print_welcome() # preguntamos al ususario como se llama la persona que desea añadir a la lista


    command = input() #Combertimos en mayuscula
    command = command.upper()

      

    if command == 'C':
        client = _get_client_from_user()

        create_client(client)

    elif command == 'D':
        client_id = int(_get_client_field('id'))

        delete_client(client_id)

    elif command == 'L':
        list_clients()

    elif command == 'U':
        client_id = int(_get_client_field('id'))
        updated_client = _get_client_from_user()

        update_client(client_id, updated_client)

    elif command == 'S':
        client_name = _get_client_field('Nombre')
        found = search_client(client_name)
        
        if found:
            print('El cliente ya esta en la lista de clientes')
        else:
            print('El cliente: {} no se encuentra en nuestra lista de clientes'.format(client_name))
    else:
        print('Comando Invalido')
        

    _save_clients_to_storage()

