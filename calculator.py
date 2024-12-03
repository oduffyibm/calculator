import random as r
import streamlit as st

def main():
  st.title("Gen-Z Calculator")
  
  n1 = st.number_input('First number here', value = 0)
  
  n2 = st.text_input('Second number here', value = 0)
  
  op = st.selectbox('Operator:',['multiply','divide','add','subtract'], on_change = genz())

  calculate(int(n1),int(n2),op)

def calculate(n1,n2,op):
  if op is 'multiply':
      ans = n1 * n2
  elif op is 'divide':
      ans = n1/n2
  elif op is 'add':
      ans = n1+n2
  else:
      ans = n1-n2

    st.write('Your answer is: ', str(ans))

def genz():
  saying = r.choose(['Rizz','On God','The Rizzler','That\'s Cap','Betski','Ruski'])
  st.write(saying)

main()
