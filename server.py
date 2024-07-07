# backend-repo/server.py

import yaml

class Server:
    def __init__(self, config_file):
        with open(config_file, 'r') as file:
            self.config = yaml.safe_load(file)
    
    def print_server_ip(self):
        print(f"Server IP Address: {self.config['ServerIPAddress']}")

if __name__ == "__main__":
    server = Server('path/to/config.yaml')
    server.print_server_ip()
