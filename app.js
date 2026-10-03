/* Die Mainzer Republik – The Mainz Republic — ein zweisprachiger Quellenapparat. Vanilla JS, Hash-Routen. */
"use strict";

const view = document.getElementById("view");
const D = { mods: null, plates: null, timeline: null, compare: null, texts: {} };

/* ------------------------------------------------------------ language */
let ui = "de";
try { ui = localStorage.getItem("mainz_ui") || ""; } catch (e) { /* storage blocked */ }
if (ui !== "de" && ui !== "en") ui = /^de\b/i.test(navigator.language || "") ? "de" : "en";
let langPref = null;
try { langPref = localStorage.getItem("mainz_lang"); } catch (e) { /* storage blocked */ }

const T = {
  de: {
    title: "Die Mainzer Republik", nav: { "": "Übersicht", texts: "Texte", compare: "Vergleich", timeline: "Zeitleiste", plates: "Tafeln", sources: "Quellen" },
    switchTo: "English", loading: "Wird geladen…", allTexts: "← Alle Texte", allCmp: "← Alle Vergleiche", citeAs: "zitiert als", cite: "Zitieren als",
    orig: "Original", both: "Original + Englisch", trans: "Englische Übersetzung", or: " oder ",
    srcNote: "Quelle und Editionsnotiz", source: "Quelle", planned: "geplant", notTaken: "nicht aufgenommen",
    shipped: "Abgedruckt", plannedH: "Geplant", missingH: "Geprüft und nicht aufgenommen",
    textsTag: "Texte", textsH: "Das Korpus", textsLede: "Jedes Modul ist vollständig lesbar, das deutsche Original neben einer englischen Übersetzung. Was geprüft und nicht aufgenommen wurde, steht unten mit Begründung.",
    cmpTag: "Vergleich", cmpH: "Klub, Kurfürst und Zeugen", tlTag: "Zeitleiste", platesTag: "Tafeln", platesH: "Bäume, Mauern, Köpfe",
    fail: "Der Apparat konnte nicht geladen werden: "
  },
  en: {
    title: "The Mainz Republic", nav: { "": "Overview", texts: "Texts", compare: "Compare", timeline: "Timeline", plates: "Plates", sources: "Sources" },
    switchTo: "Deutsch", loading: "Loading…", allTexts: "← All texts", allCmp: "← All comparisons", citeAs: "cited as", cite: "Cite as",
    orig: "German original", both: "German + English", trans: "English", or: " or ",
    srcNote: "Source and editorial note", source: "Source", planned: "planned", notTaken: "not included",
    shipped: "Printed here", plannedH: "Planned", missingH: "Examined and not included",
    textsTag: "Texts", textsH: "The corpus", textsLede: "Every module can be read in full, the German original beside an English translation. What was examined and not included is listed below, with the reason.",
    cmpTag: "Compare", cmpH: "Club, Elector and witnesses", tlTag: "Timeline", platesTag: "Plates", platesH: "Trees, walls, faces",
    fail: "The apparatus could not be loaded: "
  }
};
const S = k => T[ui][k];
const SIDES = {
  klub: { de: "Klub und Konvent", en: "Club and Convention" },
  franzosen: { de: "Die Franzosen", en: "The French" },
  reich: { de: "Kurfürst und Reich", en: "Elector and Empire" },
  zeugen: { de: "Zeugen", en: "Witnesses" },
  rezeption: { de: "Nachleben", en: "Afterlife" }
};
const LANGS = {
  de: { de: "Deutsch", en: "German" }, fr: { de: "Französisch", en: "French" },
  la: { de: "Latein", en: "Latin" }, en: { de: "Englisch", en: "English" }
};
/* a field in the reader's language: o.k_en in English if present, else o.k */
const L = (o, k) => (o && ui === "en" && o[k + "_en"] != null) ? o[k + "_en"] : (o ? o[k] : "");

