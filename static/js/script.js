// script.js

const chatContainer = document.getElementById('chat-container');
const messagesDiv = document.getElementById('messages');
const userInput = document.getElementById('user-input');
const submitBtn = document.getElementById('submit-btn');

submitBtn.addEventListener('click', async () => {
  const message = userInput.value;
  userInput.value = '';
  const response = await fetch('/chat', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ message }),
  });
  const data = await response.json();
  displayMessage('User', message);
  displayMessage('Chatbot', data.response);
});

function displayMessage(sender, message) {
  const messageDiv = document.createElement('div');
  messageDiv.className = 'message';
  messageDiv.innerHTML = `<strong>${sender}:</strong> ${message}`;
  messagesDiv.appendChild(messageDiv);
}

chatContainer.style.display = 'block';
