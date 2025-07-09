import sys
from dataclasses import dataclass
from rcon.source import Client
import getpass

DEFAULT_PORT = 27015
PORT_MIN = 1
PORT_MAX = 65535

@dataclass
class ConnectionData:
    address: str
    port: int
    password: str

def validate_port(port: str, default: int = DEFAULT_PORT) -> int:
    try:
        port_int: int = int(port)
        if PORT_MIN <= port_int <= PORT_MAX:
            return port_int
    except ValueError:
        pass
    print(f"\nUsing default port {default}.\n")
    return default

def handle_inputs() -> ConnectionData:
    address: str = input("Enter address(IPv4): ")
    port_str: str = input(f"Enter port (default {DEFAULT_PORT}): ")
    password: str = getpass.getpass("Enter your password: ")
    port: int = validate_port(port_str)
    return ConnectionData(address, port, password)

def get_command() -> str:
    command: str = input("¥: ")
    if command.strip().lower() == "exit":
        print("exiting...")
        sys.exit(0)
    return command

def execute_command(command: str, data: ConnectionData) -> str:
    with Client(data.address, data.port, passwd=data.password, timeout=3) as c:
        return c.run(command)

def mainloop(data: ConnectionData) -> None:
    while True:
        command:str = get_command()
        try: 
            response = execute_command(command, data)
            print(f"got following response: {response}")
        except Exception as e:
            print(f"Unexpected error.\n{e}")

def validate_connection(data: ConnectionData) -> bool:
    try: 
        with Client(data.address, data.port, passwd=data.password, timeout=3) as c:
            return True
    except Exception:
        return False

def main() -> None: 
    try:
        while True:
            user_data: ConnectionData = handle_inputs()
            if validate_connection(user_data):
                print("connection successful.")
                break
            print("wrong credentials or no connection possible. please try again.")
        mainloop(user_data)
    except KeyboardInterrupt:
        print("exiting...")

if __name__ == "__main__":
    main()