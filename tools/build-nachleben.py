"""Modul „Nachleben“: das Namensverzeichnis (1793), Königs Roman (1847), Kleins Anklage (1863).

Quellen:
- Getreues Namensverzeichniß der in Mainz sich befindenden 454 Klubbisten, mit Bemerkung derselben Charakter
  (Frankfurt, gedruckt im Juny, 1793), Titel, S. 2, 5, 6. Gelesen an den Seitenbildern des Internet Archive,
  bub_gb_lNZBAAAAcAAJ (Exemplar der Bayerischen Staatsbibliothek; Bild n = Seite + 3).
- Heinrich Koenig, Die Clubisten in Mainz. Ein Roman, Erster Theil (Leipzig: Brockhaus 1847), S. 22–23, 57–59.
  Gelesen an den Seitenbildern, Internet Archive 11750809bsb (Bild n = Seite + 5).
- K. Klein, Georg Forster in Mainz 1788 bis 1793, nebst Nachträgen zu seinen Werken (Gotha: Perthes 1863),
  Vorwort S. V–VIII, Einleitung S. 22–23. Gelesen an den Seitenbildern, Internet Archive bub_gb_2_o5AAAAcAAJ
  (Bild n = römische Seite + 5, arabische Seite + 17).
Schreibung der Drucke; ſ als s; Silbentrennung aufgelöst; Sperrungen nicht wiedergegeben. Auslassungen […].
"""
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "data" / "nachleben.json"


def u(n, pg, titel, titel_en, orig, en, note="", note_en=""):
    d = {"n": n, "pg": pg, "titel": titel, "titel_en": titel_en, "orig": orig.strip(), "en": en.strip()}
    if note:
        d["note"], d["note_en"] = note, note_en
    return d


