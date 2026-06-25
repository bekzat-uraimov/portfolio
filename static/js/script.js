// Theme: default to dark, only switch to light if user explicitly set it
const toggle = document.getElementById('mode-toggle');

if (localStorage.getItem('mode') === 'light') {
  document.body.classList.remove('dark');
}

toggle?.addEventListener('click', () => {
  document.body.classList.toggle('dark');
  localStorage.setItem('mode', document.body.classList.contains('dark') ? 'dark' : 'light');
});

// Scroll reveal
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      // rAF ensures initial opacity:0 is painted before transition starts
      requestAnimationFrame(() => entry.target.classList.add('revealed'));
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.08 });

document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));
});

// Active nav link — highlight the section currently in view
const navLinks = document.querySelectorAll('.nav-link');
const navTargets = ['about', 'projects', 'contact'];

const navObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      navLinks.forEach(link => {
        link.classList.toggle('active', link.getAttribute('href') === `#${entry.target.id}`);
      });
    }
  });
}, { rootMargin: '-45% 0px -45% 0px' });

document.addEventListener('DOMContentLoaded', () => {
  navTargets.forEach(id => {
    const el = document.getElementById(id);
    if (el) navObserver.observe(el);
  });
});

// Typewriter
const phrases = [
  'CS undergrad, Seattle area.',
  'I build things that work.',
  'open to internships and full-time roles.',
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

    grid.innerHTML = repos.map((repo, i) => renderCard(repo, i + 1)).join('');
    // Observe dynamically-added cards with staggered delay
    grid.querySelectorAll('.reveal').forEach((el, i) => {
      el.style.transitionDelay = `${i * 0.07}s`;
      revealObserver.observe(el);
    });
  } catch (err) {
    grid.innerHTML = '<div class="project-card skeleton">Could not load projects right now.</div>';
  }
}

function renderCard(repo, num) {
  const numStr = String(num).padStart(2, '0');
  const lang = repo.language ? escape(repo.language) : null;
  const fork = repo.forked ? '<span class="fork-tag">fork</span>' : '';
  const langLink = `<a href="${repo.url}" target="_blank" rel="noopener" class="project-lang">${lang ? lang + ' ↗' : 'GitHub ↗'}</a>`;

  return `
    <article class="project-card reveal">
      <div class="project-row">
        <span class="project-num">${numStr}</span>
        <span class="project-name">${escape(repo.name)} ${fork}</span>
        ${langLink}
      </div>
      ${repo.description ? `<p class="project-desc">${escape(repo.description)}</p>` : ''}
    </article>
  `;
}

function escape(s) {
  return String(s ?? '').replace(/[&<>"']/g, c => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
  }[c]));
}

loadProjects();
