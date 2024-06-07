from db import get_clients, save_clients

# Load data:
clients = get_clients()

# Manipulate data
# clients.pop()
client  = {
    'name': 'Maria',
    'pin':'0002'
}

clients.append(client)

# Save data
save_clients(clients)