PRANGER = [
    u(1, "NV, Titel", "Das Titelblatt", "The title page",
      """Getreues Namensverzeichniß der in Mainz sich befindenden 454 Klubbisten, mit Bemerkung derselben Charakter.
Das Stück gebunden kostet 3 kr.
Frankfurt, gedruckt im Juny, 1793.""",
      """Faithful List of Names of the 454 Clubists to Be Found in Mainz, with a Note on Their Character.
Price per copy, bound, 3 kreuzers.
Frankfurt, printed in June 1793.""",
      "Gedruckt im Juni 1793 in Frankfurt, während Mainz belagert wurde: eine Liste derer, die sich „in Mainz befinden“, alphabetisch, für drei Kreuzer, also für jedermann. Einen Verfasser nennt das Heft nicht, einen Zweck auch nicht. Die meisten Einträge bestehen nur aus Name und Beruf; bei manchen steht ein Urteil. Nach der Übergabe im Juli wurden Klubisten in der Stadt misshandelt; Goethe sah es mit an (Goethe [7]; Goethe [10]).",
      "Printed in Frankfurt in June 1793, while Mainz was under siege: a list of those 'to be found in Mainz', alphabetical, for three kreuzers, that is, for anyone. The booklet names no author and no purpose. Most entries give only a name and a trade; some carry a verdict. After the surrender in July, Clubists in the city were mistreated; Goethe watched it happen (Goethe [7]; Goethe [10])."),
    u(2, "NV, 2", "Zwei Geistliche in Königstein", "Two clergymen in Königstein",
      """Arandt, von Geburt ein Eichsfelder, Dr. Theologiae, und ehemaliger Pfarrer zu Nackenheim, hierauf von der fränkischen Administration angestelter Regens im Seminarium zu Mainz: ließ sich einfallen, constitutionsmäßiger Bischof in Mainz werden zu wollen, wurde aber ohnlängst von den Preußen erwischt, und büßt dermalen in der Festung Königstein seinen Stolz und Narrheit.
Arnsberger, ehemaliger Kaplan zu Kassel bei Mainz, ein bekannter Volksaufwiegler, wurde ebenfalls von den Preußen gefangen, und sizt auch zu Königstein.""",
      """Arandt, an Eichsfelder by birth, Doctor of Theology, and formerly parish priest at Nackenheim, then appointed by the Frankish administration as rector of the seminary at Mainz: took it into his head to want to become constitutional bishop in Mainz, but was caught not long ago by the Prussians and is now atoning in the fortress of Königstein for his pride and folly.
Arnsberger, formerly chaplain at Kastel near Mainz, a well-known agitator of the people, was likewise captured by the Prussians and also sits at Königstein.""",
      "„Kassel bei Mainz“ ist Kastel auf dem rechten Rheinufer. Ein „constitutionsmäßiger Bischof“ wäre ein Bischof nach französischem Recht gewesen, gewählt statt vom Domkapitel bestellt. In der Festung Königstein saß in diesen Monaten auch Caroline Böhmer (Caroline [8]; Tafel).",
      "'Kassel near Mainz' is Kastel on the right bank of the Rhine. A 'constitutional bishop' would have been a bishop under French law, elected rather than appointed by the cathedral chapter. In these months Caroline Böhmer was also held in the fortress of Königstein (Caroline [8]; plate)."),
    u(3, "NV, 2", "Der Buchstabe B", "The letter B",
      """Bach.
Bamberger, Schreiner.
Bapil, französis. Soldat.
Cerf Bär, Jude von Strasburg, Lieferant bey der Armee.
Bartholomä, getaufter Jude, Pompenmacher, Schuhflicker und Makler.
Beyer, Bendermeister.
Bayer, Silberschmidt an der Judengasse, dermalen Munizipal.
Beck, Schulmeister; pflanzte in seiner Schule den Freyheitsbaum mit den rothen Käppchen auf.
Becker, Schreiner.
Beringer, jun. Buchbinder.
Berlancour, verdorbener Krämer. Ausgetreten.""",
      """Bach.
Bamberger, joiner.
Bapil, French soldier.
Cerf Bär, Jew from Strasbourg, supplier to the army.
Bartholomä, baptized Jew, pump maker, cobbler and broker.
Beyer, master cooper.
Bayer, silversmith in the Jews' lane, now a municipal officer.
Beck, schoolmaster; set up the liberty tree with the red caps in his school.
Becker, joiner.
Beringer, jun., bookbinder.
Berlancour, ruined shopkeeper. Withdrawn.""",
      "Eine ganze Spalte, so wie sie gedruckt ist: Das sind die Klubisten, wie die Liste sie zeigt, Handwerker, Krämer, ein Lehrer, ein Soldat. Wo die Liste urteilt, urteilt sie nach Herkunft und Stand: „Jude“, „getaufter Jude“, „verdorbener Krämer“. „Ausgetreten“ heißt wohl: aus dem Klub ausgetreten. Der Schulmeister Beck mit dem Freiheitsbaum in der Schule gehört zu dem Streit um die Kinder, den Hoffmann aus dem Konvent überliefert (Konvent [17]).",
      "A whole column, just as it is printed: these are the Clubists as the list shows them, craftsmen, shopkeepers, a teacher, a soldier. Where the list judges, it judges by origin and station: 'Jew', 'baptized Jew', 'ruined shopkeeper'. 'Withdrawn' probably means: left the club. The schoolmaster Beck with the liberty tree in his school belongs to the dispute over the children that Hoffmann reports from the Convention (Konvent [17])."),
    u(4, "NV, 5", "Dorsch, Eikemeyer, Ekel", "Dorsch, Eikemeyer, Ekel",
      """Dorsch, ehemaliger Canonicus und Professor Philosophiæ zu Mainz hierauf Vicarius des Bischofs Brendel zu Strasburg, nachher lächerlicher Präsident bey der fränkischen Administration zu Mainz; er fand für gut, die schmachtende Mademoiselle Strohmayer von Mainz, dermalen ein Mittelding zwischen einer Frau und Mamsell, als Priester zu heyrathen.
[…]
Eikemeyer, als Landesverräther schon bekannt genug, um noch einer weiteren Schilderung zu bedürfen.
[…]
Ekel, Zinngießer, Präsident des sogenannten rheinischen Nationalkonvents.
[…]
Endlich, Stadthauptmann und ehemaliger Bedienter bey Herrn Großhofmeister Grafen von Stadion.""",
      """Dorsch, formerly canon and professor of philosophy at Mainz, then vicar of Bishop Brendel at Strasbourg, afterwards ridiculous president of the Frankish administration at Mainz; he saw fit, as a priest, to marry the languishing Mademoiselle Strohmayer of Mainz, now a middle thing between a wife and a maid.
[…]
Eikemeyer, already known well enough as a traitor to his country to need no further description.
[…]
Ekel, pewterer, president of the so-called Rhenish National Convention.
[…]
Endlich, town captain and formerly a servant of the Lord High Steward Count Stadion.""",
      "Anton Joseph Dorsch führte die Allgemeine Administration; Hoffmann zeigt ihn, wie er im November 1792 die Feder zum Einschreiben reicht (Forster [3]). Brendel war der konstitutionelle Bischof von Straßburg. Eickemeyer verhandelte im Oktober 1792 die Übergabe und ging dann zu den Franzosen über (Custine [11]). Eckel, nach Hoffmann achtzig Jahre alt, leitete die erste Sitzung des Konvents nur als Ältester; Präsident wurde Hofmann (Konvent [1]; Konvent [2]). Ein Graf Stadion tritt auch in Königs Roman auf (Nachleben [6]).",
      "Anton Joseph Dorsch headed the General Administration; Hoffmann shows him handing over the pen for signing in November 1792 (Forster [3]). Brendel was the constitutional bishop of Strasbourg. Eickemeyer negotiated the surrender in October 1792 and then went over to the French (Custine [11]). Eckel, eighty years old according to Hoffmann, chaired the first session of the Convention only as its eldest member; Hofmann became president (Konvent [1]; Konvent [2]). A Count Stadion also appears in König's novel (Nachleben [6])."),
    u(5, "NV, 6", "Forster", "Forster",
      """Forster, ehemaliger Bibliothekar der Universität-Bibliothek zu Mainz, zog eine starke Besoldung, ohne etwas dafür zu arbeiten, wurde hierauf Vicepräsident bey der fränkischen Administration, und dermalen Deputirter des weiland rheinischen Nationalkonvents zu Paris: er ist der Verfasser der Schrift über das Verhältniß der Mainzer gegen die Neufranken, worinn auf die frechste und ungezogenste Art gegen den König von Preußen geschimpft wird, der dem Vater u. den Anverwandten des Forsters Brod giebt.
[…]
Fuchs, ehemaliger Kopist, und Verräther der ihm anvertrauten Papiere.""",
      """Forster, formerly librarian of the University Library at Mainz, drew a large salary without doing any work for it, then became vice-president of the Frankish administration, and is now deputy of the late Rhenish National Convention at Paris: he is the author of the piece on the relation of the people of Mainz to the New Franks, in which the King of Prussia is abused in the most insolent and ill-mannered way, the King who gives bread to Forster's father and relatives.
[…]
Fuchs, formerly a copyist, and betrayer of the papers entrusted to him.""",
      "Die „Schrift über das Verhältniß der Mainzer gegen die Neufranken“ ist Forsters Rede vom 15. November 1792, die auf dieser Seite vollständig steht; dort heißt Preußen ein „blos durch Finanzoperationen“ erhobenes Königreich (Forster [17]). Forsters Vater Johann Reinhold Forster war Professor in Halle, also im Dienst des Königs von Preußen. „Weiland“, ehemalig: Der Konvent war mit dem Anschluss an Frankreich aufgegangen, Forster saß seit Ende März in Paris (Konvent [12]; Konvent [13]).",
      "The 'piece on the relation of the people of Mainz to the New Franks' is Forster's speech of 15 November 1792, printed in full on this site; there Prussia is called a kingdom raised 'merely by financial operations' (Forster [17]). Forster's father Johann Reinhold Forster was a professor at Halle, that is, in the service of the King of Prussia. 'Late', former: the Convention had been absorbed by the union with France, and Forster had been in Paris since the end of March (Konvent [12]; Konvent [13])."),
]

