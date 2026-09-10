/* ===========================================================
   Ciudad de Paseo — interactivity
   =========================================================== */
(function () {
  'use strict';

  var panels    = document.querySelectorAll('.tab-panel');
  var navLinks  = document.querySelectorAll('[data-tab]');
  var navMenu   = document.getElementById('navLinks');
  var navToggle = document.getElementById('navToggle');

  /* ---- Tab switching ---- */
  function showTab(id) {
    var found = false;
    panels.forEach(function (p) {
      var on = p.id === id;
      p.classList.toggle('active', on);
      if (on) found = true;
    });
    if (!found) return;

    document.querySelectorAll('.nav-links .nav-link').forEach(function (l) {
      l.classList.toggle('active', l.getAttribute('data-tab') === id);
    });

    // update hash without a jump, then scroll to top of content
    history.replaceState(null, '', '#' + id);
    window.scrollTo({ top: 0, behavior: 'smooth' });

    // close mobile menu
    navMenu.classList.remove('open');
    if (navToggle) navToggle.setAttribute('aria-expanded', 'false');
  }

  navLinks.forEach(function (link) {
    link.addEventListener('click', function (e) {
      var tab = link.getAttribute('data-tab');
      if (tab) { e.preventDefault(); showTab(tab); }
    });
  });

  /* ---- Mobile menu toggle ---- */
  if (navToggle) {
    navToggle.addEventListener('click', function () {
      var open = navMenu.classList.toggle('open');
      navToggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  /* ---- Rules accordion ---- */
  document.querySelectorAll('.rule-head').forEach(function (head) {
    head.addEventListener('click', function () {
      var cat = head.parentElement;
      cat.classList.toggle('open');
    });
  });

  // open the first rule category by default
  var firstRule = document.querySelector('.rule-cat');
  if (firstRule) firstRule.classList.add('open');

  /* ---- Deep-link support (open correct tab from #hash) ---- */
  var initial = (location.hash || '#home').replace('#', '');
  if (document.getElementById(initial)) showTab(initial);

  /* ---- Discord button placeholders ---- */
  ['discordBtn', 'donateDiscordBtn'].forEach(function (id) {
    var btn = document.getElementById(id);
    if (!btn) return;
    btn.addEventListener('click', function (e) {
      if (btn.getAttribute('href') === '#') {
        e.preventDefault();
        alert('Add your Discord invite link here in index.html (the #' + id + ' link).');
      }
    });
  });
})();
