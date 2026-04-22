import streamlit as st


st.title("Calculator")

num1=st.number_input("enter number 1")
num2=st.number_input("enter number 2")

operation=st.selectbox("select operation",["addition","subtraction","multiplication"])


if st.button("Submit"):
    if operation == "addition":
        sum=num1 + num2
        st.divider()
        st.success(f"sum : {sum}")

    elif operation == "subtraction":
        diff=num1-num2
        st.divider()
        st.warning(f"diff : {diff}")
    
    elif operation == "multiplication":
        multiply=num1 * num2
        st.divider()
        st.warning(f"Product: {multiply}")
