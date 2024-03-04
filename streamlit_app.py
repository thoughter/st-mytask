import os
import streamlit as st


if('tasks' not in st.session_state):
    st.session_state.tasks=[]

def submit():
    st.session_state.tasks.append(st.session_state.task_input)    
    st.session_state.task_input=''
    
st.title('My Task')

task=st.text_input('Enter a task',key="task_input",on_change=submit)

for i, t in enumerate(st.session_state.tasks):
    st.checkbox(t,key=i)

