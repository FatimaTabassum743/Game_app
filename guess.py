import streamlit as st
import random

st.title("Guess the number Game")
Random_number=random.randint(1,10)
guess=st.number_input("Enter your guess Number: ",min_value=1, max_value=10, step=1)
if st.button("Check"):
   if guess==Random_number:
      st.header("Congratulations! You guessed the number correctly.")
   elif guess<Random_number:
      st.header("Too low! Try again.")
   else:
      st.header("Too high! Try again.")

st.title("Age Group Classifier")
age=st.number_input("Enter your age: ",min_value=1, max_value=110, step=1)
if age<10:
    st.header("You are a child.")
elif age<20:
    st.header("You are a teenager.")  
else:
    st.header("You are an adult.")      