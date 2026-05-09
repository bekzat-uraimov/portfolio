// Dark mode toggle (persists across reloads)
const toggle = document.getElementById('mode-toggle');

if (localStorage.getItem('mode') === 'dark') {
  document.body.classList.add('dark');
}

toggle?.addEventListener('click', () => {
  document.body.classList.toggle('dark');
  localStorage.setItem('mode', document.body.classList.contains('dark') ? 'dark' : 'light');
});

// Typed hero subtitle
const phrases = [
  'Building',
  'Shipping',
  'Learning',
  'Open to opportunities',
];

const typed = document.getElementById('typed');

async function runTyper() {
  if (!typed) return;
  let i = 0;
  while (true) {
    const phrase = phrases[i % phrases.length];
    for (let n = 0; n <= phrase.length; n++) {
      typed.textContent = phrase.slice(0, n);
      await sleep(55);
    }
    await sleep(1600);
    for (let n = phrase.length; n >= 0; n--) {
      typed.textContent = phrase.slice(0, n);
      await sleep(28);
    }
    await sleep(280);
    i++;
  }
}

const sleep = ms => new Promise(r => setTimeout(r, ms));
runTyper();

// Copy email
const copyBtn = document.getElementById('copy-email');
copyBtn?.addEventListener('click', async () => {
  const email = copyBtn.dataset.email;
  try {
    await navigator.clipboard.writeText(email);
    copyBtn.querySelector('.copy-status').textContent = 'copied';
    copyBtn.classList.add('copied');
    setTimeout(() => copyBtn.classList.remove('copied'), 1500);
  } catch {
    window.location.href = `mailto:${email}`;
  }
});

// Live GitHub projects
async function loadProjects() {
  const grid = document.getElementById('projects-grid');
  if (!grid) return;

  try {
    const res = await fetch('/api/repos');
    if (!res.ok) throw new Error('failed to fetch');
    const repos = await res.json();

    if (!Array.isArray(repos) || repos.length === 0) {
      grid.innerHTML = '<div class="project-card skeleton">No public projects yet.</div>';
      return;
    }

    grid.innerHTML = repos.map(renderCard).join('');
  } catch (err) {
    grid.innerHTML = '<div class="project-card skeleton">Could not load projects right now.</div>';
  }
}

function renderCard(repo) {
  const topics = (repo.topics || []).slice(0, 4)
    .map(t => `<span class="badge">${escape(t)}</span>`).join('');
  const lang = repo.language ? `<span class="badge">${escape(repo.language)}</span>` : '';
  const fork = repo.forked ? '<span class="fork-tag">fork</span>' : '';
  const stars = repo.stars > 0 ? `★ ${repo.stars}` : '';

  return `
    <article class="project-card">
      <div class="project-name">${escape(repo.name)} ${fork}</div>
      <p class="project-desc">${escape(repo.description) || 'No description.'}</p>
      <div class="project-meta">${lang}${topics}</div>
      <div class="project-foot">
        <span>${stars}</span>
        <a href="${repo.url}" target="_blank" rel="noopener">View on GitHub →</a>
      </div>
    </article>
  `;
}

function escape(s) {
  return String(s ?? '').replace(/[&<>"']/g, c => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
  }[c]));
}

loadProjects();
