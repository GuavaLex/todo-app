import functions
import PySimpleGUI as sg

Label = sg.Text("Enter the todo")
input_box = sg.InputText(tooltip="Enter todo")
btn = sg.Button("Add")

window = sg.Window("My To-do App", layout=[[Label], [input_box ,btn ]])
window.read()
window.close()