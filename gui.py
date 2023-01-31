import functions
import PySimpleGUI as sg

Label = sg.Text("Enter the todo")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_btn = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="items", enable_events=True, size=[40,10])

edit_btn = sg.Button("Edit")

window = sg.Window("My To-do App",
                   layout=[[Label], [input_box,add_btn], [list_box,edit_btn]],
                   font=("Helvetica", 20))



todos = functions.get_todos()
while True:
    event, value = window.read()
    if event is None or value is None:
        break
    print(1,event)
    print(2,value)
    print(3,value['items'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todos = value["todo"] + "\n"
            todos.append(new_todos)
            functions.write_todos(todos)
            window['items'].update(values=todos)
        case "Edit":
            todo_to_edit = value['items'][0]
            new_todos = value['todo']
            index = todos.index(todo_to_edit)
            todos[index] = new_todos
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()