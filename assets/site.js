(() => {
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.site-nav');
  if (toggle && nav) {
    const close = () => { nav.classList.remove('is-open'); toggle.setAttribute('aria-expanded', 'false'); };
    toggle.addEventListener('click', () => {
      const open = !nav.classList.contains('is-open');
      nav.classList.toggle('is-open', open);
      toggle.setAttribute('aria-expanded', String(open));
    });
    nav.addEventListener('click', (event) => { if (event.target.closest('a')) close(); });
    addEventListener('keydown', (event) => { if (event.key === 'Escape') { close(); toggle.focus(); } });
  }

  const reveals = [...document.querySelectorAll('[data-reveal]')];
  if (!('IntersectionObserver' in window) || matchMedia('(prefers-reduced-motion: reduce)').matches) {
    reveals.forEach((el) => el.classList.add('is-in'));
  } else {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-in');
          observer.unobserve(entry.target);
        }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.04 });
    reveals.forEach((el) => observer.observe(el));
  }

  const choices = [...document.querySelectorAll('[data-choice]')];
  const output = document.querySelector('#choice-output');
  const messages = {
    'Research preparation': 'Review focus: open every cited source; confirm currency, support, and application.',
    'Draft from supplied records': 'Review focus: compare every fact and requested position with the supplied record.',
    'Intake organization': 'Review focus: correct parties, dates, documents, and open questions; complete conflict and engagement checks outside Merit.',
    'Filing-document preparation': 'Review focus: check substance and form, then sign and submit through the court process manually.',
    'Proposed deadline calculation': 'Review focus: independently recalculate from the governing rule, trigger, court order, service method, holidays, and exceptions.'
  };
  choices.forEach((button) => button.addEventListener('click', () => {
    choices.forEach((item) => item.setAttribute('aria-pressed', String(item === button)));
    if (output) output.textContent = messages[button.dataset.choice];
  }));
})();