const esc = s => String(s ?? "").replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const side = s => `<span class="side ${s}">${esc(SIDES[s] ? SIDES[s][ui] : s)}</span>`;
const lname = l => LANGS[l] ? LANGS[l][ui] : l;
const plateOf = id => (D.plates.plates || []).find(p => p.id === id);
const getJSON = url => fetch(url).then(r => { if (!r.ok) throw new Error(url); return r.json(); });

function setUI(lang) {
  ui = lang;
  try { localStorage.setItem("mainz_ui", ui); } catch (e) { /* storage blocked */ }
  applyUI();
  route();
}

function applyUI() {
  document.documentElement.lang = ui;
  document.title = S("title");
  document.querySelectorAll(".top nav a[data-k]").forEach(a => a.textContent = S("nav")[a.dataset.k]);
  const b = document.getElementById("uiBtn");
  b.textContent = S("switchTo");
  b.lang = ui === "de" ? "en" : "de";
}

async function boot() {
  applyUI();
  document.getElementById("uiBtn").onclick = () => setUI(ui === "de" ? "en" : "de");
  [D.mods, D.plates, D.timeline, D.compare] = await Promise.all(
    ["data/modules.json", "data/plates.json", "data/timeline.json", "data/compare.json"].map(getJSON));
  document.getElementById("navCompare").hidden = !(D.compare.pairs || []).length;
  document.getElementById("navPlates").hidden = !(D.plates.plates || []).length;
  window.addEventListener("hashchange", route);
  route();
}

async function text(id) {
  if (!D.texts[id]) D.texts[id] = await getJSON(`data/${id}.json`);
  return D.texts[id];
}

