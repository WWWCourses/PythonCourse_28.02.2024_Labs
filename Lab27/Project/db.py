import json


filename = './data/clients.json'

def get_clients():
    with open(filename,'r') as f:
        clients = json.load(f)
        return clients


def save_clients(clients):
    print(clients)
    with open(filename, 'w') as f:
        json.dump(clients, f)
    # to JSON

