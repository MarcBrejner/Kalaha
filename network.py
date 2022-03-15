import socket


class Network:
    def __init__(self):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "127.0.0.1"
        self.port = 13000
        self.addr = (self.server, self.port)
        self.connect()

    def connect(self):
        try:
            self.connection.connect(self.addr)
        except:
            pass

    def take_turn(self, cup):
        try:
            self.connection.send(str.encode(cup))
        except socket.error as e:
            print(e)

    def get_game_state(self):
        try:
            self.connection.send(str.encode("getGameState"))
            return self.connection.recv(4096)
        except:
            pass

    def wait_for_turn(self):
        try:
            return self.connection.recv(2048).decode()
        except:
            pass

    def get_player_number(self):
        try:
            return self.connection.recv(2048).decode()
        except:
            pass

    def check_game_over(self):
        try:
            return self.connection.recv(2048).decode()
        except:
            pass