function route() {
  const parts = (location.hash.replace(/^#\/?/, "") || "").split("/").filter(Boolean);
  const [page, ...args] = parts;
  document.querySelectorAll(".top nav a").forEach(a => {
    const t = a.getAttribute("href").replace(/^#\/?/, "");
    a.classList.toggle("on", (t || "") === (page === "text" ? "texts" : page || ""));
  });
  view.innerHTML = "";
  window.scrollTo(0, 0);
  const pages = { "": overview, texts, text: reader, compare, timeline, plates, sources };
  (pages[page || ""] || overview)(args);
}

/* ------------------------------------------------------------ overview */
const OVERVIEW = {
  de: {
    tag: "1792–1793 · Mainz · Deutschhaus · Paris",
    h: "Was bleibt von einer Republik, die vier Monate dauerte?",
    lede: "Am 21. Oktober 1792 besetzten französische Revolutionstruppen unter General Custine Mainz, die Residenz des Kurfürsten und Erzbischofs. Zwei Tage später gründeten Mainzer Bürger eine Gesellschaft der Freunde der Freiheit und Gleichheit, den Jakobinerklub. Im Februar 1793 wurde gewählt, wer schwor, durfte wählen; wer den Eid auf Freiheit und Gleichheit verweigerte, musste gehen. Am 18. März 1793 erklärte der Rheinisch-Deutsche Nationalkonvent im Mainzer Deutschhaus das Land zwischen Landau und Bingen für frei, drei Tage später beschloss er, sich Frankreich anzuschließen. Im April schlossen preußische und Reichstruppen die Stadt ein; am 23. Juli 1793 kapitulierte die Besatzung.",
    body: "Dieser Apparat folgt den neun Monaten durch ihre Dokumente, in gemeinfreien Drucken, das deutsche Original neben einer englischen Übersetzung: die Proklamationen und Reden, die Beschlüsse des Konvents, die Tagebücher aus der belagerten Stadt, Goethes Bericht vom Lager der Belagerer, die Briefe Caroline Böhmers, und die Schriften, mit denen das 19. Jahrhundert die „Klubisten“ verurteilte oder verteidigte. Georg Forster, Weltreisender, Bibliothekar der Universität und Vizepräsident des Konvents, ist die Stimme, die durch alle Teile geht.",
    q: [
      ["Eine Republik auf deutschem Boden?", "Die erste, die sich auf deutschem Boden aus Wahlen bildete, sagen die einen; ein Satellit französischer Bajonette, sagen die anderen. Die Texte zeigen beides: Wahlen unter Besatzung, einen Eid als Bedingung, und Männer, die meinten, was sie schworen."],
      ["Wer wählte, und wer nicht?", "Gewählt wurde in Mainz und in den Dörfern der Umgebung. Viele Gemeinden verweigerten den Eid; Zünfte und Geistliche protestierten; wer nicht schwor, wurde ausgewiesen. Was die Wahlen bedeuteten, hängt an ihren Zahlen und an den Stimmen derer, die fernblieben."],
      ["Was sahen die Zeugen?", "Goethe stand im Sommer 1793 mit dem Herzog von Weimar im Lager der Belagerer und schrieb dreißig Jahre später auf, was er sah. Caroline Böhmer lebte im Winter in der Stadt, floh im März und wurde verhaftet. Die Tagebücher der Belagerten zählen Kugeln, Brände und Brotpreise."],
      ["Lässt sich das spielen?", "Das Begleitspiel Der Freiheitsbaum ist in Arbeit: Man führt den Konvent durch Wahl, Eid und Belagerung. Die Stadt fällt, wie sie gefallen ist; gewertet wird, was bleibt."]
    ],
    none: "Die ersten Module sind in Arbeit; die Seite „Texte“ nennt sie mit ihren Quellen.",
    have: "Was der Apparat enthält", qs: "Die Fragen"
  },
  en: {
    tag: "1792–1793 · Mainz · Deutschhaus · Paris",
    h: "What remains of a republic that lasted four months?",
    lede: "On 21 October 1792 French revolutionary troops under General Custine occupied Mainz, the seat of the Elector and Archbishop. Two days later citizens of Mainz founded a Society of the Friends of Liberty and Equality, the Jacobin club. In February 1793 elections were held: whoever took the oath could vote, and whoever refused the oath to liberty and equality had to leave. On 18 March 1793 the Rhenish-German National Convention, meeting in the Deutschhaus in Mainz, declared the land between Landau and Bingen free; three days later it voted to join France. In April Prussian and Imperial troops closed round the city; on 23 July 1793 the garrison capitulated.",
    body: "This apparatus follows those nine months through their documents, in public-domain prints, the German original beside an English translation: the proclamations and speeches, the decrees of the Convention, the diaries kept in the besieged city, Goethe's account from the besiegers' camp, the letters of Caroline Böhmer, and the books with which the nineteenth century condemned or defended the 'Clubists'. Georg Forster, circumnavigator, librarian of the university and vice-president of the Convention, is the voice that runs through every part.",
    q: [
      ["A republic on German soil?", "The first to form on German soil out of elections, say some; a satellite held up by French bayonets, say others. The texts show both: elections under occupation, an oath as the condition, and men who meant what they swore."],
      ["Who voted, and who did not?", "Votes were held in Mainz and in the villages around it. Many communities refused the oath; guilds and clergy protested; those who would not swear were expelled. What the elections meant depends on their numbers and on the voices of those who stayed away."],
      ["What did the witnesses see?", "Goethe stood in the besiegers' camp in the summer of 1793 with the Duke of Weimar and wrote down what he had seen thirty years later. Caroline Böhmer lived in the city that winter, fled in March and was arrested. The diaries of the besieged count cannonballs, fires and the price of bread."],
      ["Can it be played?", "The companion game The Liberty Tree is in the making: you lead the Convention through election, oath and siege. The city falls, as it fell; the score is what remains."]
    ],
    none: "The first modules are in preparation; the Texts page lists them with their sources.",
    have: "What the apparatus contains", qs: "The questions"
  }
};

function overview() {
  const O = OVERVIEW[ui];
  view.innerHTML = `
  <div class="hero one">
    <div>
      <span class="tag">${esc(O.tag)}</span>
      <h1>${esc(O.h)}</h1>
      <p class="lede">${esc(O.lede)}</p>
      <p class="readable">${esc(O.body)}</p>
    </div>
  </div>

  <h2>${esc(O.have)}</h2>
  ${D.mods.shipped.length ? `<div class="grid g2">${D.mods.shipped.map(card).join("")}</div>` : `<p class="fine">${esc(O.none)}</p>`}

  <h2>${esc(O.qs)}</h2>
  <div class="grid g2">${O.q.map(([h, p]) => `<div class="panel"><h3>${esc(h)}</h3><p>${esc(p)}</p></div>`).join("")}</div>`;
}

function card(m) {
  return `<a class="card" href="#/text/${m.id}">
    <div>${side(m.side)} <span class="fine">${esc(m.zk)}</span></div>
    <h3>${esc(L(m, "kurz"))}</h3><p class="fine">${esc(L(m, "warum"))}</p></a>`;
}

/* ------------------------------------------------------------ texts */
function texts() {
  const other = (list, label) => list.map(m => `
      <div class="card planned"><div>${side(m.side)} <span class="fine">${esc(label)}</span></div>
      <h3>${esc(L(m, "kurz"))}</h3><p class="fine">${esc(L(m, "warum"))}</p><p class="fine"><b>${esc(S("source"))}:</b> ${esc(m.quelle)}</p></div>`).join("");
  view.innerHTML = `
    <span class="tag">${esc(S("textsTag"))}</span><h1>${esc(S("textsH"))}</h1>
    <p class="lede">${esc(S("textsLede"))}</p>
    ${D.mods.shipped.length ? `<h2>${esc(S("shipped"))}</h2><div class="grid g2">${D.mods.shipped.map(card).join("")}</div>` : ""}
    ${(D.mods.planned || []).length ? `<h2>${esc(S("plannedH"))}</h2><div class="grid g2">${other(D.mods.planned, S("planned"))}</div>` : ""}
    ${(D.mods.missing || []).length ? `<h2 id="missing">${esc(S("missingH"))}</h2><div class="grid g2">${other(D.mods.missing, S("notTaken"))}</div>` : ""}`;
}

async function reader([id, secId, unitN]) {
  const m = D.mods.shipped.find(x => x.id === id);
  if (!m) { location.hash = "#/texts"; return; }
  view.innerHTML = `<p class="fine">${esc(S("loading"))}</p>`;
  const t = await text(m.datei);
  const sec = t.sections.find(s => s.id === secId) || t.sections[0];
  const bilingual = sec.units.some(u => u.orig);
  const pref = langPref || (ui === "de" ? "orig" : "both");
  const lang = bilingual ? pref : "en";
  const langs = [...new Set(sec.units.filter(u => u.orig).map(u => u.lang || t.orig_sprache))];
  const origName = langs.length === 1 && langs[0] !== "de" ? `Original (${lname(langs[0])})` : S("orig");
  const labels = { both: S("both"), orig: origName, en: S("trans") };
  view.innerHTML = `
    <p class="fine"><a href="#/texts">${esc(S("allTexts"))}</a></p>
    <span class="tag">${side(m.side)} ${esc(t.jahr)} · ${esc(S("citeAs"))} ${esc(sec.zk)} [n]</span>
    <h1>${esc(L(t, "titel"))}</h1>
    <p class="fine">${esc(L(t, "autor"))}</p>
    <nav class="toc">${t.sections.map(s => `<a href="#/text/${id}/${s.id}" class="${s.id === sec.id ? "on" : ""}">${esc(L(s, "titel"))}</a>`).join("")}</nav>
    <div class="panel readable"><h3>${esc(L(sec, "titel"))}</h3><p>${esc(L(sec, "blurb"))}</p></div>
    ${bilingual ? `<div class="langbar" id="langbar">
      ${["orig", "both", "en"].map(k => `<button data-l="${k}" class="${k === lang ? "on" : ""}">${esc(labels[k])}</button>`).join("")}</div>` : ""}
    <div id="units"></div>
    <div class="panel readable hinweis"><span class="tag">${esc(S("srcNote"))}</span>
      <p><b>${esc(S("source"))}.</b> ${esc(t.quelle)}</p><p>${esc(L(t, "hinweis"))}</p></div>`;
  const box = view.querySelector("#units");
  for (const u of sec.units) {
    const showO = u.orig && lang !== "en", showE = !u.orig || lang !== "orig";
    const cls = ["unit", String(u.n) === unitN ? "hl" : ""].join(" ");
    const ul = u.lang || t.orig_sprache;
    box.insertAdjacentHTML("beforeend", `
      <div class="${cls}" id="u${u.n}">
        <div class="num"><a href="#/text/${id}/${sec.id}/${u.n}" title="${esc(S("cite"))} ${esc(sec.zk)} [${u.n}]">[${u.n}]</a>
          ${u.pg ? `<span class="pg">${esc(t.pg_label || "")} ${esc(u.pg)}</span>` : ""}</div>
        <div>${u.titel ? `<h4>${esc(L(u, "titel"))}${u.lang && langs.length > 1 ? ` <span class="fine">(${esc(lname(u.lang))})</span>` : ""}</h4>` : ""}
          <div class="cols ${showO && showE ? "" : "one"}">
            ${showO ? `<div class="orig" lang="${esc(ul)}">${esc(u.orig)}</div>` : ""}
            ${showE ? `<div class="text" lang="en">${esc(u.en)}</div>` : ""}
          </div></div>
        ${L(u, "note") ? `<div class="note">${esc(L(u, "note"))}</div>` : ""}
      </div>`);
  }
  view.querySelectorAll("#langbar button").forEach(b => b.onclick = () => {
    langPref = b.dataset.l;
    try { localStorage.setItem("mainz_lang", langPref); } catch (e) { /* storage blocked */ }
    route();
  });
  if (unitN) { const el = document.getElementById("u" + unitN); if (el) el.scrollIntoView({ block: "center" }); }
}

/* ------------------------------------------------------------ compare */
async function compare([pid]) {
  const CMP = D.compare;
  const pair = (CMP.pairs || []).find(p => p.id === pid);
  if (!pair) {
    view.innerHTML = `
      <span class="tag">${esc(S("cmpTag"))}</span><h1>${esc(S("cmpH"))}</h1>
      <p class="lede">${esc(L(CMP, "lede"))}</p>
      <div class="grid g2">${(CMP.pairs || []).map(p => `<a class="card" href="#/compare/${p.id}">
        <div>${p.voices.map(v => side((D.mods.shipped.find(m => m.id === v.text) || {}).side)).join(" ")}</div>
        <h3>${esc(L(p, "titel"))}</h3><p class="fine">${esc(L(p, "frage"))}</p></a>`).join("")}</div>`;
    return;
  }
  view.innerHTML = `<p class="fine"><a href="#/compare">${esc(S("allCmp"))}</a></p><p class="fine">${esc(S("loading"))}</p>`;
  const docs = await Promise.all(pair.voices.map(v => {
    const m = D.mods.shipped.find(x => x.id === v.text);
    return text(m.datei).then(t => ({ v, m, t }));
  }));
  const col = ({ v, m, t }) => {
    const sec = t.sections.find(s => s.id === v.sec);
    const units = v.n.map(n => sec.units.find(u => u.n === n)).filter(Boolean);
    return `<div class="voice">
      <div class="vhead">${side(m.side)} <b>${esc(L(t, "autor"))}</b><br><span class="fine">${esc(t.jahr)} · ${esc(L(sec, "titel"))}</span></div>
      ${units.map(u => `<div class="vunit">
        <div class="fine"><a href="#/text/${m.id}/${sec.id}/${u.n}">${esc(sec.zk)} [${u.n}]</a>${u.titel ? ` · ${esc(L(u, "titel"))}` : ""}</div>
        <div class="text">${esc(ui === "de" && u.orig && (u.lang || t.orig_sprache) === "de" ? u.orig : u.en)}</div></div>`).join("")}
    </div>`;
  };
  view.innerHTML = `
    <p class="fine"><a href="#/compare">${esc(S("allCmp"))}</a></p>
    <span class="tag">${esc(S("cmpTag"))}</span><h1>${esc(L(pair, "titel"))}</h1>
    <p class="lede">${esc(L(pair, "frage"))}</p>
    <div class="panel readable"><p>${esc(L(pair, "note"))}</p></div>
    <div class="cmp n${docs.length}">${docs.map(col).join("")}</div>`;
}

/* ------------------------------------------------------------ timeline */
function timeline() {
  const TL = D.timeline;
  view.innerHTML = `
    <span class="tag">${esc(S("tlTag"))}</span><h1>1792–1794</h1>
    <p class="lede">${esc(L(TL, "lede"))}</p>
    <div class="legend">${Object.keys(SIDES).map(side).join(" ")}</div>
    <div class="tl">${TL.stations.map(s => {
      const p = s.plate && plateOf(s.plate);
      return `<div class="st" style="--c:var(--${s.side})">
        <div><div class="d">${esc(L(s, "d"))} · ${side(s.side)}</div><h3>${esc(L(s, "titel"))}</h3><p>${esc(L(s, "text"))}</p>
        ${s.cite ? `<p class="fine"><a href="${s.cite}">✦ ${esc(L(s, "citeLabel"))}</a></p>` : ""}</div>
        ${p ? `<img src="assets/plates/${p.id}_t.jpg" alt="${esc(L(p, "titel"))}" title="${esc(L(p, "titel"))}">` : "<span></span>"}
      </div>`;
    }).join("")}</div>`;
}

/* ------------------------------------------------------------ plates */
function plates() {
  view.innerHTML = `
    <span class="tag">${esc(S("platesTag"))}</span><h1>${esc(S("platesH"))}</h1>
    <p class="lede">${esc(L(D.plates, "lede"))}</p>
    <div class="grid g4">${D.plates.plates.map(p => `
      <figure class="plate card"><a href="#" data-p="${p.id}"><img src="assets/plates/${p.id}_t.jpg" alt="${esc(L(p, "titel"))}"></a>
      <figcaption>${side(p.side)} <b>${esc(L(p, "titel"))}</b><br>${esc(L(p, "caption"))}<br><i>${esc(p.source)}</i></figcaption></figure>`).join("")}</div>
    <p class="fine">${esc(L(D.plates, "credit"))}</p>`;
  view.querySelectorAll("[data-p]").forEach(a => a.onclick = e => {
    e.preventDefault();
    const p = plateOf(a.dataset.p);
    const lb = document.createElement("div");
    lb.className = "lightbox";
    lb.innerHTML = `<figure><img src="assets/plates/${p.id}.jpg" alt="${esc(L(p, "titel"))}"><figcaption class="cap"><b>${esc(L(p, "titel"))}.</b> ${esc(L(p, "caption"))}</figcaption></figure>`;
    lb.onclick = () => lb.remove();
    document.body.append(lb);
  });
}

/* ------------------------------------------------------------ sources */
const METHOD = {
  de: {
    tag: "Quellen, Methode, Grenzen", h: "Wie dieser Apparat gemacht ist",
    p: [
      ["Nur Gemeinfreies.", "Jeder Text stammt aus einem Druck, dessen Schutzfrist abgelaufen ist; die Quelle steht auf seiner Seite. Die großen modernen Editionen der Mainzer Republik, Heinrich Scheels Protokolle des Klubs und des Konvents (1975–1989) und Joseph Hansens Quellen zur Geschichte des Rheinlandes (1931–1938), sind noch geschützt und werden nicht benutzt; was sie enthalten, wird hier aus den Drucken von 1792 und 1793 und aus den Ausgaben des 19. Jahrhunderts gezeigt, oder als Lücke benannt."],
      ["Die Seite ist maßgeblich.", "Die Texte sind am Seitenbild gelesen, nicht aus der maschinellen Texterkennung übernommen, die bei Fraktur nur Hilfsmittel ist. Schreibung und Zeichensetzung der Drucke bleiben erhalten; jede Korrektur, die über das Offensichtliche hinausgeht, steht in den Anmerkungen."],
      ["Englische Übersetzungen.", "Die englischen Übersetzungen sind eigene Arbeit, nah am Original und gemeinfrei (CC0), eine Lesehilfe, keine kritische Übersetzung. Wo es eine gemeinfreie zeitgenössische Übersetzung gibt, etwa für Goethes Belagerung von Mainz, steht sie an ihrer Stelle und ist als solche gekennzeichnet."],
      ["Stimmen und Abstände.", "Die Proklamationen sprechen für die Besatzung, die Reden für den Klub, die Beschlüsse für den Konvent, die Gegenschriften für den Kurfürsten und die Zünfte; Goethe schrieb dreißig Jahre danach, König und Klein ein halbes Jahrhundert danach, jeder für sein Publikum. Jedes Modul nennt, wer schrieb, wann und für wen."],
      ["Daten.", "Die Texte datieren teils nach dem gregorianischen, teils nach dem französischen Revolutionskalender; die Daten stehen wie gedruckt, mit dem gregorianischen Datum daneben."]
    ],
    printed: "Abgedruckte Quellen", plates: "Tafeln"
  },
  en: {
    tag: "Sources, method, limits", h: "How this apparatus is made",
    p: [
      ["Public domain only.", "Every text comes from a print whose term of protection has expired; the source is named on its page. The great modern editions of the Mainz Republic, Heinrich Scheel's minutes of the club and the Convention (1975–1989) and Joseph Hansen's Quellen zur Geschichte des Rheinlandes (1931–1938), are still protected and are not used; what they contain is shown here from the prints of 1792 and 1793 and from nineteenth-century editions, or named as a gap."],
      ["The page decides.", "The texts are read against the page images, not taken from machine text recognition, which for blackletter is only an aid. Spelling and punctuation of the prints are kept; any correction beyond the obvious is given in the notes."],
      ["English translations.", "The English translations are my own, close to the original and in the public domain (CC0): a reading aid, not a critical translation. Where a public-domain translation of the period exists, as for Goethe's Siege of Mainz, it stands in its place and is marked as such."],
      ["Voices and distances.", "The proclamations speak for the occupying army, the speeches for the club, the decrees for the Convention, the counter-pamphlets for the Elector and the guilds; Goethe wrote thirty years after the event, König and Klein half a century after, each for his own public. Every module says who wrote, when and for whom."],
      ["Dates.", "Some texts are dated by the Gregorian calendar, some by the French revolutionary calendar; dates stand as printed, with the Gregorian date beside them."]
    ],
    printed: "Sources printed here", plates: "Plates"
  }
};

function sources() {
  const M = METHOD[ui];
  view.innerHTML = `
    <span class="tag">${esc(M.tag)}</span><h1>${esc(M.h)}</h1>
    <div class="readable">${M.p.map(([b, p]) => `<p><b>${esc(b)}</b> ${esc(p)}</p>`).join("")}</div>
    ${D.mods.shipped.length ? `<h2>${esc(M.printed)}</h2>
    <div class="grid g2">${D.mods.shipped.map(m => `<div class="panel"><b>${esc(L(m, "kurz"))}</b><p class="fine" id="src-${m.id}">…</p></div>`).join("")}</div>` : ""}
    ${(D.plates.plates || []).length ? `<h2>${esc(M.plates)}</h2><p class="fine readable">${esc(L(D.plates, "credit"))}</p>` : ""}`;
  D.mods.shipped.forEach(async m => {
    const t = await text(m.datei);
    const el = document.getElementById("src-" + m.id);
    if (el) el.textContent = t.quelle;
  });
}

boot().catch(e => { view.innerHTML = `<p>${esc(S("fail"))}${esc(e.message)}</p>`; });