ROMAN = [
    u(6, "König I, 22–23", "„Thee mit Literatur“", "'Tea with literature'",
      """Wissen Sie aber, Cäcilie, wo er jetzt hingeht, wo er seine Abende zubringt, seit er aus Wien wieder zurück ist?
Fritz? —
Kapitular Stadion, dachte ich? Ja, der Graf. Bei Forsters, bei Frau Forster.
Frau Forster? Wer ist die Person?
Ei! des Hofraths Forster, des berühmten Weltumseglers, des Bibliothekars.
Ach, Frau Forster! lachte laut mit erzwungener Lustigkeit Cäcilie. Die liebe Frau Forster! Sie kennen sie also, — ist sie hübsch?
O, Sie fürchten zuviel, liebe Cäcilie! Das ist nicht, wie bei Ihnen. Das ist ein norddeutscher Umgang, das ist geistreicher Verkehr, das ist protestantische Geselligkeit, das ist Thee. Frau Forster ist die Tochter des göttinger Professors Heyne. Stadion hat in Göttingen studirt, il affiche le bel esprit. Nein, meine Gute, das ist eine gelehrte Sympathie, — Thee mit Literatur. Die wird Ihnen nicht schaden. Aber Sie sollten die geistreiche Frau kennen lernen!
Mein Gott — die Frau Forster! erwiderte mit verächtlichem Mäulchen die Baronesse. Und Sie, beste Gräfin, wie kommen Sie nur zu solchen Bekanntschaften?
Forster gibt meinem Edmund Unterricht in der Naturgeschichte, antwortete die Gräfin. Der Kurfürst wollte es so. Ich sehe den interessanten Mann öfter. Wahrhaftig, liebe Cäcilie, es ist ein recht anziehender Mann, ohne schön zu sein. Er hat etwas Apartes, — Auge und Teint des Weltumseglers, den Reiz, soll ich sagen den Hautgout ehemaligen Skorbuts. Ha, welch' ein Spaß, Cäcilie, wenn Sie, dem Stadion zum Possen, jenen interessanten Mann an sich zögen. Es ist ja guter Ton jetzt in Mainz mit Schriftstellern umzugehen. Der Kurfürst zieht das Volk heran, und der Coadjutor schreibt selbst. Ich glaube, dieser Dalberg schätzt die neue Philosophie höher, als seinen alten Adel. Wahrhaftig, liebe Cäcilie, Sie können diesem treulosen Freunde, der so gern den Geistreichen spielt, keinen bessern Schabernack anthun, als wenn Sie an seine Stelle einen berühmten Mann setzen, — einen Schriftsteller zum Anbeter nehmen.""",
      """But do you know, Cäcilie, where he goes now, where he spends his evenings, since he came back from Vienna?
Fritz? —
Capitular Stadion, I thought? Yes, the Count. At the Forsters', with Frau Forster.
Frau Forster? Who is the person?
Why! The wife of Privy Councillor Forster, the famous circumnavigator, the librarian.
Oh, Frau Forster! laughed Cäcilie aloud with forced merriment. Dear Frau Forster! So you know her, — is she pretty?
Oh, you fear too much, dear Cäcilie! It is not as with you. That is North German company, that is witty conversation, that is Protestant sociability, that is tea. Frau Forster is the daughter of Professor Heyne of Göttingen. Stadion studied at Göttingen, il affiche le bel esprit. No, my dear, that is a learned sympathy, — tea with literature. It will do you no harm. But you ought to get to know the witty woman!
Good heavens — Frau Forster! replied the baroness with a contemptuous little pout. And you, dearest Countess, how do you come by such acquaintances?
Forster gives my Edmund lessons in natural history, answered the Countess. The Elector wished it so. I see the interesting man quite often. Truly, dear Cäcilie, he is a very attractive man, without being handsome. He has something special about him, — the eye and complexion of the circumnavigator, the charm, shall I say the haut goût of former scurvy. Ha, what a joke, Cäcilie, if, to spite Stadion, you drew that interesting man to yourself. It is good form now in Mainz to keep company with writers. The Elector draws the people to him, and the Coadjutor writes himself. I believe this Dalberg values the new philosophy more highly than his old nobility. Truly, dear Cäcilie, you could play this faithless friend, who so likes to play the wit, no better trick than to put a famous man in his place, — to take a writer for an admirer.""",
      "So tritt Forster in den Roman ein: zuerst als Gerücht im Salon, durch die Augen des Hofadels. Frau von Coudenhove, die Gräfin, war die Vertraute des Kurfürsten Erthal; Therese Forster war tatsächlich die Tochter des Göttinger Philologen Christian Gottlob Heyne. Der Roman verbindet solche verbürgten Personen mit erfundenen wie der Baronesse Cäcilie. Der erste Teil spielt um 1790/91, Jahre vor der Besetzung; wenig später ziehen auf derselben Seite randalierende Handwerksgesellen durch die Straße. „Il affiche le bel esprit“: Er gibt sich als Schöngeist.",
      "This is how Forster enters the novel: first as salon gossip, seen through the eyes of the court nobility. Frau von Coudenhove, the Countess, was the confidante of the Elector Erthal; Therese Forster was indeed the daughter of the Göttingen philologist Christian Gottlob Heyne. The novel mixes such attested people with invented ones like the baroness Cäcilie. The first part is set around 1790/91, years before the occupation; a little later on the same page rioting journeymen march through the street. 'Il affiche le bel esprit': he poses as a man of wit."),
    u(7, "König I, 57", "Der Kurfürst und der Weltumsegler", "The Elector and the circumnavigator",
      """Zwischen den Musikstücken wurden Erfrischungen umher gereicht. Der Kurfürst unterhielt sich abwechselnd und trat auch zu Forstern. Sie haben einen kleinen Ausflug gemacht? fragte er.
Ja, Eure Durchlaucht, im August.
Mein Land, fuhr der Fürst fort, ist sehr klein für den Maßstab eines Weltumseglers; aber es liegt dafür etwas verzettelt. Die Dörfer und Häuser der protestantischen Einwohner werden Ihnen angenehm aufgefallen sein in dem von Ihnen bereisten Strich? Reden Sie nur offen! Sie kennen mich. Ich gestehe Ihnen, Herr Hofrath, daß ich — heißt das — ich als weltlicher Fürst — meine protestantischen Unterthanen vorziehe: sie sind fleißiger, reinlicher, treuer.
Welch' ein edles Anerkenntniß, kurfürstliche Gnaden! rief Forster aus. Eine große Gerechtigkeit des Herzens bei so weiser Einsicht!
Woher mag das kommen, Herr Forster? fragte der Fürst.
Vielleicht weil die Protestanten weniger von Kirchenwerken in Anspruch genommen sind, können sie mehr für das häusliche und bürgerliche Leben thun.
Ja. Oder weil wir ihnen die ewige Seligkeit absprechen, suchen sie sich auf der Erde besser einzurichten. Nicht wahr?
Der Kurfürst lachte laut hinter seinem Scherze her; wie er denn gegen Protestanten gern den Freidenker zeigte.""",
      """Between the pieces of music refreshments were handed round. The Elector conversed with one guest after another and came over to Forster too. You have made a little excursion? he asked.
Yes, Your Highness, in August.
My country, the prince went on, is very small by the measure of a circumnavigator; but to make up for it, it lies somewhat scattered. The villages and houses of the Protestant inhabitants will have struck you pleasantly in the stretch you travelled through? Speak quite openly! You know me. I confess to you, Herr Hofrat, that I — that is to say — I as a secular prince — prefer my Protestant subjects: they are more industrious, cleaner, more loyal.
What a noble acknowledgement, Your Electoral Grace! cried Forster. A great justice of the heart joined to such wise insight!
Where might that come from, Herr Forster? asked the prince.
Perhaps because the Protestants are less taken up with works of the church, they can do more for domestic and civic life.
Yes. Or because we deny them eternal salvation, they try to make themselves more comfortable on earth. Isn't that so?
The Elector laughed loudly after his own joke; for with Protestants he liked to show himself a freethinker.""",
      "Ein Hofkonzert im Schloss, mit dem Hofkapellmeister Righini und einer Arie aus „Armida“. König zeichnet Erthal als leutseligen, eitlen Aufklärer und Forster als höflichen Hofrat, der dem Fürsten schmeichelt. Das ist der Forster, dem Hoffmann später seine Zueignung an den Kurfürsten von 1789 vorhielt (Forster [2]).",
      "A court concert in the palace, with the court music director Righini and an aria from 'Armida'. König draws Erthal as an affable, vain man of the Enlightenment and Forster as a courteous Hofrat who flatters the prince. This is the Forster whom Hoffmann later reproached with his dedication to the Elector of 1789 (Forster [2])."),
    u(8, "König I, 58–59", "„Die zwei größten Despoten der Welt“", "'The two greatest despots in the world'",
      """Wie ich kurfürstliche Gnaden kenne, lächelte Forster, wird der Erzbischof von Mainz den Protestanten des Kurfürsten von Mainz auch jenseits etwas zu gut kommen lassen, für das, was sie diesseits leisten. Eure Durchlaucht kennen wol, aber lieben nicht die zwei größten Despoten der Welt.
Wer sind diese? fragte der Fürst lebhaft.
Das Alleinrechthaben und das Alleinseligmachen, antwortete Forster. Der Fürst will es, — also ist es recht; der Priester sagt es, — also ist es wahr! Beispiele sind überall auf der Erde. Braminendespotismus und päpstliche Alleingewalt haben Asien und Europa beinahe Jahrtausende in Dummheit und Elend versenkt gehalten. Vergebung, kurfürstliche Gnaden!
Während dieser kühnen Worte Forster's hatte der Kurfürst seine Bonbonniere wieder hervorgeholt, schüttelte etwas Zuckerwerk in die linke Hand und aus der Hand mit zurückgelegtem Kopf in den laut einschlürfenden Mund. Unter lebhaftem Kauen sagte er dann: Sehr wahr! Sie wissen ja, was ich mit den Emser Punktationen wider Rom gewollt habe.
Ewigen Dank dafür! rief Forster mit Wärme. Es wird wenigstens ein unvergeßliches Vorbild bleiben. Darum wollen wir nicht aufhören zu rufen: Freiheit! grenzenlose Freiheit in Allem, was über das Sinnenweltliche hinausgeht! Jeder wähle sich seinen Weg, ohne daß es auf seine politischen Verhältnisse Einfluß habe. Jeder glaube so wenig oder so viel, als er kann; Jeder sage frei und ohne Furcht, was er glaubt; Keiner erfreue sich blos der Duldung, sondern Jeder des anerkannten Rechtes zu denken, wie und was sein Wesen mit sich bringt.
Ob diese Aeußerung dem alten Herrn zu kühn oder nur zu laut gesprochen war: er wendete sich ab und suchte die Gräfin wieder auf.""",
      """As I know Your Electoral Grace, Forster smiled, the Archbishop of Mainz will let the Protestants of the Elector of Mainz have some credit in the hereafter too, for what they achieve here below. Your Highness knows well, but does not love, the two greatest despots in the world.
Who are they? asked the prince eagerly.
Being alone in the right and being alone in saving grace, answered Forster. The prince wills it, — so it is right; the priest says it, — so it is true! Examples are everywhere on earth. The despotism of the Brahmins and papal sole power have kept Asia and Europe sunk in stupidity and misery for almost thousands of years. Forgive me, Your Electoral Grace!
During these bold words of Forster's the Elector had taken out his bonbonnière again, shaken some sweets into his left hand and, head thrown back, from the hand into his loudly slurping mouth. Chewing vigorously, he then said: Very true! You know what I intended against Rome with the Punctation of Ems.
Eternal thanks for it! cried Forster warmly. It will at least remain an unforgettable example. Therefore we will not cease to cry: Freedom! boundless freedom in all that goes beyond the world of the senses! Let each choose his way without its having any influence on his political circumstances. Let each believe as little or as much as he can; let each say freely and without fear what he believes; let no one enjoy mere toleration, but each the acknowledged right to think how and what his nature brings with it.
Whether this utterance was too bold for the old gentleman or merely spoken too loudly: he turned away and sought out the Countess again.""",
      "Die „Emser Punktation“ von 1786 war der Versuch der vier deutschen Erzbischöfe, darunter Erthal, ihre Kirchen von Rom unabhängiger zu machen. Königs Forster ruft „Freiheit!“ schon 1790, aber nur für Glauben und Gewissen, nicht für den Staat: der Aufklärer vor dem Revolutionär. Ob König hier Sätze aus Forsters Schriften verarbeitet, ist für diese Ausgabe nicht nachgeprüft. Eben diese Behandlung meinte Klein: alle Schuld bei der Zeit und den Fürsten, Forster als edler Mann (Nachleben [12]).",
      "The 'Punctation of Ems' of 1786 was the attempt of the four German archbishops, Erthal among them, to make their churches more independent of Rome. König's Forster cries 'Freedom!' as early as 1790, but only for faith and conscience, not for the state: the man of the Enlightenment before the revolutionary. Whether König works sentences from Forster's writings in here has not been checked for this edition. It is precisely this treatment that Klein meant: all guilt laid on the times and the princes, Forster as a noble man (Nachleben [12])."),
]

