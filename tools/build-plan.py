"""Writes the scaffold data of the apparatus: planned modules, timeline, empty plates and comparisons.

Run once from the repository root (python tools/build-plan.py). As modules are shipped,
modules.json, timeline.json, plates.json and compare.json are maintained by their own scripts
and by hand; this script is the starting point, not a generator to re-run over them.
"""
import json, os

ROOT = os.path.join(os.path.dirname(__file__), "..", "data")


def mod(id, side, zk, kurz, kurz_en, warum, warum_en, quelle):
    return dict(id=id, side=side, zk=zk, kurz=kurz, kurz_en=kurz_en, warum=warum, warum_en=warum_en, quelle=quelle)


PLANNED = [
    mod("custine", "franzosen", "Custine",
        "Custine an die Mainzer (Oktober–November 1792)", "Custine to the people of Mainz (October–November 1792)",
        "Die Proklamationen des Generals nach der Einnahme: Freiheit für die Völker, Krieg den Palästen, Kontributionen für Adel und Geistlichkeit. Gedruckt deutsch und französisch, für die Mainzer geschrieben, im Namen der Republik.",
        "The general's proclamations after the capture: liberty to the peoples, war on the palaces, levies on nobility and clergy. Printed in German and French, written for the people of Mainz, in the name of the Republic.",
        "Zeitgenössische Einblattdrucke 1792 (Bayerische Staatsbibliothek, zu sichten); Abdrucke bei K. Klein, Georg Forster in Mainz (1863)."),
    mod("forster1792", "klub", "Forster 1792",
        "Forster im Klub: die Reden vom November 1792", "Forster in the club: the speeches of November 1792",
        "Der Weltreisende und Universitätsbibliothekar tritt dem Klub bei und spricht über das Verhältnis der Mainzer zu den Franken: warum man frei sein soll, und warum mit Frankreich. Die tragende Stimme des Apparats, in ihrem ersten Auftritt.",
        "The circumnavigator and university librarian joins the club and speaks on the relation of the people of Mainz to the French: why they should be free, and why with France. The apparatus's leading voice, in its first appearance.",
        "G. Forster, Sämmtliche Schriften, hg. von seiner Tochter und G. G. Gervinus (Leipzig 1843), Band zu prüfen; Erstdrucke Mainz 1792."),
    mod("eid", "klub", "Wahl und Eid",
        "Wahl und Eid (Februar 1793)", "Election and oath (February 1793)",
        "Die Kommissare des Pariser Nationalkonvents schreiben Wahlen aus: wählen darf, wer der Freiheit und Gleichheit Treue schwört und dem Kurfürsten entsagt. Die Eidformel, die Wahlordnung und die Berichte über Gemeinden, die den Eid verweigerten.",
        "The commissioners of the National Convention in Paris call elections: whoever swears loyalty to liberty and equality and renounces the Elector may vote. The oath, the electoral rules and the reports of communities that refused it.",
        "Drucke 1793 (zu suchen); Abdrucke bei Klein (1863) und F. X. Remling, Die Rheinpfalz in der Revolutionszeit von 1792 bis 1798 (Speyer 1865–1866)."),
    mod("konvent", "klub", "Konvent",
        "Der Rheinisch-Deutsche Nationalkonvent (17.–21. März 1793)", "The Rhenish-German National Convention (17–21 March 1793)",
        "Im Deutschhaus, dem heutigen Landtag von Rheinland-Pfalz, erklärt der Konvent das Land von Landau bis Bingen für frei und unabhängig, sagt sich von Kaiser und Reich los und beschließt drei Tage später, den Anschluss an Frankreich zu erbitten.",
        "In the Deutschhaus, today the seat of the Landtag of Rhineland-Palatinate, the Convention declares the land from Landau to Bingen free and independent, renounces Emperor and Empire, and three days later resolves to ask for union with France.",
        "Dekrete des Konvents, Drucke Mainz 1793 (zu suchen); Abdrucke bei Klein (1863) und Remling (1865–1866)."),
    mod("darstellung", "klub", "Darstellung",
        "Forster: Darstellung der Revolution in Mainz (1793)", "Forster: Account of the Revolution in Mainz (1793)",
        "In Paris, abgeschnitten von der belagerten Stadt, beginnt Forster eine Darstellung dessen, was in Mainz geschehen war, und bricht sie ab. Ein Rechenschaftsbericht und eine Verteidigung, geschrieben, als die Stadt noch nicht gefallen war.",
        "In Paris, cut off from the besieged city, Forster begins an account of what had happened in Mainz, and leaves it unfinished. A report and a defence, written while the city had not yet fallen.",
        "G. Forster, Sämmtliche Schriften (1843), Band zu prüfen."),
    mod("gegenschrift", "reich", "Gegenschrift",
        "Gegenstimmen aus der Stadt (1793)", "Voices against, from the city (1793)",
        "Was die Mainzer sagten, die nicht schworen: Proteste der Zünfte, Schriften gegen die Klubisten, und die Flugschrift „Mainz im Genusse der … Freiheit und Gleichheit“, nach ihrem Titel eine Gegenschrift.",
        "What the people of Mainz said who did not swear: protests of the guilds, pamphlets against the Clubists, and the pamphlet ‘Mainz im Genusse der … Freiheit und Gleichheit’, by its title a counter-pamphlet.",
        "Flugschrift 1793 (Bayerische Staatsbibliothek, bsb11779263, Charakter zu prüfen); weitere Drucke zu sichten."),
    mod("belagerung", "zeugen", "Belagerung",
        "Tagebücher der Belagerung (April–Juli 1793)", "Diaries of the siege (April–July 1793)",
        "Die Belagerten zählen Kugeln, Brände und Brotpreise: zwei Tagebücher und eine Beschreibung der Festung, gedruckt 1793, als alles noch frisch war, von Mainzern, die in der Stadt blieben.",
        "The besieged count cannonballs, fires and the price of bread: two diaries and a description of the fortress, printed in 1793 while everything was still fresh, by people of Mainz who stayed in the city.",
        "„Mein Tagebuch der Belagerung von Mainz“ (1793, bsb11252758); „Die Belagerung der Stadt Mainz …“ (1793, bsb11694602); Gymnich, Beschreibung der Vestung Mainz (1793, bsb11087309)."),
    mod("goethe", "zeugen", "Goethe",
        "Goethe: Belagerung von Mainz (1793/1822)", "Goethe: The Siege of Mainz (1793/1822)",
        "Goethe begleitet den Herzog von Weimar ins Lager der Belagerer, sieht die Stadt brennen und nach der Kapitulation die Klubisten abziehen, und schreibt es dreißig Jahre später auf. Deutsch, mit der gemeinfreien englischen Übersetzung von 1882.",
        "Goethe accompanies the Duke of Weimar to the besiegers' camp, watches the city burn and, after the capitulation, the Clubists leaving, and writes it down thirty years later. German, with the public-domain English translation of 1882.",
        "J. W. von Goethe, Belagerung von Mainz (1822); engl. in Goethe, Miscellaneous Travels (London: Bell, 1882)."),
    mod("caroline", "zeugen", "Caroline",
        "Caroline Böhmer: Briefe aus Mainz (1792–1793)", "Caroline Böhmer: letters from Mainz (1792–1793)",
        "Die junge Witwe lebt im Kreis der Forsters, schreibt über Klub und Besatzung mit Witz und Sympathie, flieht im März 1793 und wird von preußischen Truppen verhaftet. Eine Stimme aus der Stadt, die nicht im Konvent saß.",
        "The young widow lives in the Forsters' circle, writes about club and occupation with wit and sympathy, flees in March 1793 and is arrested by Prussian troops. A voice from the city that had no seat in the Convention.",
        "Caroline. Briefe an ihre Geschwister, ihre Tochter Auguste, die Familie Gotter, F. L. W. Meyer, A. W. und Fr. Schlegel …, hg. von G. Waitz (Leipzig 1871)."),
    mod("nachleben", "rezeption", "Nachleben",
        "Klubisten im 19. Jahrhundert: König und Klein", "Clubists in the nineteenth century: König and Klein",
        "Wie das 19. Jahrhundert die Mainzer Republik las: Heinrich Königs Roman „Die Clubbisten in Mainz“ (1847) im Vormärz, Karl Kleins Darstellung „Georg Forster in Mainz“ (1863) mit den Akten im Anhang.",
        "How the nineteenth century read the Mainz Republic: Heinrich König's novel ‘Die Clubbisten in Mainz’ (1847) on the eve of 1848, Karl Klein's ‘Georg Forster in Mainz’ (1863) with documents in its appendix.",
        "H. König, Die Clubbisten in Mainz (Leipzig 1847); K. Klein, Georg Forster in Mainz 1788 bis 1793 (Gotha 1863)."),
]

