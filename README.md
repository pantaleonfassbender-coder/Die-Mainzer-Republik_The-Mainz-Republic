# Die Mainzer Republik – The Mainz Republic

Ein zweisprachiger Quellenapparat zur Mainzer Republik 1792–1793: Was bleibt von einer Republik, die vier Monate dauerte? Gemeinfreie Quellen im deutschen Original neben einer englischen Übersetzung, eine Zeitleiste mit Verweisen in die Texte, Vergleiche und Tafeln. Die Oberfläche lässt sich zwischen Deutsch und Englisch umschalten.

*A bilingual documentary apparatus on the Mainz Republic, 1792–1793: what remains of a republic that lasted four months? Public-domain sources in the German original beside an English translation, a timeline pointing into the texts, comparisons and plates. The interface switches between German and English.*

Die These, an den Texten zu prüfen: Unter französischer Besatzung gründeten Mainzer einen Klub, wählten unter Eid einen Konvent, der am 18. März 1793 im Deutschhaus das Land von Landau bis Bingen für frei erklärte, und verloren die Stadt am 23. Juli 1793 an die Belagerer. Georg Forster ist die Stimme, die durch alle Teile geht; Goethe sah die Belagerung aus dem Lager, Caroline Böhmer den Winter aus der Stadt.

**Stand:** Im Aufbau, zehn Module geplant. Abgedruckt:

- **Custine vor Mainz: Aufforderung und Übergabe (Oktober 1792)** — [Anton Hoffmann], *Darstellung der Mainzer Revolution*, Heft 1 (1793), Beylagen No. 1–9 und Erzählung, mit einer Anmerkung aus Heft 2; am Seitenbild gelesen, mit englischer Übersetzung.
- **Forster im Klub: die Rede vom November 1792** — Georg Forster, *Ueber das Verhältniß der Mainzer gegen die Franken*, vollständig nach den Sämmtlichen Schriften, Bd. 6 (1843), S. 413–431; dazu Anton Hoffmann über Forsters Eintritt, das rote und das schwarze Buch und die Rede (Heft 3, S. 222–234; Heft 4, S. 256–260); am Seitenbild gelesen, mit englischer Übersetzung.

Dazu drei Vergleiche (freie Wahl, das Buch, der Redner und sein Gegner). Geplant sind Forsters *Darstellung der Revolution in Mainz*, Wahl und Eid, der Konvent, Gegenstimmen aus der Stadt, Tagebücher der Belagerung, Goethe, Caroline Böhmer und das Nachleben bei König und Klein; die Seite „Texte“ nennt sie mit ihren Quellen und dazu, was geprüft und nicht aufgenommen wurde. Die Tafeln stammen aus gemeinfreien oder CC0-Reproduktionen über Wikimedia Commons (`tools/build-plates.py`).

**Nur Gemeinfreies.** Die großen modernen Editionen (Scheel 1975–1989; Hansen 1931–1938, in den USA bandweise erst ab 2027 frei) werden nicht benutzt; jeder Text ist am Seitenbild eines gemeinfreien Drucks gelesen.

**Begleitspiel:** *Der Freiheitsbaum – The Liberty Tree* (in Arbeit): Man führt den Konvent durch Wahl, Eid und Belagerung; die Stadt fällt, wie sie gefallen ist, gewertet wird, was bleibt.

## Aufbau

Statische Site ohne Build-Schritt: `index.html`, `app.js` (Hash-Routen, Sprachumschalter), `style.css`, `legal.html`; Daten in `data/` (`modules.json`, `timeline.json`, `compare.json`, `plates.json`, je Modul eine Datei); Bauskripte in `tools/`. Felder mit dem Suffix `_en` tragen die englische Fassung; fehlt sie, zeigt die Site die deutsche.

Lokal: `python -m http.server` im Repository, dann `http://localhost:8000/`.

## Lizenzen

Code MIT; redaktionelle Texte CC BY 4.0; Editionen und Übersetzungen CC0 1.0. Siehe [LICENSES.md](LICENSES.md).