KLEIN = [
    u(9, "Klein, V–VI", "„Fast 40 Jahre“", "'Almost forty years'",
      """Fast 40 Jahre lang nach Forster's Tod scheute man sich ihn zu nennen, Niemand getraute sich ihn zu loben, weil er des Verraths am Vaterland überführt war; daß er in Mainz zu den Franzosen überging, verzieh man ihm wie vielen Andern, besonders weil er sie für die Träger der Freiheit hielt; daß er die Revolution nach Deutschland verpflanzte, mochte man übersehen, wiewohl er mehrfach erklärte, daß die Deutschen noch nicht zur Freiheit reif seien; daß er aber einen ansehnlichen Theil Deutschlands, so viel an ihm lag, vom Vaterland abriß und dem Feinde einzuverleiben suchte, dies konnte man damals, dies kann man niemals ihm vergeben: auf ihm lastet somit das schwerste Verbrechen. Die Familie selbst stimmte während dieser Zeit in die Verurtheilung ein oder schwieg. Erst kurz vor der französischen Juli-Revolution (1829) veröffentlichte die Frau desselben seinen Briefwechsel, der ihn, wenn auch nicht freisprechen, doch entschuldigen oder Mitleid erregen sollte. Aber man nahm davon nicht Notiz. Doch als ein Romanschreiber den Forster zum Helden eines Romans gemacht hatte, da traten Biographen, Geschichtschreiber, Literarhistoriker u. s. w. in Menge auf, und suchten ihn zu vertheidigen; wollten doch sogar Einige ihn zum Vorbild den Deutschen hinstellen.""",
      """For almost forty years after Forster's death people shrank from naming him; no one dared to praise him, because he stood convicted of treason against the fatherland. That he went over to the French in Mainz was forgiven him, as it was forgiven many others, especially because he took them for the bearers of freedom; that he transplanted the revolution to Germany might be overlooked, although he declared several times that the Germans were not yet ripe for freedom; but that he tore a considerable part of Germany, as far as lay in his power, from the fatherland and sought to incorporate it into the enemy, this could not be forgiven him then, this can never be forgiven him: on him therefore lies the gravest crime. During this time his family itself joined in the condemnation or kept silent. Only shortly before the French July Revolution (1829) did his wife publish his correspondence, which was meant, if not to acquit him, then to excuse him or arouse pity. But no notice was taken of it. Yet when a novelist had made Forster the hero of a novel, biographers, historians, literary historians and so on came forward in crowds and tried to defend him; some even wanted to hold him up to the Germans as a model.""",
      "Karl Klein schrieb in Mainz, siebzig Jahre nach der Republik. Das „schwerste Verbrechen“ ist für ihn der Antrag auf Anschluss an Frankreich vom März 1793 (Konvent [11]). Die „Frau desselben“ ist Therese, inzwischen verwitwete Huber (Caroline [4]); ihre Ausgabe von Forsters Briefwechsel erschien 1829, ein Jahr vor der Julirevolution. Der „Romanschreiber“ ist Heinrich König ([12]).",
      "Karl Klein wrote in Mainz, seventy years after the Republic. The 'gravest crime' for him is the request for union with France of March 1793 (Konvent [11]). 'His wife' is Therese, by then the widowed Huber (Caroline [4]); her edition of Forster's correspondence appeared in 1829, a year before the July Revolution. The 'novelist' is Heinrich König ([12])."),
    u(10, "Klein, VI–VII", "Ein Denkmal für Forster?", "A monument to Forster?",
      """So wurde von Moleschott im Jahre 1854 den Mainzern die Zumuthung gestellt: „dem Forster dahier ein Denkmal zu errichten.“ Sie wiesen es mit Indignation zurück.
Als ich vor zwei Jahren die „Geschichte von Mainz während der ersten französischen Occupation 1792 — 93“ schrieb, worin des Forster's hiesiges Treiben kurz, aber der Wahrheit gemäß, geschildert wurde: stutzten Manche über das bisherige Lob Forster's und über seine Lobredner.
Doch die Verherrlichung desselben nahm noch kein Ende. Derselbe Moleschott hatte am 18. Oktober v. J., als in Mainz die Schiller-Statue enthüllt wurde, die Kühnheit, die Mainzer öffentlich zu einem Denkmal für Forster aufzufordern. — Er wurde wieder zurückgewiesen.
Es dürfte daher an der Zeit sein, Forster's letzte Lebensjahre ausführlich darzustellen. Und so unternahm ich es, die Zeit, welche er in Mainz zubrachte, einer genauen Schilderung zu unterbreiten; woraus sich ergeben wird, daß Forster — wenigstens in den letzten vier Jahren — den edelen Sinn nicht besaß, den Manche in ihm fortwährend fanden. Daß er aber im letzten Jahre die schwerste Schuld auf sich lud, dieses wird vorliegendes Werk neu bekräftigen, auf daß Niemand in Deutschland einen Mann feiere, der sich so schwer am Vaterland versündigte.""",
      """Thus in the year 1854 Moleschott put to the people of Mainz the presumptuous demand 'to erect a monument to Forster here'. They rejected it with indignation.
When two years ago I wrote the 'History of Mainz during the First French Occupation 1792–93', in which Forster's doings here were described briefly but truthfully, many were taken aback at the praise hitherto given to Forster and at his eulogists.
But the glorification of him did not yet come to an end. On 18 October of last year, when the Schiller statue was unveiled in Mainz, the same Moleschott had the audacity publicly to call on the people of Mainz to erect a monument to Forster. — He was rejected again.
It may therefore be time to set out Forster's last years in detail. And so I undertook to submit the time he spent in Mainz to an exact description; from which it will emerge that Forster — at least in the last four years — did not possess the noble mind that many kept finding in him. But that in the last year he took the gravest guilt upon himself, this the present work will confirm anew, so that no one in Germany may celebrate a man who sinned so gravely against the fatherland.""",
      "Jacob Moleschott, Physiologe und Materialist, hatte 1854 ein Buch über Forster als „Naturforscher des Volks“ veröffentlicht (Tafel). In einer Fußnote nennt Klein seine Gegenschriften: eine „Zurückweisung der Tischrede Moleschott's“ (1862) und zwei Drucke von 1863 gegen einen anonymen Verteidiger Forsters in der Hessischen Landes-Zeitung. „Vorliegendes Werk“: Klein druckt im Hauptteil Akten aus der Mainzer Zeit ab; hier stehen nur Vorwort und Einleitung.",
      "Jacob Moleschott, physiologist and materialist, had published a book in 1854 on Forster as 'naturalist of the people' (plate). In a footnote Klein lists his own counter-pieces: a 'Rejection of Moleschott's Table Speech' (1862) and two prints of 1863 against an anonymous defender of Forster in the Hessische Landes-Zeitung. 'The present work': in the main part Klein prints documents from the Mainz period; only the preface and introduction are given here."),
    u(11, "Klein, VII–VIII", "„Es thut noth zu sichten“", "'There is need to sift'",
      """Von dieser ganzen Schrift hat mich der Gedanke oft abschrecken wollen, daß Viele nicht löblich finden mögen, wenn man den Namen eines Todten in böses Licht zu stellen versucht. Da fiel mir aber ein, daß dieses nicht der Zweck der Schrift ist, sondern sie will das Urtheil, das 40 Jahre galt, erneuen und bestärken und soll auftreten gegen die frevelhafte Gesinnung Vieler, welche sogar zum Vorbild der Deutschen einen Mann hinstellen wollen, der einen großen Theil des deutschen Landes an unsern Erbfeind abtrat. Ich meine, es thut noth zu sichten; und jetzt ist die Zeit da, in welcher ein Buch von Allen, die das Vaterland lieben, mit Freuden begrüßt werden sollte, weil es sich zum Ziel setzt, klar und aktenmäßig und unwiderleglich zu beweisen, daß alle jene, welche den Forster vertheidigen oder feiern, entweder in Unwissenheit sind oder eine verwerfliche Gesinnung kundgeben.
Möge dies Buch also beitragen, die Wahrheit über Forster festzustellen und möge es mithelfen die deutsche Gesinnung in unserem Vaterland zu erhöhen, um alle jene auszustoßen, welche mit dem Feinde liebäugeln oder zu ihm übergehen.
Mainz, 30. Juni 1863.
Klein.""",
      """From this whole work I was often nearly deterred by the thought that many may not find it praiseworthy when one tries to put the name of a dead man in a bad light. But then it occurred to me that this is not the purpose of the work; rather, it means to renew and strengthen the judgement that held for forty years, and to stand up against the wicked disposition of many who even want to hold up as a model for the Germans a man who ceded a great part of the German land to our hereditary enemy. I think there is need to sift; and now the time has come in which a book ought to be welcomed with joy by all who love the fatherland, because it sets itself the goal of proving clearly, from the documents and irrefutably, that all those who defend or celebrate Forster are either in ignorance or reveal a reprehensible disposition.
May this book therefore help to establish the truth about Forster, and may it help to raise German sentiment in our fatherland, in order to cast out all those who make eyes at the enemy or go over to him.
Mainz, 30 June 1863.
Klein.""",
      "Der Schluss des Vorworts. „Erbfeind“ ist Frankreich. Das Vorwort ist auf den 30. Juni 1863 datiert, auf den Tag siebzig Jahre nach dem 30. Juni 1793, mitten in der Beschießung (Belagerung [9]). Klein will nicht abwägen, sondern ein Urteil „erneuen“; die Akten, die er abdruckt, sind trotzdem für jeden Leser brauchbar, der anders urteilt.",
      "The end of the preface. The 'hereditary enemy' is France. The preface is dated 30 June 1863, seventy years to the day after 30 June 1793, in the middle of the bombardment (Belagerung [9]). Klein does not want to weigh, but to 'renew' a verdict; the documents he prints are nonetheless usable by any reader who judges otherwise."),
    u(12, "Klein, 22–23", "Der Roman und der Geist in Hanau", "The novel and the ghost in Hanau",
      """Doch auch Gervinus Sammlung hat den Forster nicht populär gemacht: einige seiner Werke sind veraltet, andere setzen einen Grad von Bildung voraus, der sich gerade bei den gewöhnlichen Lesern selten findet. Die Charakteristik und Vertheidigung übersah man.
Da mußte ein Romanschreiber auftreten, — was für Deutschland bezeichnend ist — um den Forster bei denen, die nichts von ihm wußten, bekannt zu machen, bei denen, die ihn kannten, zu vertheidigen. Heinrich König's Klubisten in Mainz haben ihrer Zeit ein bedeutendes Aufsehen erregt und finden noch immer ihre Leser und Zustimmer. In ihnen ist von den Personen, welche damals wirklich lebten, die Hauptperson unser Forster. Der Verfasser entschuldigt zwar die Handlungen Forster's, die nie entschuldigt werden können, nicht, allein die ganze Behandlung des Romans ist von der Art, daß alles, was gefehlt wird, der damaligen Zeit und den Fürsten Deutschlands zugeschrieben wird, so daß die einzelnen Privatpersonen, oft Hauptleiter im klubistischen Mainz, beim schnellen Lesen — wie es in Romanen der Fall ist — übersehen werden, oder gar gerechtfertigt erscheinen; Forster aber ist in vieler Hinsicht falsch aufgefaßt. Doch war er von jetzt an bekannt, ja er wurde beliebt und die Folge war, daß man sein Vergehen, wenn auch noch nicht vertheidigte, doch übersah oder nicht mehr berührte.
Doch zur vollen Erkenntniß kann ein Roman nicht führen. Forster war „nur halb erkennbar;“ da erschien, „um sich von dieser Halbheit zu erlösen,“ Forster selbst (Nov. 1851) dem eben erwähnten Heinrich König in Hanau und bat ihn, „wie er ihn zur Fabel gemacht habe, so ihn zum Vorbild zu vollenden.“ Und der erfreute Geisterseher versuchte es. Er schrieb „Haus und Welt; eine Lebensgeschichte.“ […] Auf keinen Fall will König ihn als „Vorbild“ hinstellen und somit hatte er die Bitte von Forster's Geist nicht erfüllt noch erfüllen können.""",
      """But Gervinus's collection did not make Forster popular either: some of his works are out of date, others presuppose a degree of education that is seldom found precisely among ordinary readers. The characterization and defence were overlooked.
Then a novelist had to come forward — which is characteristic of Germany — to make Forster known among those who knew nothing of him and to defend him among those who knew him. Heinrich König's 'Clubists in Mainz' caused a considerable stir in their day and still find their readers and supporters. In it, of the persons who really lived at the time, the chief character is our Forster. The author does not, it is true, excuse Forster's actions, which can never be excused; but the whole treatment of the novel is such that everything that goes wrong is ascribed to the times and to the princes of Germany, so that the individual private persons, often chief leaders in Clubist Mainz, are overlooked in quick reading — as is the way with novels — or even appear justified; Forster, however, is in many respects wrongly conceived. Yet from now on he was known, indeed he became popular, and the consequence was that his offence, if not yet defended, was overlooked or no longer touched upon.
But a novel cannot lead to full knowledge. Forster was 'only half recognizable'; then, 'to release himself from this halfness', Forster himself appeared (Nov. 1851) to the aforementioned Heinrich König in Hanau and asked him, 'as he had made him into a fable, so to complete him as a model'. And the delighted ghost-seer tried. He wrote 'House and World; a Life Story'. […] In no case does König want to present him as a 'model', and so he had not fulfilled, nor could he fulfil, the request of Forster's ghost.""",
      "Gervinus schrieb die „Charakteristik“ für die Sämmtlichen Schriften von 1843, nach denen diese Seite Forsters Rede und die „Darstellung“ abdruckt (Darstellung [1]). In einer Fußnote gibt Klein den Roman als „Leipzig bei Brockhaus 1847 drei Bände“ an und „Haus und Welt“ als „Zwei Theile, Braunschweig 1852“. Die Erscheinung in Hanau zitiert Klein aus dem Vorwort von „Haus und Welt“; wie König sie dort meinte, ob als Erzählspiel oder anders, ist hier nicht nachgeprüft. Kleins Spott über den „Geisterseher“ ist sein eigener.",
      "Gervinus wrote the 'Characterization' for the collected writings of 1843, from which this site prints Forster's speech and the 'Account' (Darstellung [1]). In a footnote Klein gives the novel as 'Leipzig, Brockhaus 1847, three volumes' and 'Haus und Welt' as 'two parts, Brunswick 1852'. Klein quotes the apparition in Hanau from the preface of 'Haus und Welt'; how König meant it there, as a narrative game or otherwise, has not been checked here. Klein's mockery of the 'ghost-seer' is his own."),
]

