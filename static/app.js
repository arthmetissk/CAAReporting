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

  function el(tag, className, text) {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (text != null) node.textContent = text;
    return node;
  }

  function renderAnswerCard(target, data) {
    const card = el('article', 'chat-answer-card');
    const formatted = data.formatted || {};
    const headline = formatted.headline || data.answer || 'No answer available.';
    const bullets = formatted.bullets || [];
    const nextStep = formatted.next_step;
    const context = formatted.context || '';

    card.appendChild(el('div', 'chat-answer-kicker', 'Performance summary'));
    card.appendChild(el('h3', 'chat-answer-headline', headline));
    if (context) {
      card.appendChild(el('div', 'chat-answer-context', context));
    }

    if (bullets.length) {
      card.appendChild(el('div', 'chat-section-label', 'What the data shows'));
      const list = el('ul', 'chat-answer-list');
      bullets.forEach(function (point) {
        list.appendChild(el('li', null, point));
      });
      card.appendChild(list);
    }

    if (data.metrics && data.metrics.length) {
      card.appendChild(el('div', 'chat-section-label', 'Metrics by month'));
      const metricsWrap = el('div', 'chat-metrics');
      data.metrics.slice(0, 8).forEach(function (m) {
        const chip = el('div', 'chat-metric-chip');
        const monthPrefix = m.month ? (m.month + ' · ') : '';
        const campaignBit = m.campaign ? m.campaign.replace(/ — .*$/, '').split(' ').slice(0, 3).join(' ') : '';
        chip.appendChild(el('span', 'metric-label', monthPrefix + (campaignBit ? campaignBit + ' · ' : '') + m.label));
        chip.appendChild(el('span', 'metric-value', m.value));
        chip.appendChild(el('span', 'metric-delta', m.delta || ''));
        metricsWrap.appendChild(chip);
      });
      card.appendChild(metricsWrap);
    }

    if (data.campaigns && data.campaigns.length) {
      card.appendChild(el('div', 'chat-section-label', 'Campaigns referenced'));
      const refs = el('div', 'chat-ref-row');
      data.campaigns.forEach(function (c) {
        const label = (c.month ? c.month + ' · ' : '') + c.title;
        refs.appendChild(el('span', 'chat-ref-chip', label));
      });
      card.appendChild(refs);
    }

    if (nextStep) {
      card.appendChild(el('div', 'chat-section-label', 'Recommendation'));
      card.appendChild(el('p', 'chat-next-step', nextStep));
    }

    target.appendChild(card);
  }

  function askQuestion(query) {
    const q = (query || '').trim();
    if (!q || !drawerOutput) return;

    openDrawer();
    drawerOutput.appendChild(el('div', 'chat-output-user', q));
    drawerOutput.scrollTop = drawerOutput.scrollHeight;
    if (drawerQueryInput) drawerQueryInput.value = '';

    const thinking = el('div', 'chat-drawer-message chat-thinking', 'Preparing a concise metric summary…');
    drawerOutput.appendChild(thinking);

    fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query: q })
    })
      .then(function (response) { return response.json(); })
      .then(function (data) {
        thinking.remove();
        renderAnswerCard(drawerOutput, data);
        drawerOutput.scrollTop = drawerOutput.scrollHeight;
      })
      .catch(function () {
        thinking.remove();
        drawerOutput.appendChild(el(
          'div',
          'chat-drawer-message',
          'Chat is unavailable right now. Use By month / Families / Stores tabs for metrics.'
        ));
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

  const filter = document.getElementById('brandFilter');
  if (filter) {
    filter.querySelectorAll('.filter-chip').forEach(function (chip) {
      chip.addEventListener('click', function () {
        filter.querySelectorAll('.filter-chip').forEach(function (c) { c.classList.remove('active'); });
        chip.classList.add('active');
        const brand = chip.getAttribute('data-brand');
        document.querySelectorAll('.august-card').forEach(function (card) {
          card.hidden = !(brand === 'all' || card.getAttribute('data-brand') === brand);
        });
      });
    });
  }

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
