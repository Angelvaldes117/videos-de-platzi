import click

from clients.services import ClientService
from clients.models import Client

@click.group()
def clients():
    """Manages the clients lifecycle""" #Gestiona el ciclo de vida de los clintes
    pass

@clients.command()
@click.option('-n', '--name',
                type=str,
                prompt=True,
                help='The client name')#Nombre del cliente
@click.option('-c', '--company', #compañia
                type=str,
                prompt=True,
                help='The client company')#La empresa del cliente
@click.option('-e', '--email',
                type=str,
                prompt=True,
                help='The client email') #email del cliente
@click.option('-p', '--position',
                type=str,
                prompt=True,
                help='The client position') #posicion del usuario
@click.pass_context
def create(ctx, name, company, email, position):
    """Creates a new client"""
    client = Client(name, company, email, position)
    client_service = ClientService(ctx.obj['clients_table'])
    client_service.create_client(client)



@clients.command()
@click.pass_context
def list(ctx):
    """List all clients"""
    client_service = ClientService(ctx.obj['clients_table'])

    clients_list = client_service.list_clients()


    click.echo(' ID  |  NAME | COMPANY | EMAIL | POSITION')
    click.echo('*' * 100)

    for client in clients_list:
        click.echo('{uid} | {name} | {company} | {email} | {position}'. format(
            uid=client['uid'],
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position']))

@clients.command()
@click.argument('client_uid',
                type=str)
@click.pass_context
def update(ctx, client_uid):
    """Updates a single client"""
    client_service = ClientService(ctx.obj['clients_table'])

    client = [client for client in client_service.list_clients() if client['uid'] == client_uid]
    
    if client:
        client = _update_client_flow(Client(**client[0]))
        client_service.update_client(client)

        click.echo('cliente actualizado')
    else:
        click.echo('Client not found')


def _update_client_flow(client):
    click.echo('dejelo vacio para no cambiar el dato')

    client.name = click.prompt('Nuevo name', type=str, default=client.name)
    client.company = click.prompt('Nuevo company', type=str, default=client.company)
    client.email = click.prompt('Nuevo email', type=str, default=client.email)
    client.position = click.prompt('Nuevo position', type=str, default=client.position)

    return client


@clients.command()
@click.argument('client_uid',
                type=str)
@click.pass_context
def delete(ctx, client_uid):
    """Deletes a client"""
    client_service = ClientService(ctx.obj['clients_table'])

    if click.confirm('estas seguro que desea elimanr el cliente con el id: {}'.format(client_uid)):
        client_service.delete_client(client_uid)


all = clients