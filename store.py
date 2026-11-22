FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as todo_file:
        stored_todos = todo_file.readlines()
    return stored_todos

def write_todos(new_todos, filepath=FILEPATH):
    """ Write the list of to-do items to a text file."""
    with open(filepath, 'w') as todo_file:
        todo_file.writelines(new_todos)

if __name__ == "__main__":
    print(__name__)