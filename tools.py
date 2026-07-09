import json

def get_file_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def save_file_data(data):
    with open("data.json", 'w') as file:
        json.dump(data, file)

def new_list(list_name, id):
    data = get_file_data("data.json")
    data[list_name] = {"data": [], "name": list_name, "id": id}
    save_file_data(data)

def get_list(list_name):
    data = get_file_data("data.json")
    return data[list_name]

def delete_list(list_name):
    data = get_file_data("data.json")
    del data[list_name]
    save_file_data(data)

def update_list(list_name, new_data):
    data = get_file_data("data.json")
    data[list_name] = new_data
    save_file_data(data)

def add_item(list_name, item):
    data = get_file_data("data.json")
    data[list_name]["data"].append(item)
    save_file_data(data)

def remove_item(list_name, item):
    data = get_file_data("data.json")
    data[list_name]["data"].remove(item)
    save_file_data(data)

def edit_item(list_name, item, new_item):
    data = get_file_data("data.json")
    index = data[list_name]["data"].index(item)
    if data[list_name]["data"][index]:
        data[list_name]["data"][index] = new_item
    else:
        raise Exception("Item not found in list")
    save_file_data(data)

def get_list_items(list_name):
    data = get_file_data("data.json")
    return data[list_name]["data"]

def clear_list(list_name):
    data = get_file_data("data.json")
    data[list_name]["data"] = []
    save_file_data(data)
