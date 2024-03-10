def get_todos(local_filepath="todos.txt"):
    """ get list from textfile. just paste full path here: local_filepath """
    with open(local_filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, local_filepath="todos.txt"):
    """ safe new list into the file """
    with open(local_filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("hello from functions")
    print(get_todos())

