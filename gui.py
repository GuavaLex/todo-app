import functions
import PySimpleGUI as sg

Label = sg.Text("Enter the todo")
input_box = sg.InputText(tooltip="Enter todo", key = "todo")
btn = sg.Button("Add")

window = sg.Window("My To-do App",
                   layout=[[Label], [input_box ,btn ]],
                   font=("Helvetica", 20))
while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todos = value["todo"] + "\n"
            todos.append(new_todos)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()