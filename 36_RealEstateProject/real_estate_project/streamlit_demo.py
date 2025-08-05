import streamlit as st

st.title("Streamlit Demo by Bipul")

st.header("Header for the App")

st.subheader("Sub-Header of the app")

st.text("Hello, welcome to our real estate price prediction website--")

st.success("This is a Success")
st.warning("This is a Warning")
st.info("This is an Information")
st.error("This is an Error")

if st.checkbox("Select/Unselect"):
    st.text("You selected the checkbox")
else:
    st.text("You didn't selected the checkbox")


#Radio Button
state = st.radio("Choose one color-" , ("Red","Green","Blue","Yellow","Purple"))

if state == 'Green':
    st.success("That is my favorite color as well")

#SelectBox
occupation = st.selectbox("What do you do?" , ["Student","Vlogger","Engineer"])
st.text(f"Selected option is {occupation}")

st.text_input("Enter your name-")

st.text_area("Enter your feedback....")

if st.button("Submit"):
    st.text("Form Submitted")