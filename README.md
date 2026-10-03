# Die Mainzer Republik – The Mainz Republic

Ein zweisprachiger Quellenapparat zur Mainzer Republik 1792–1793: Was bleibt von einer Republik, die vier Monate dauerte? Gemeinfreie Quellen im deutschen Original neben einer englischen Übersetzung, eine Zeitleiste mit Verweisen in die Texte, Vergleiche und Tafeln. Die Oberfläche lässt sich zwischen Deutsch und Englisch umschalten.

*A bilingual documentary apparatus on the Mainz Republic, 1792–1793: what remains of a republic that lasted four months? Public-domain sources in the German original beside an English translation, a timeline pointing into the texts, comparisons and plates. The interface switches between German and English.*

Die These, an den Texten zu prüfen: Unter französischer Besatzung gründeten Mainzer einen Klub, wählten unter Eid einen Konvent, der am 18. März 1793 im Deutschhaus das Land von Landau bis Bingen für frei erklärte, und verloren die Stadt am 23. Juli 1793 an die Belagerer. Georg Forster ist die Stimme, die durch alle Teile geht; Goethe sah die Belagerung aus dem Lager, Caroline Böhmer den Winter aus der Stadt.

**Stand:** Alle zehn geplanten Module sind abgedruckt:

- **Custine vor Mainz: Aufforderung und Übergabe (Oktober 1792)** — [Anton Hoffmann], *Darstellung der Mainzer Revolution*, Heft 1 (1793), Beylagen No. 1–9 und Erzählung, mit einer Anmerkung aus Heft 2; am Seitenbild gelesen, mit englischer Übersetzung.
- **Forster im Klub: die Rede vom November 1792** — Georg Forster, *Ueber das Verhältniß der Mainzer gegen die Franken*, vollständig nach den Sämmtlichen Schriften, Bd. 6 (1843), S. 413–431; dazu Anton Hoffmann über Forsters Eintritt, das rote und das schwarze Buch und die Rede (Heft 3, S. 222–234; Heft 4, S. 256–260); am Seitenbild gelesen, mit englischer Übersetzung.

- **Wahl und Eid (16.–24. Februar 1793)** — [Anton Hoffmann], *Darstellung der Mainzer Revolution*, Heft 9 (S. 641–672, Beylagen No. 56–59) und Heft 10 (Beylagen No. 65–66, S. 750–754): Custines Eidbefehl, die Proklamationen der Kommissare, die Vorstellung der Geistlichkeit, Aufschub und Widerruf, die Ausweisungen und der Wahltag; am Seitenbild gelesen, mit englischer Übersetzung.

- **Der Konvent: Freistaat und Anschluss (17.–29. März 1793)** — [Anton Hoffmann], *Darstellung der Mainzer Revolution*, Heft 11 (S. 801–822, Beylagen No. 78–80 und 83): die Eröffnung im Deutschhaus, das Freistaatsdekret vom 18. März, der Anschlussbeschluss vom 21. März mit dem Schreiben nach Paris und das Gesetz über die Nichtschwörenden vom 27. März; am Seitenbild gelesen, mit englischer Übersetzung.

- **Die Belagerung: ein Tagebuch aus dem Gefängnis (Februar–Juli 1793)** — Karl Wilhelm Friedrich Schaber, *Mein Tagebuch der Belagerung von Mainz, geschrieben in Mainz* (Frankfurt 1793): Gefangenschaft, Einschließung, Hunger, die Brände von Liebfrauenkirche und Dom, die Kapitulation; am Seitenbild gelesen, mit englischer Übersetzung.

- **Goethe: Belagerung von Maynz (Mai–Juli 1793)** — deutsch nach der Erstausgabe, *Aus meinem Leben*, Zweyter Abtheilung fünfter Theil (Cotta 1822), S. 417–485; englisch in der gemeinfreien Übersetzung der *Miscellaneous Travels*, hg. von L. Dora Schmitz (London 1884), S. 251–279; beide am Seitenbild gelesen.

- **Caroline: Briefe aus Mainz und aus der Haft (Oktober 1792 – Juni 1793)** — *Caroline. Briefe*, hg. von G. Waitz, Bd. 1 (Leipzig 1871), Nr. 68–79; am Seitenbild gelesen, mit englischer Übersetzung.

- **Gegenstimmen: Mainz im Genusse der Freiheit und Gleichheit (1793)** — anonyme Mainzer Flugschrift, S. 6–9, 17–28; am Seitenbild gelesen, mit englischer Übersetzung.

- **Forster: Darstellung der Revolution in Mainz (Fragment, 1792)** — Sämmtliche Schriften, Bd. 6 (1843), S. 352–412, Auszüge; am Seitenbild gelesen, mit englischer Übersetzung.
- **Nachleben: Namensverzeichnis, Roman und Anklage (1793–1863)** — *Getreues Namensverzeichniß der in Mainz sich befindenden 454 Klubbisten* (Frankfurt 1793); Heinrich Koenig, *Die Clubisten in Mainz*, Erster Theil (1847), S. 22–23, 57–59; K. Klein, *Georg Forster in Mainz 1788 bis 1793* (1863), Vorwort und S. 22–23; am Seitenbild gelesen, mit englischer Übersetzung.

Dazu vierundzwanzig Vergleiche. Die Seite „Texte“ nennt alle Module mit ihren Quellen und dazu, was geprüft und nicht aufgenommen wurde. Die Tafeln stammen aus gemeinfreien oder CC0-Reproduktionen über Wikimedia Commons (`tools/build-plates.py`).

**Nur Gemeinfreies.** Die großen modernen Editionen (Scheel 1975–1989; Hansen 1931–1938, in den USA bandweise erst ab 2027 frei) werden nicht benutzt; jeder Text ist am Seitenbild eines gemeinfreien Drucks gelesen.

**Begleitspiel:** *Der Freiheitsbaum – The Liberty Tree* (in Arbeit): Man führt den Konvent durch Wahl, Eid und Belagerung; die Stadt fällt, wie sie gefallen ist, gewertet wird, was bleibt.

## Aufbau

Statische Site ohne Build-Schritt: `index.html`, `app.js` (Hash-Routen, Sprachumschalter), `style.css`, `legal.html`; Daten in `data/` (`modules.json`, `timeline.json`, `compare.json`, `plates.json`, je Modul eine Datei); Bauskripte in `tools/`. Felder mit dem Suffix `_en` tragen die englische Fassung; fehlt sie, zeigt die Site die deutsche.

Lokal: `python -m http.server` im Repository, dann `http://localhost:8000/`.

## Lizenzen

Code MIT; redaktionelle Texte CC BY 4.0; Editionen und Übersetzungen CC0 1.0. Siehe [LICENSES.md](LICENSES.md).
