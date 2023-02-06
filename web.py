import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my todo app")
st.write("This app is created to increase your productivity")

for index,i in enumerate(todos):
    checkbox = st.checkbox(i,key=i)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[i]
        st._rerun()

st.text_input(label="", placeholder="Add a new todo", on_change= add_todo, key= "new_todo")
