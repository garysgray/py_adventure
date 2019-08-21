
var chatText = document.getElementById('chat-text');
var chatInput = document.getElementById('chat-input');
var chatForm = document.getElementById('chat-form');

chatForm.onsubmit = function(e)
{
    e.preventDefault();
    chatText.innerHTML += '<div>' + chatInput.value + '</div>';
    chatInput.value = ""; 
}
