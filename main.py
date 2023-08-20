import streamlit as st
import google.generativeai as palm

def main():
    st.title("Chat Garden")

st.write(f"""
* {
    box-sizing: border-box;
}

body {
    margin: 0;
    padding: 0;
    font-family: Arial, sans-serif;
    background-color: #222;
    color: #fff;
}

.container {
    display: flex;
    height: 100vh;
}

.sidebar {
    width: 20%;
    background-color: #333;
    padding: 20px;
}

.sidebar .header {
    text-align: center;
    margin-bottom: 20px;
}

.sidebar .header h1 {
    font-size: 24px;
}

.chatbot-list {
    display: flex;
    flex-direction: column;
}

.chatbot {
    display: flex;
    align-items: center;
    padding: 10px;
    border-radius: 5px;
    cursor: pointer;
    margin-bottom: 10px;
}

.chatbot img {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    margin-right: 10px;
}

.chatbot.active {
    background-color: #555;
}

.chat-interface {
    flex: 1;
    padding: 20px;
    display: flex;
    flex-direction: column;
}

.chat-interface .header {
    display: flex;
    align-items: center;
    margin-bottom: 20px;
}

.chat-interface .header img {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    margin-right: 10px;
}

.chat-interface .messages {
    flex: 1;
    overflow-y: scroll;
    display: flex;
    flex-direction: column;
}

.chat-interface .message {
    display: flex;
    align-items: flex-start;
    margin-bottom: 10px;
}

.chat-interface .message.right {
    justify-content: flex-end;
}

.chat-interface .message.left {
    justify-content: flex-start;
}

.chat-interface .message .message-content {
    background-color: #444;
    padding: 10px;
    border-radius: 5px;
    word-wrap: break-word;
}

.chat-interface .message .text {
    color: #fff;
    line-height: 1.4;
    margin: 0;
    word-break: break-word; /* Add this line */
    overflow-wrap: break-word; /* Add this line */
}

.input-container {
    display: flex;
    margin-top: 20px;
}

.input-container textarea {
    flex: 1;
    padding: 10px;
    border-radius: 5px;
    resize: none;
}

.input-container button {
    background-color: #4caf50;
    color: #fff;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
    margin-left: 10px;
}

.input-container button:hover {
    background-color: #45a049;
}

<div class="container">
  <div class="sidebar">
    <div class="header">
      <h1>Chat Garden</h1>
    </div>
    <div class="chatbot-list">
      <div class="chatbot active">
        <img src="avatar1.jpg" alt="Chatbot Avatar">
        <span class="name">Chatbot 1</span>
      </div>
      <div class="chatbot">
        <img src="avatar2.jpg" alt="Chatbot Avatar">
        <span class="name">Chatbot 2</span>
      </div>
      <!-- Add more chatbots here -->
    </div>
  </div>
  <div class="chat-interface">
    <div class="header">
      <img src="active-avatar.jpg" alt="Active Chatbot Avatar">
      <span class="name">Chatbot 1</span>
    </div>
    <div class="messages">
      <div class="message right">
        <div class="message-content">
          <span class="text">Hello, how can I assist you?</span>
        </div>
      </div>
      <div class="message left">
        <div class="message-content">
          <span class="text">This is a sample reply from the chatbot.</span>
        </div>
      </div>
      <!-- Add more messages here -->
    </div>
    <div class="input-container">
      <textarea id="input-text" placeholder="Type your message..."></textarea>
      <button id="send-btn">Send</button>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
