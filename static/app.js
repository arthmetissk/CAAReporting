document.addEventListener('DOMContentLoaded', function () {
  const goButton = document.getElementById('chatSubmit');
  const queryInput = document.getElementById('chatQuery');
  const output = document.getElementById('chatOutput');

  function addOutput(text, isUser) {
    if (!output) return;
    const row = document.createElement('div');
    row.className = isUser ? 'chat-output-user' : 'chat-output-message';
    row.textContent = text;
    output.appendChild(row);
  }

  if (goButton && queryInput && output) {
    goButton.addEventListener('click', function () {
      const query = queryInput.value.trim();
      if (!query) return;
      addOutput(query, true);
      output.scrollTop = output.scrollHeight;

      fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query: query })
      })
      .then(response => response.json())
      .then(data => {
        output.innerHTML = '';
        addOutput(data.answer || 'No answer available.', false);
        if (data.recommendations && data.recommendations.length > 0) {
          const recText = 'Recommendations: ' + data.recommendations.map(r => r.title).join(' • ');
          addOutput(recText, false);
        }
      })
      .catch(err => {
        output.innerHTML = '';
        addOutput('The campaign intelligence assistant is unavailable. Please try again.', false);
      });
    });
  }

  const askButtons = Array.from(document.getElementsByClassName('small-button'));
  askButtons.forEach(btn => {
    btn.addEventListener('click', function () {
      if (!queryInput) return;
      const text = btn.getAttribute('data-query') || 'What is the strategic recommendation?';
      queryInput.value = text;
      if (goButton) goButton.click();
    });
  });
});
