/* One dated supplement per morning edition; the main lesson remains independent. */
(() => {
  const host = document.getElementById('weekly-highlight');
  const data = document.getElementById('weekly-data');
  if (!host || !data) return;
  const editions = JSON.parse(data.textContent);
  const today = new Intl.DateTimeFormat('en-CA', {timeZone:'Europe/Berlin',year:'numeric',month:'2-digit',day:'2-digit'}).format(new Date());
  const latestEdition = editions.filter(e => e.date <= today).sort((a,b) => b.date.localeCompare(a.date))[0];
  const add = (parent, tag, text, className) => {
    const node = document.createElement(tag);
    if (text) node.textContent = text;
    if (className) node.className = className;
    parent.append(node);
    return node;
  };
  const dayName = new Intl.DateTimeFormat('de-DE',{weekday:'long',timeZone:'Europe/Berlin'}).format(new Date());
  document.querySelectorAll('#weekly-plan tbody tr').forEach(row => {
    if (row.dataset.day === dayName) {
      row.classList.add('current-day');
      row.setAttribute('aria-current','date');
    }
  });
  if (!latestEdition) { host.hidden = true; return; }
  const e = latestEdition;
  const dateLabel = new Intl.DateTimeFormat('de-DE',{weekday:'long',day:'2-digit',month:'2-digit',year:'numeric',timeZone:'Europe/Berlin'}).format(new Date(e.date+'T12:00:00Z'));
  add(host,'p',dateLabel+' · '+e.kind,'eyebrow');
  add(host,'h2',e.title);
  if (e.topicId) {
    const topic = topics.find(t => t.id === e.topicId);
    if (topic) add(host,'p','Passend zu Thema '+topic.id+' · '+topic.title,'muted');
  }
  if (e.intro) add(host,'p',e.intro);
  const body = add(host,'details');
  add(body,'summary',e.summary || 'Weiterlesen');
  for (const text of e.paragraphs || []) add(body,'p',text);
  if (e.image) {
    const img = add(body,'img');
    img.src = e.image;
    img.alt = e.imageAlt || e.title;
    img.loading = 'lazy';
  }
  if (e.sources?.length) {
    const refs = add(body,'p',null,'weekly-sources');
    add(refs,'strong','Quelle: ');
    for (const [i,source] of e.sources.entries()) {
      const url = new URL(source.url,location.href);
      if (!['http:','https:'].includes(url.protocol)) continue;
      if (i) refs.append(document.createTextNode(' · '));
      const link = add(refs,'a',source.label);
      link.href = url.href;
      link.target = '_blank';
      link.rel = 'noopener noreferrer';
    }
  }
  if (e.topicId && published.includes(e.topicId)) {
    const button = add(body,'button','Zur passenden Fortbildung');
    button.type = 'button';
    button.addEventListener('click',() => show('lesson',e.topicId));
  }
})();
