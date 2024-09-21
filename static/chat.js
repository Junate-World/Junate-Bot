document.getElementById('chat-form').addEventListener('submit', function(event) {
  event.preventDefault();
  var userInput = document.getElementById('user_input').value;
  var chatBox = document.getElementById('chat-box');

  chatBox.innerHTML += '<div class="Me2"><div class="Me"><strong></strong> ' + userInput + '</div></div><br>';

  fetch('/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ user_input: userInput })
  })
  .then(response => response.json())
  .then(data => {
      chatBox.innerHTML += '<div class="bot"><div class="message"> ' + data.response + '</div></div><br>';
      document.getElementById('user_input').value = '';
      chatBox.scrollTop = chatBox.scrollHeight; // Scroll to bottom

      if (data.response.includes("I don't know the answer")) {
          var newAnswer = prompt('Type the new answer or "skip" to skip:');
          if (newAnswer.toLowerCase() !== 'skip') {
              fetch('/update_knowledge', {
                  method: 'POST',
                  headers: { 'Content-Type': 'application/json' },
                  body: JSON.stringify({ user_input: userInput, new_answer: newAnswer })
              })
              .then(response => response.json())
              .then(data => {
                  chatBox.innerHTML += '<div class="bot"><div class="message"> ' + data.response + '</div></div><br>';
                  chatBox.scrollTop = chatBox.scrollHeight; // Scroll to bottom
              });
          }
      }
  });
});