
# rconsole.py
# -------------
# This script provides a simple command-line interface for connecting to a Source RCON server.
# It allows the user to input connection details, validates them, and then interactively send commands to the server.
#
# Main features:
# - Prompt user for server address, port, and password
# - Validate port input and use a default if invalid
# - Attempt to connect and authenticate with the server
# - Provide a command loop for sending RCON commands and displaying responses
# - Gracefully handle connection errors and user exit

import sys
from dataclasses import dataclass
from rcon.source import Client
import getpass

# Default port for Source RCON servers
DEFAULT_PORT = 27015
# Minimum allowed port number
PORT_MIN = 1
# Maximum allowed port number
PORT_MAX = 65535

@dataclass
class ConnectionData:
    """
    Data class to store connection information for the RCON server.
    Attributes:
        address (str): The IPv4 address of the server.
        port (int): The port number to connect to.
        password (str): The RCON password for authentication.
    """
    address: str
    port: int
    password: str

def validate_port(port: str, default: int = DEFAULT_PORT) -> int:
    """
    Validate the port input by the user. If invalid, return the default port.
    Args:
        port (str): The port input as a string.
        default (int): The default port to use if validation fails.
    Returns:
        int: A valid port number.
    """
    try:
        port_int: int = int(port)
        if PORT_MIN <= port_int <= PORT_MAX:
            return port_int
    except ValueError:
        pass
    print(f"\nUsing default port {default}.\n")
    return default

def handle_inputs() -> ConnectionData:
    """
    Prompt the user for server address, port, and password.
    Returns:
        ConnectionData: The collected connection information.
    """
    address: str = input("Enter address(IPv4): ")
    port_str: str = input(f"Enter port (default {DEFAULT_PORT}): ")
    password: str = getpass.getpass("Enter your password: ")
    port: int = validate_port(port_str)
    return ConnectionData(address, port, password)

def get_command() -> str:
    """
    Prompt the user for a command to send to the RCON server.
    Returns:
        str: The command entered by the user.
    Exits the program if the user types 'exit'.
    """
    command: str = input("¥: ")
    if command.strip().lower() == "exit":
        print("exiting...")
        sys.exit(0)
    return command

def execute_command(command: str, data: ConnectionData) -> str:
    """
    Send a command to the RCON server and return the response.
    Args:
        command (str): The command to send.
        data (ConnectionData): The connection information.
    Returns:
        str: The server's response.
    """
    with Client(data.address, data.port, passwd=data.password, timeout=3) as c:
        return c.run(command)

def mainloop(data: ConnectionData) -> None:
    """
    Main command loop. Continuously prompt the user for commands and display responses.
    Args:
        data (ConnectionData): The connection information.
    """
    while True:
        command:str = get_command()
        try: 
            response = execute_command(command, data)
            print(f"got following response: {response}")
        except Exception as e:
            print(f"Unexpected error.\n{e}")

def validate_connection(data: ConnectionData) -> bool:
    """
    Attempt to connect to the RCON server to validate credentials and connectivity.
    Args:
        data (ConnectionData): The connection information.
    Returns:
        bool: True if connection is successful, False otherwise.
    """
    try: 
        with Client(data.address, data.port, passwd=data.password, timeout=3) as c:
            return True
    except Exception:
        return False

def main() -> None: 
    """
    Main entry point. Handles user input, connection validation, and starts the command loop.
    """
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