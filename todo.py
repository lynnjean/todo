import streamlit as st

# st.write('helloworld2')

if 'todos' not in st.session_state:
    st.session_state.todos=[]

new_todo = st.text_input("할일을 입력하세요:",
                         placeholder="예: 장보기, 운동하기, 책읽기")
submitted = st.button("추가하기")

# st.write('new_todo:',new_todo, 'submitted:',submitted)

if submitted: # 버튼을 눌렀을때
    st.session_state.todos.append({
        'task':new_todo,
        'completed':False
    })
    st.success(f"{new_todo}가 추가되었습니다.")

st.divider() # 구분선 추가

# st.write(st.session_state.todos)

if st.session_state.todos:
    for i in range(len(st.session_state.todos)):
        # st.write(i)
        todo = st.session_state.todos[i]
        # st.write(todo)
        col1, col2, col3 = st.columns([0.1,0.7,0.2])
        
        with col1:
            completed = st.checkbox("", value=todo['completed'], key=f"ckeck_{i}")
            # st.write(completed)     

            if completed != todo['completed']:
                st.session_state.todos[i]['completed']=completed
                st.rerun()

        with col2:
            if completed:
                st.markdown(f"~~{todo['task']}~~")
            else:
                st.write(todo['task'])
        
        with col3:
            if st.button("🗑️", key=f"delete_{i}"):
                st.session_state.todos.pop(i)
                st.success('삭제되었습니다.')
                st.rerun()

        if i>=0:
            st.markdown('---')
else:
    st.info('아직 할일이 없습니다. 새로운 할일을 추가해보세요.')