MISSING = [
    mod("scheel", "klub", "Scheel",
        "Die Protokolle von Klub und Konvent (Scheel)", "The minutes of club and Convention (Scheel)",
        "Die vollständige moderne Edition der Protokolle und Akten, Heinrich Scheel, Die Mainzer Republik I–III (Berlin 1975–1989), ist urheberrechtlich geschützt und wird nicht benutzt. Was sie enthält, zeigt der Apparat aus den Drucken von 1793 und aus Klein (1863), oder nennt es als Lücke.",
        "The complete modern edition of the minutes and records, Heinrich Scheel, Die Mainzer Republik I–III (Berlin 1975–1989), is protected by copyright and is not used. What it contains, the apparatus shows from the prints of 1793 and from Klein (1863), or names as a gap.",
        "H. Scheel (Hg.), Die Mainzer Republik, 3 Bde. (Berlin 1975–1989)."),
    mod("hansen", "franzosen", "Hansen",
        "Hansens Quellen zur Geschichte des Rheinlandes", "Hansen's sources for the history of the Rhineland",
        "Joseph Hansens Quellensammlung (1931–1938) ist in Deutschland seit 2014 frei, siebzig Jahre nach dem Tod des Herausgebers, in den Vereinigten Staaten aber erst Band für Band ab 2027. Weil der Apparat in den Vereinigten Staaten betrieben wird, wartet er.",
        "Joseph Hansen's collection (1931–1938) has been free in Germany since 2014, seventy years after the editor's death, but in the United States only volume by volume from 2027. Because the apparatus is run from the United States, it waits.",
        "J. Hansen (Hg.), Quellen zur Geschichte des Rheinlandes im Zeitalter der Französischen Revolution 1780–1801, 4 Bde. (Bonn 1931–1938)."),
]

