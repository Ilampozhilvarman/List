import subprocess
import os
import tools
clear_command = command = "cls" if os.name == "nt" else "clear"
command_line = input("> ")
args = command_line.split()
args_and_their_uses = {
    "new": "Create a new list",
    "push": "Add an item to a list",
    "delete": "Remove an item from a list",
    "update": "Update a list",
    "get": "Get a list",
    "del": "Delete a list",
    "rtl": "Get a list",
    "aci": "Get a list item",
    "clr": "Clear a list",
    "edit": "Edit an item in a list",
    "clear": "Clear the terminal",
}

command = args[0]
if len(args) == 3:
    if command == "new":
        tools.new_list(args[1], args[2])
    elif command == "push":
        tools.add_item(args[1], args[2])
    elif command == "delete":
        tools.remove_item(args[1], args[2])
    elif command == "update":
        tools.update_list(args[1], args[2])

elif len(args) == 2:
    if command == "rtl":
        tools.get_list(args[1])
    elif command == "del":
        tools.delete_list(args[1])
    elif command == "aci":
        tools.get_list_items(args[1])
    elif command == "clr":
        tools.clear_list(args[1])

elif len(args) == 3:
    if command == "edit":
        tools.edit_item(args[1], args[2], args[3])

elif len(args) == 1:
    if command == "clear":
        subprocess.run([clear_command])
    elif command == "help":
        for command, use in args_and_their_uses.items():
            print(f"{command}: {use}")
