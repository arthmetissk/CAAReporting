document.addEventListener('DOMContentLoaded', function () {
  const goButton = document.getElementById('chatSubmit');
  const queryInput = document.getElementById('chatQuery');
  const output = document.getElementById('chatOutput');
  const drawer = document.getElementById('chatDrawer');
  const drawerClose = document.getElementById('chatClose');
  const launcher = document.getElementById('chatLauncher');
  const drawerGoButton = document.getElementById('chatDrawerSubmit');
  const drawerQueryInput = document.getElementById('chatDrawerQuery');
  const drawerOutput = document.getElementById('chatDrawerOutput');

  function addOutput(target, text, isUser) {
    if (!target) return;
    const row = document.createElement('div');
    row.className = isUser ? 'chat-output-user' : 'chat-output-message';
    row.textContent = text;
    target.appendChild(row);
  }

  function askQuestion(input, outputTarget, submitTarget) {
    const query = (input.value || '').trim();
    if (!query) return;
    addOutput(outputTarget, query, true);
    if (outputTarget.scrollTop !== undefined) {
      outputTarget.scrollTop = outputTarget.scrollHeight;
    }

    fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query: query })
    })
    .then(response => response.json())
    .then(data => {
      outputTarget.innerHTML = '';
      addOutput(outputTarget, data.answer || 'No answer available.', false);
      if (data.recommendations && data.recommendations.length > 0) {
        const recText = 'Recommendations: ' + data.recommendations.map(r => r.title).join(' • ');
        addOutput(outputTarget, recText, false);
      }
    })
    .catch(err => {
      outputTarget.innerHTML = '';
      addOutput(outputTarget, 'The campaign intelligence assistant is unavailable. Please try again.', false);
    });
  }

  if (launcher && drawer) {
    launcher.addEventListener('click', function () {
      drawer.classList.toggle('open');
      if (drawer.classList.contains('open')) {
        if (drawerQueryInput) drawerQueryInput.focus();
      }
    });
  }

  if (drawerClose && drawer) {
    drawerClose.addEventListener('click', function () {
      drawer.classList.remove('open');
    });
  }

  if (goButton && queryInput && output) {
    goButton.addEventListener('click', function () {
      askQuestion(queryInput, output, goButton);
    });
  }

  if (drawerGoButton && drawerQueryInput && drawerOutput) {
    drawerGoButton.addEventListener('click', function () {
      askQuestion(drawerQueryInput, drawerOutput, drawerGoButton);
    });

    drawerQueryInput.addEventListener('keydown', function (event) {
      if (event.key === 'Enter') {
        askQuestion(drawerQueryInput, drawerOutput, drawerGoButton);
      }
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
