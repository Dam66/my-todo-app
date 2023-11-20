import streamlit as st
import func1

todos = func1.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    func1.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my to do app")
st.write("This app is to help improve your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        func1.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Enter a to do..",
              on_change=add_todo, key="new_todo")