SECS = [
    ("pranger", "Der Pranger: das Namensverzeichnis (Juni 1793)", "The pillory: the list of names (June 1793)", PRANGER,
     "Während der Belagerung druckt man in Frankfurt eine Liste der „454 Klubbisten“, die sich in Mainz befinden, mit Beruf und, bei manchen, einem Urteil über ihren „Charakter“. Auch Forster steht darin.",
     "During the siege a list of the '454 Clubists' to be found in Mainz is printed in Frankfurt, with trades and, for some, a verdict on their 'character'. Forster is in it too."),
    ("roman", "Der Roman: Heinrich König, „Die Clubisten in Mainz“ (1847)", "The novel: Heinrich König, 'The Clubists in Mainz' (1847)", ROMAN,
     "Im Vormärz macht Heinrich König Forster zur Hauptfigur eines dreibändigen Romans. Der erste Teil zeigt ihn vor der Revolution, am Hof des Kurfürsten Erthal.",
     "On the eve of 1848 Heinrich König makes Forster the main character of a three-volume novel. The first part shows him before the revolution, at the court of the Elector Erthal."),
    ("klein", "Die Anklage: Karl Klein, „Georg Forster in Mainz“ (1863)", "The indictment: Karl Klein, 'Georg Forster in Mainz' (1863)", KLEIN,
     "Ein Mainzer Historiker antwortet auf Roman, Biographien und Denkmalspläne: Forster habe sich „so schwer am Vaterland versündigt“, dass niemand ihn feiern dürfe.",
     "A Mainz historian answers the novel, the biographies and the plans for a monument: Forster had 'sinned so gravely against the fatherland' that no one should celebrate him."),
]

