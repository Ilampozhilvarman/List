import subprocess
import os
import tools

clear_command = "cls" if os.name == "nt" else "clear"

args_and_their_uses = {
    "new":    {"args": ["list_name", "list_type"], "desc": "Create a new list"},
    "push":   {"args": ["list_name", "item"], "desc": "Add an item to a list"},
    "delete": {"args": ["list_name", "item"], "desc": "Remove an item from a list"},
    "update": {"args": ["list_name", "value"], "desc": "Update a list"},
    "get":    {"args": ["list_name"], "desc": "Get a list"},
    "del":    {"args": ["list_name"], "desc": "Delete a list"},
    "rtl":    {"args": ["list_name"], "desc": "Get a list"},
    "aci":    {"args": ["list_name"], "desc": "Get a list item"},
    "emp":    {"args": ["list_name"], "desc": "Clear a list"},
    "edit":   {"args": ["list_name", "item", "new_value"], "desc": "Edit an item in a list"},
    "clr":    {"args": [], "desc": "Clear the terminal"},
    "exit":   {"args": [], "desc": "Quit the program"},
}

while True:
    command_line = input("> ").strip()
    if not command_line:
        continue

    args = command_line.split()
    command = args[0]

    try:
        if command == "exit":
            break
        elif len(args) == 3:
            if command == "new":
                tools.new_list(args[1], args[2])
            elif command == "push":
                tools.add_item(args[1], args[2])
            elif command == "delete":
                tools.remove_item(args[1], args[2])
            elif command == "update":
                tools.update_list(args[1], args[2])
            else:
                print("Invalid command")
        elif len(args) == 2:
            if command == "rtl":
                tools.get_list(args[1])
            elif command == "del":
                tools.delete_list(args[1])
            elif command == "aci":
                tools.get_list_items(args[1])
            elif command == "emp":
                tools.clear_list(args[1])
            else:
                print("Invalid command")
        elif len(args) == 4:
            if command == "edit":
                tools.edit_item(args[1], args[2], args[3])
            else:
                print("Invalid command")
        elif len(args) == 1:
            if command == "clr":
                subprocess.run([clear_command], shell=(os.name == "nt"))
            elif command == "help":
                print("\n   Command line arguments:")
                for cmd, info in args_and_their_uses.items():
                    arg_str = " " + " ".join(f"<{a}>" for a in info["args"]) if info["args"] else ""
                    print(f"{cmd}{arg_str}: {info['desc']}")
            elif command == "end":
                print("\nSession ended")
                break
            else:
                print("Invalid command")
        else:
            print("Invalid command")
    except Exception as e:
        print(f"Error: {e}")
