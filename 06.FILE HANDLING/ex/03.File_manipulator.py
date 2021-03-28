import os


def delete_file(file_name):
    try:
        os.remove(file_name)
    except FileNotFoundError:
        print("An error occurred")


def replace_content(file_name, old_content, new_content):
    try:
        with open(file_name, "r+") as file:
            text = ''.join(file.readlines())
            replaced = text.replace(old_content, new_content)
            file.seek(0)
            file.write(replaced)
    except FileNotFoundError:
        print("An error occurred")


def add_content(file_name, content):
    if os.path.exists(file_name):
        with open(file_name, "a") as file:
            file.write(content + '\n')
    else:
        with open(file_name, "w") as file:
            file.write(content)


def create_file(file_name):
    with open(file_name, "w") as file:
        file.write("")


actioner = {
            "Create": create_file,
            "Add": add_content,
            "Replace": replace_content,
            "Delete": delete_file,
            }


def start_engine():
    command_data = input().split("-")
    while not command_data[0] == "End":
        command, command_args = command_data[0], command_data[1:]
        actioner[command](*command_args)
        command_data = input().split("-")


start_engine()