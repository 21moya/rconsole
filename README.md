# rconsole 🚀

rconsole is a command-line tool that provides an interactive shell for sending RCON commands to servers that support the Source RCON protocol, such as game servers like Counter-Strike, Team Fortress 2, and others. 🎮

## Features ✨

- Interactive command-line interface for sending RCON commands
- Easy connection setup with server address, port, and password 🔐
- Default port handling (27015)
- Secure password input
- Ability to send multiple commands in a single session
- Exit the shell by typing "exit" 🛑

## Requirements 📋

- Python 3.7 or higher
- `rcon` library

## Installation 🛠️

1. Ensure you have Python 3.7 or higher installed.
2. Install the required library using pip:

```
pip install rcon
```

## Usage 🎯

1. Run the script:

```
python rconsole.py
```

2. Follow the prompts:
   - Enter the server address (IPv4).
   - Enter the port (default is 27015; press Enter to use default).
   - Enter the RCON password (input is hidden).

3. If the connection is successful, you will see a prompt `¥:`. Enter your RCON commands here.
4. To exit, type `exit`.

If the connection fails (e.g., due to wrong credentials or no connection possible), you will be prompted to try again.

### Example 📝

```
Enter address(IPv4): 192.168.1.100
Enter port (default 27015): 27016
Enter your password: 
connection successful.
¥: status
got following response: hostname: My Server
version : 1.0.0
...
¥: exit
exiting...
```

## Building an Executable 💻

If you are on Windows and want to create a standalone executable, you can use [auto-py-to-exe](https://pypi.org/project/auto-py-to-exe/). This tool packages the script into a single executable file that can be run on machines without Python installed. 🖥️

1. Install auto-py-to-exe:

```
pip install auto-py-to-exe
```

2. Run the tool:

```
auto-py-to-exe
```

3. In the GUI, select the script file (e.g., `rconsole.py`).
4. Configure the build options as needed (e.g., one-file mode).
5. Click "Convert" to generate the executable.

For more details, refer to the [auto-py-to-exe documentation](https://pypi.org/project/auto-py-to-exe/).