NOTE, NOTE_EN = " (Nach modernen Darstellungen; Modul geplant.)", " (After modern accounts; module planned.)"


def st(d, d_en, side, titel, titel_en, text, text_en):
    return dict(d=d, d_en=d_en, side=side, titel=titel, titel_en=titel_en, text=text + NOTE, text_en=text_en + NOTE_EN)


STATIONS = [
    st("21. Oktober 1792", "21 October 1792", "franzosen", "Custine in Mainz", "Custine in Mainz",
       "Die Revolutionsarmee unter General Custine nimmt die kurfürstliche Festung fast kampflos; der Kurfürst ist geflohen.",
       "The revolutionary army under General Custine takes the Elector's fortress almost without a fight; the Elector has fled."),
    st("23. Oktober 1792", "23 October 1792", "klub", "Der Klub", "The club",
       "Zwanzig Mainzer gründen die Gesellschaft der Freunde der Freiheit und Gleichheit, den Jakobinerklub.",
       "Twenty citizens of Mainz found the Society of the Friends of Liberty and Equality, the Jacobin club."),
    st("November 1792", "November 1792", "klub", "Forster spricht", "Forster speaks",
       "Georg Forster tritt dem Klub bei und wird seine bekannteste Stimme.",
       "Georg Forster joins the club and becomes its best-known voice."),
    st("15. Dezember 1792", "15 December 1792", "franzosen", "Das Dekret von Paris", "The Paris decree",
       "Der Nationalkonvent in Paris bestimmt, wie in den besetzten Gebieten die alte Ordnung abgeschafft und neue Verwaltungen gewählt werden sollen.",
       "The National Convention in Paris determines how the old order is to be abolished in the occupied territories and new administrations elected."),
    st("24. Februar 1793", "24 February 1793", "klub", "Wahl und Eid", "Election and oath",
       "Wahlen in Mainz und den Gemeinden der Umgebung; wählen darf, wer schwört. Viele verweigern den Eid.",
       "Elections in Mainz and the surrounding communities; whoever swears may vote. Many refuse the oath."),
    st("17.–18. März 1793", "17–18 March 1793", "klub", "Der Konvent im Deutschhaus", "The Convention in the Deutschhaus",
       "Der Rheinisch-Deutsche Nationalkonvent tritt zusammen, Andreas Joseph Hofmann als Präsident, Forster als Vizepräsident, und erklärt das Land von Landau bis Bingen für frei.",
       "The Rhenish-German National Convention meets, with Andreas Joseph Hofmann as president and Forster as vice-president, and declares the land from Landau to Bingen free."),
    st("21. März 1793", "21 March 1793", "klub", "Der Anschluss", "Union",
       "Der Konvent beschließt, den Anschluss an Frankreich zu erbitten; Forster reist mit Adam Lux nach Paris, um ihn zu überbringen.",
       "The Convention resolves to ask for union with France; Forster travels to Paris with Adam Lux to deliver the request."),
    st("Ende März 1793", "Late March 1793", "zeugen", "Caroline flieht", "Caroline flees",
       "Caroline Böhmer verlässt Mainz, wird auf der Flucht von preußischen Truppen verhaftet und auf die Festung Königstein gebracht.",
       "Caroline Böhmer leaves Mainz, is arrested in flight by Prussian troops and taken to the fortress of Königstein."),
    st("April 1793", "April 1793", "reich", "Die Einschließung", "The investment",
       "Preußische, österreichische und Reichstruppen schließen die Stadt ein.",
       "Prussian, Austrian and Imperial troops close round the city."),
    st("Juni–Juli 1793", "June–July 1793", "zeugen", "Die Beschießung", "The bombardment",
       "Die Belagerer beschießen die Stadt; der Dom brennt. Goethe sieht es aus dem Lager.",
       "The besiegers bombard the city; the cathedral burns. Goethe watches from the camp."),
    st("23. Juli 1793", "23 July 1793", "reich", "Die Kapitulation", "The capitulation",
       "Die französische Besatzung kapituliert und zieht mit Waffen ab; die zurückgebliebenen Klubisten sind der Rache der Stadt und der Haft ausgeliefert.",
       "The French garrison capitulates and marches out under arms; the Clubists left behind are exposed to the city's revenge and to prison."),
    st("10. Januar 1794", "10 January 1794", "klub", "Forster stirbt", "Forster dies",
       "Georg Forster stirbt in Paris, ohne Mainz wiedergesehen zu haben.",
       "Georg Forster dies in Paris without having seen Mainz again."),
]


def dump(name, obj):
    with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=1)
        f.write("\n")


if __name__ == "__main__":
    dump("modules.json", {"shipped": [], "planned": PLANNED, "missing": MISSING})
    dump("timeline.json", {
        "lede": "Von der Einnahme der Stadt bis zu Forsters Tod. Die Stationen folgen vorerst modernen Darstellungen; mit jedem Modul werden sie an den Quellen geprüft und verweisen dann in die Texte.",
        "lede_en": "From the taking of the city to Forster's death. For now the stations follow modern accounts; with each module they are checked against the sources and then point into the texts.",
        "stations": STATIONS})
    dump("plates.json", {
        "lede": "Bildnisse, Flugblätter, Ansichten der Stadt und der Belagerung, alle gemeinfrei, mit den Modulen nach und nach.",
        "lede_en": "Portraits, broadsides, views of the city and the siege, all in the public domain, added module by module.",
        "credit": "", "credit_en": "", "plates": []})
    dump("compare.json", {
        "lede": "Dieselben Tage aus dem Klub, aus dem Lager und aus der Stadt. Die Vergleiche entstehen mit den Modulen.",
        "lede_en": "The same days from the club, from the camp and from the city. The comparisons will be added with the modules.",
        "pairs": []})
    print("ok")
