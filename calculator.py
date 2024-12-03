import streamlit as st

st.title("Gen-Z Calculator")

n1 = st.text_input('', 'Enter first number here')
n1 = float(n1)

n2 = st.text_input('Second number')
n2 = float(n2)

op = st.selectbox("Operator", ['multiply','add','subtract','divide'])

if op is 'multiply':
    ans = n1 * n2
elif op is 'divide':
    ans = n1/n2
elif op is 'add':
    ans = n1+n2
else:
    ans = n1-n2

st.write('Your answer is: ', ans)

