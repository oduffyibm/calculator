
import streamlit as st

#def main():
st.title("Gen-Z Calculator")

n1 = st.number_input('First number here')

n2 = st.text_input('Second number here')

op = st.selectbox("Operator", ['multiply','add','subtract','divide'],on_change=calculate(n1,n2,op))


#def calculate(n1,n2,op):
#    if op is 'multiply':
#        ans = n1 * n2
#    elif op is 'divide':
##        ans = n1/n2
#    elif op is 'add':
#        ans = n1+n2
#    else:
#        ans = n1-n2

#    st.write('Your answer is: ', ans)

#main()