DATA = {
    "titel": "Nachleben: Pranger, Roman und Anklage (1793–1863)",
    "titel_en": "Afterlife: pillory, novel and indictment (1793–1863)",
    "autor": "Anonymer Frankfurter Druck (1793); Heinrich Koenig (1847); Karl Klein (1863)",
    "autor_en": "Anonymous Frankfurt print (1793); Heinrich Koenig (1847); Karl Klein (1863)",
    "jahr": "1793–1863",
    "sprache": "de",
    "orig_sprache": "de",
    "pg_label": "",
    "quelle": "Getreues Namensverzeichniß der in Mainz sich befindenden 454 Klubbisten, mit Bemerkung derselben Charakter (Frankfurt 1793), Titel, S. 2, 5, 6 (Internet Archive, bub_gb_lNZBAAAAcAAJ, Exemplar der Bayerischen Staatsbibliothek). Heinrich Koenig, Die Clubisten in Mainz. Ein Roman, Erster Theil (Leipzig: Brockhaus 1847), S. 22–23, 57–59 (Internet Archive, 11750809bsb). K. Klein, Georg Forster in Mainz 1788 bis 1793, nebst Nachträgen zu seinen Werken (Gotha: Perthes 1863), S. V–VIII, 22–23 (Internet Archive, bub_gb_2_o5AAAAcAAJ).",
    "hinweis": "Drei Arten, wie die Mainzer Republik weiterlebte: als Pranger noch während der Belagerung, als Roman im Vormärz, als Anklage siebzig Jahre danach. Alle drei Texte sind parteiisch, jeder auf seine Weise; sie stehen hier, weil sie zeigen, wie über Forster und die Klubisten gesprochen wurde, nicht als Auskunft darüber, wie es war. Die Seitenangaben nennen „NV“ für das Namensverzeichnis, „König I“ für den ersten Teil des Romans und „Klein“ für das Buch von 1863. Alle Texte am Seitenbild gelesen; Schreibung und Zeichensetzung wie gedruckt, ſ als s, Silbentrennung aufgelöst, Sperrungen nicht wiedergegeben, Auslassungen mit […] bezeichnet. Die englische Übersetzung ist eine eigene Arbeitsübersetzung (CC0).",
    "hinweis_en": "Three ways in which the Mainz Republic lived on: as a pillory while the siege was still going on, as a novel before 1848, as an indictment seventy years later. All three texts are partisan, each in its own way; they stand here because they show how people spoke about Forster and the Clubists, not as information about how things were. Page references give 'NV' for the list of names, 'König I' for the first part of the novel and 'Klein' for the book of 1863. All texts read against the page images; spelling and punctuation as printed, long s as s, hyphenation resolved, letter-spacing not reproduced, omissions marked […]. The English translation is my own working translation (CC0).",
    "sections": [{"id": i, "titel": t, "titel_en": te, "zk": "Nachleben", "blurb": b, "blurb_en": be, "units": us}
                 for i, t, te, us, b, be in SECS],
}

if __name__ == "__main__":
    ns = [x["n"] for s in DATA["sections"] for x in s["units"]]
    assert ns == list(range(1, len(ns) + 1)), ns
    OUT.write_text(json.dumps(DATA, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("ok", OUT.name, len(ns), "units")
