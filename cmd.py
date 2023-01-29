import time
from functions import *

now = time.strftime("%b %d, %Y %H:%M %S")
print("It is",now)
while True:
    user_prompt = input("type add,show,edit,complete or exit ")
    user_prompt = user_prompt.strip()


    if user_prompt.startswith("add"):
        todo = user_prompt[4:] + "\n"

        todos = get_todos()

        todos.append(todo)

        write_todos(todos)

    elif user_prompt.startswith("show"):
        todos = get_todos()

        for index, items in enumerate(todos):
            items = items.strip("\n")
            index = index + 1
            row = f"{index}.{items}"
            print(row)


    elif user_prompt.startswith("edit"):
        try:
            edit_number = int(user_prompt[5:])
            edit_number = edit_number - 1

            todos = get_todos()


            edit_data = input("Enter new todo")
            todos[edit_number] = edit_data + "\n"

            write_todos(todos)


        except ValueError:
            print("Your command is not valid")
            continue
    elif user_prompt.startswith("complete"):
        try:
            no = int(user_prompt[9:])

            todos = get_todos()

            index = no - 1
            todo_to_remove = todos[index]
            todos.pop(index)

            write_todos(todos)

        except IndexError:
            print("There is no item with that number")
            continue

            message = f"Todo {todo_to_remove} was removed"
            print(message)
    elif user_prompt.startswith("exit"):
        break
    else:
        print("command not valid")
print("bye")

