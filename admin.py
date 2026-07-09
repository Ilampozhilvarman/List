import tools

command_line = input("> ")
args = command_line.split()
command = args[0]
if len(args) == 3:
    if command == "new":
        tools.new_list(args[1], args[2])
    elif command == "push":
        tools.push_list_item(args[1], args[2])
    elif command == "":
        pass
elif len(args) == 2:
    if command == "":
        pass
    elif command == "":
        pass
