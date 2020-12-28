class Subscriber:
    def __init__(self):
        self.clients = []
        self.send_message = None

    def add_client(self, client):
        if type(client) != str:
            raise TypeError("Client is not a string!")
        if client in self.clients:
            raise ValueError("Client already exists!")
        self.clients.append(client)
        return self.clients

    def remove_client(self, client):
        if type(client) != str:
            raise TypeError("Client is not a string!")
        self.clients.remove(client)
        return self.clients

    def send_message_to_client(self, client, message):
        if type(client) != str or type(message) != str:
            raise TypeError("Client or message is not a string!")
        if client not in self.clients:
            raise ValueError("Client doesn't exist!")
        return self.send_message(client, message)
