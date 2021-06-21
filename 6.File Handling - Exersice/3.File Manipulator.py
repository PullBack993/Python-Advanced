import os

def create_file(*f_name):
    file_name = f_name[0]
    with open(file_name, 'a') as file:
        file.write("")

def add_content(*f_content):
    file_name = f_content[0]
    content = f_content[1]
    with open(file_name, 'a') as file:
        file.write(content + '\n')

def replace_text(*data_to_replaced):
    name, old, new = data_to_replaced
    try:
        with open(name, 'r+') as file:
            reader = file.read()
            updated = reader.replace(old, new)
            file.seek(0)
            file.write(updated)
    except FileNotFoundError:
        print(ERROR_MSG)

def delete_file(*f_del):
    name = f_del[0]
    if os.path.exists(name):
        os.remove(name)
    else:
        print(ERROR_MSG)

ERROR_MSG = 'An error occurred'
END_COMMAND = 'End'

mapper = {
    'Create': create_file,
    'Add': add_content,
    'Replace': replace_text,
    'Delete': delete_file,
}

while True:
    command = input()
    if command == END_COMMAND:
        break
    action, *args = command.split('-')
    mapper[action](*args)