"""
server/chatroom.py

Contains the implementation of the "Chatroom" class, which manages a set of
connections and the publishing of new messages to the clients.
"""
from utils.constants import DEFAULT_PORT

import socket
import threading

class Chatroom:
    def __init__(self):
        # Set up the socket that clients connect to
        self.server_socket = socket.socket()
        hostname = socket.gethostname()
        port = DEFAULT_PORT
        self.server_socket.bind( (hostname, port) )

        # Start the listening process for clients
        self.threads = []
        self.isChatroomActive = True

        # Loop continuously until chatroom is deactivated
        while self.isChatroomActive:
            self.listenForClient()

    def listenForClient(self):
        '''
        Continuously checks for new clients, initializes them if detected.
        '''
        # NOTE: The following is BLOCKING!
        connection, address = self.server_socket.accept()
        client_thread = threading.Thread(target=self.onNewClient, args=(connection, address))
        self.threads.append(client_thread)

    def onNewClient(self, client_socket: socket.socket, address):
        '''
        Called any time a new client connects to the server.
        '''
        is_client_active = True
        while is_client_active:
            client_msg = client_socket.recv(1024)
            if str(client_msg) == '/exit':
                # User wants to exit chatroom, so client is no longer active
                is_client_active = False
            else:
                # TODO: Add message to chatroom
                # TODO: Send message out to all clients
                print(address, '>>', str(client_msg))
            
