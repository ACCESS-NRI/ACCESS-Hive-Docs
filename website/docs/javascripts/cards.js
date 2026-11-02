/* Turns the flat Markdown body into the live site's layout: each H2 section becomes a white card,
   and a small decorative image next to it is moved to a side column (alternating left/right). */
(function () {
  /* preview builds use *.html URLs; make directory-style internal links (raw HTML in index.md) work there too */
  function fixLinks() {
    if (!/\.html$/.test(location.pathname)) return;
    document.querySelectorAll('a[href]').forEach(function (a) {
      var h = a.getAttribute("href");
      if (/^(https?:|mailto:|#|\/\/)/.test(h) || !/\/$/.test(h)) return;
      a.setAttribute("href", h.replace(/\/$/, ".html"));
    });
  }
  function init() {
    fixLinks();
    var root = document.querySelector(".md-content__inner.md-typeset");
    if (!root || root.dataset.cards || document.querySelector(".masthead") || document.querySelector('meta[name="anri-cards"]')) return;
    root.dataset.cards = "1";
    var kids = Array.prototype.slice.call(root.children).filter(function (e) { return !e.matches("h1,.md-source-file,.headerlink,.md-content__button"); });
    var first = root.querySelector(":scope > h1");
    function imgOnly(el) {
      if (!el || el.tagName !== "P") return null;
      var imgs = el.querySelectorAll("img");
      if (imgs.length !== 1 || el.textContent.trim() !== "") return null;
      var m = (imgs[0].getAttribute("src") || "").match(/-(\d+)x(\d+)\.\w+$/);
      if (m) { var w = parseInt(m[1], 10), h = parseInt(m[2], 10); if (w > 400 || w / h < 0.8 || w / h > 1.25) return null; } else if (imgs[0].complete && imgs[0].naturalWidth && (imgs[0].naturalWidth / imgs[0].naturalHeight < 0.8 || imgs[0].naturalWidth / imgs[0].naturalHeight > 1.25)) return null; /* only small square icons are decoration; photos stay in the body */
      return el;
    }
    // runs of [icon image][## linked heading] become a 3-column icon grid
    (function () {
      var els = Array.prototype.slice.call(root.children), i = 0;
      while (i < els.length - 1) {
        var run = [];
        while (i + 1 < els.length && imgOnly(els[i]) && els[i + 1].tagName === "H2" && els[i + 1].querySelector("a")) { run.push([els[i], els[i + 1]]); i += 2; }
        if (run.length >= 3) {
          var g = document.createElement("div"); g.className = "anri-icons";
          run[0][0].parentNode.insertBefore(g, run[0][0]);
          run.forEach(function (r) { var it = document.createElement("div"); it.className = "anri-icons__item"; it.appendChild(r[0]); it.appendChild(r[1]); g.appendChild(it); });
        } else if (!run.length) i++;
      }
      kids = Array.prototype.slice.call(root.children).filter(function (e) { return !e.matches("h1,.md-source-file,.headerlink,.md-content__button"); });
    })();
    var sections = [], cur = null;
    kids.forEach(function (el) {
      if (el.classList.contains("anri-icons")) { if (!cur) { cur = { els: [] }; sections.push(cur); } cur.els.push(el); return; }
      if (el.tagName === "H2" || !cur) { cur = { els: [] }; sections.push(cur); }
      cur.els.push(el);
    });
    // an image-only paragraph at the end of a section belongs to the next section's heading
    for (var i = 0; i < sections.length - 1; i++) {
      var last = sections[i].els[sections[i].els.length - 1];
      if (sections[i].els.length > 1 && imgOnly(last) && sections[i + 1].els[0].tagName === "H2") {
        sections[i].els.pop(); sections[i + 1].els.splice(1, 0, last);
      }
    }
    var n = 0;
    sections.forEach(function (s) {
      if (!s.els.length || (s.els.length === 1 && s.els[0].tagName === "HR")) return;
      var hasHeading = s.els[0].tagName === "H2";
      if (!hasHeading && s.els.every(function (e) { return e.tagName === "P" && e.textContent.trim().length < 3; })) return;
      var media = null;
      for (var j = 0; j < s.els.length; j++) { if (imgOnly(s.els[j]) && j <= 2) { media = s.els[j]; break; } }
      var card = document.createElement("section");
      card.className = "anri-card" + (media ? " anri-card--media" + (n % 2 ? " anri-card--flip" : "") : "");
      var body = document.createElement("div"); body.className = "anri-card__body";
      s.els[0].parentNode.insertBefore(card, s.els[0]);
      if (media) { var m = document.createElement("div"); m.className = "anri-card__media"; m.appendChild(media); card.appendChild(m); n++; }
      card.appendChild(body);
      s.els.forEach(function (e) { if (e !== media && e.tagName !== "HR") body.appendChild(e); else if (e.tagName === "HR") e.remove(); });
    });
  }
  if (document.readyState !== "loading") init(); else document.addEventListener("DOMContentLoaded", init);
  if (window.document$) window.document$.subscribe(function () { var r = document.querySelector(".md-content__inner.md-typeset"); if (r) delete r.dataset.cards; init(); });
})();
