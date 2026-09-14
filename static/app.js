document.addEventListener('DOMContentLoaded', function () {
  const drawer = document.getElementById('chatDrawer');
  const drawerClose = document.getElementById('chatClose');
  const launcher = document.getElementById('chatLauncher');
  const drawerGoButton = document.getElementById('chatDrawerSubmit');
  const drawerQueryInput = document.getElementById('chatDrawerQuery');
  const drawerOutput = document.getElementById('chatDrawerOutput');

  function openDrawer() {
    if (!drawer) return;
    drawer.classList.add('open');
    if (drawerQueryInput) drawerQueryInput.focus();
  }

  function addMessage(target, text, className) {
    if (!target) return;
    const row = document.createElement('div');
    row.className = className;
    row.textContent = text;
    target.appendChild(row);
  }

  function addMetrics(target, metrics) {
    if (!target || !metrics || !metrics.length) return;
    const wrap = document.createElement('div');
    wrap.className = 'chat-metrics';
    metrics.slice(0, 6).forEach(function (m) {
      const chip = document.createElement('div');
      chip.className = 'chat-metric-chip';
      chip.innerHTML =
        '<span class="metric-label">' + (m.campaign ? m.campaign.split(' ')[0] + ' · ' : '') + m.label + '</span>' +
        '<span class="metric-value">' + m.value + '</span>' +
        '<span class="metric-delta">' + (m.delta || '') + '</span>';
      wrap.appendChild(chip);
    });
    target.appendChild(wrap);
  }

  function addRecs(target, recs) {
    if (!target || !recs || !recs.length) return;
    addMessage(
      target,
      'Actions: ' + recs.map(function (r) { return r.title || r; }).join(' · '),
      'chat-drawer-message chat-recs'
    );
  }

  function askQuestion(query) {
    const q = (query || '').trim();
    if (!q || !drawerOutput) return;

    openDrawer();
    addMessage(drawerOutput, q, 'chat-output-user');
    drawerOutput.scrollTop = drawerOutput.scrollHeight;
    if (drawerQueryInput) drawerQueryInput.value = '';

    const thinking = document.createElement('div');
    thinking.className = 'chat-drawer-message';
    thinking.textContent = 'Pulling campaign metrics…';
    drawerOutput.appendChild(thinking);

    fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query: q })
    })
      .then(function (response) { return response.json(); })
      .then(function (data) {
        thinking.remove();
        addMessage(drawerOutput, data.answer || 'No answer available.', 'chat-drawer-message');
        addMetrics(drawerOutput, data.metrics);
        addRecs(drawerOutput, data.recommendations);
        drawerOutput.scrollTop = drawerOutput.scrollHeight;
      })
      .catch(function () {
        thinking.remove();
        addMessage(
          drawerOutput,
          'Chat is unavailable right now. Use By month / Families / Stores tabs for metrics.',
          'chat-drawer-message'
        );
      });
  }

  if (launcher && drawer) {
    launcher.addEventListener('click', function () {
      drawer.classList.toggle('open');
      if (drawer.classList.contains('open') && drawerQueryInput) drawerQueryInput.focus();
    });
  }

  if (drawerClose && drawer) {
    drawerClose.addEventListener('click', function () {
      drawer.classList.remove('open');
    });
  }

  if (drawerGoButton && drawerQueryInput) {
    drawerGoButton.addEventListener('click', function () {
      askQuestion(drawerQueryInput.value);
    });
    drawerQueryInput.addEventListener('keydown', function (event) {
      if (event.key === 'Enter') askQuestion(drawerQueryInput.value);
    });
  }

  document.querySelectorAll('[data-query]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      askQuestion(btn.getAttribute('data-query') || '');
    });
  });

  // Browse tabs
  const tabs = document.getElementById('browseTabs');
  if (tabs) {
    tabs.querySelectorAll('.browse-tab').forEach(function (tab) {
      tab.addEventListener('click', function () {
        tabs.querySelectorAll('.browse-tab').forEach(function (t) { t.classList.remove('active'); });
        tab.classList.add('active');
        const panel = tab.getAttribute('data-panel');
        document.querySelectorAll('.browse-panel').forEach(function (p) {
          const match = p.id === 'panel-' + panel;
          p.hidden = !match;
          p.classList.toggle('active', match);
        });
      });
    });
  }

  // August brand filter
  const filter = document.getElementById('brandFilter');
  if (filter) {
    filter.querySelectorAll('.filter-chip').forEach(function (chip) {
      chip.addEventListener('click', function () {
        filter.querySelectorAll('.filter-chip').forEach(function (c) { c.classList.remove('active'); });
        chip.classList.add('active');
        const brand = chip.getAttribute('data-brand');
        document.querySelectorAll('.august-card').forEach(function (card) {
          const show = brand === 'all' || card.getAttribute('data-brand') === brand;
          card.hidden = !show;
        });
      });
    });
  }

  // All-campaigns month filter
  const campaignFilters = document.getElementById('campaignFilters');
  if (campaignFilters) {
    campaignFilters.querySelectorAll('.filter-chip').forEach(function (chip) {
      chip.addEventListener('click', function () {
        campaignFilters.querySelectorAll('.filter-chip').forEach(function (c) { c.classList.remove('active'); });
        chip.classList.add('active');
        const month = chip.getAttribute('data-month');
        document.querySelectorAll('#allCampaignGrid .scorecard').forEach(function (card) {
          card.hidden = !(month === 'all' || card.getAttribute('data-month') === month);
        });
      });
    });
  }

  // Store filter
  const storeFilter = document.getElementById('storeFilter');
  if (storeFilter) {
    storeFilter.querySelectorAll('.filter-chip').forEach(function (chip) {
      chip.addEventListener('click', function () {
        storeFilter.querySelectorAll('.filter-chip').forEach(function (c) { c.classList.remove('active'); });
        chip.classList.add('active');
        const store = chip.getAttribute('data-store');
        document.querySelectorAll('[data-store-card]').forEach(function (card) {
          card.hidden = !(store === 'all' || card.getAttribute('data-store-card') === store);
        });
      });
    });
  }
});
