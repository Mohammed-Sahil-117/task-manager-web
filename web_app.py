import streamlit as st
import store

todos = store.get_todos()

def update_todo_list():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    store.write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("The To-Do App")
st.subheader("My To-Do List")
st.write("A step towards increasing my productivity")


for index, todo in enumerate(todos):
    checked = st.checkbox(todo, key=todo)
    if checked:
        todos.pop(index)
        store.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

# pyrefly: ignore[no-matching-overload]
st.text_input(label='Enter a todo', placeholder='Add new todos....',
              key='new_todo', on_change=update_todo_list, label_visibility='hidden')