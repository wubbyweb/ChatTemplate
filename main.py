import streamlit as st

def main():
    st.title('Chat Interface')

    # Create a text input for the user's message
    user_message = st.text_input("Type your message here...")

    # Create a button for the user to submit their message
    if st.button('Send'):
        # Display the user's message on the screen
        st.write(f"You: {user_message}")

        # Simulate a response from the chatbot
        # For demonstration purposes, we'll just echo the user's message back to them
        st.write(f"ChatGPT: {user_message}")

if __name__ == "__main__":
    main()
