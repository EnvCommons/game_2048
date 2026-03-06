from openreward.environments import Server
from env import Game2048Environment

if __name__ == "__main__":
    server = Server([Game2048Environment])
    server.run()
