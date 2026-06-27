# -*- coding: utf-8 -*-
"""
Einzige Inhaltsquelle für Plattform + PDFs.
Sprachvergleich Deutsch–Türkisch · DaZ · Dr. Ergun Özsoy, LMU München (ALM 260).
Konvention: türkische Tokens stehen in <span class="trk"> (kursiv, eigene Farbe),
deutsche/neutrale Beispiele in <span class="ex">. Quellen ausschließlich auf der
Literatur-Seite – im Inhalt keine Zitate/Quellenkürzel.
"""

BLOCKNAMES = ["Kontrastiver Befund","Didaktik & DaZ-Relevanz","Interferenzanalyse",
              "Korrektur & Förderung","Interkulturalität & Mehrsprachigkeit als Ressource"]

# Strukturbaum (Reihenfolge = Navigation). status: "ready" | "draft"
MODULES = [
 {"id":"m1","name":"Modul I · Laut & Schrift","topics":[
   {"id":"alphabet","t":"Alphabet & Aussprache","s":"ready","desc":"DE: ein Buchstabe – mehrere Laute; TR: weitgehend 1:1."},
   {"id":"auslaut","t":"Auslautverhärtung","s":"ready","desc":"Finale Entstimmung – gleicher Laut, andere Schreibregel."},
   {"id":"sprossv","t":"Konsonantenhäufung & Sprossvokal","s":"ready","desc":"Vokaleinschub als L1-Phonotaktik."},
   {"id":"graphem","t":"Graphem-Kontraste (v/w · z/s · c/ç · ı/i)","s":"ready","desc":"Gleiche Buchstaben, andere Lautwerte."},
   {"id":"vokalh","t":"Vokalharmonie & Umlaut","s":"ready","desc":"TR-Vokalharmonie vs. DE-Umlaut als Morphemsignal."},
 ]},
 {"id":"m2","name":"Modul II · Morphologie","topics":[
   {"id":"genus","t":"Nomen: Genus & Artikel","s":"ready","desc":"der/die/das & Bestimmtheit – TR ohne Genus/Artikel."},
   {"id":"plural","t":"Nomen: Plural & Kasus","s":"ready","desc":"Pluraltypen vs. -lAr; 4 vs. 6 Kasus."},
   {"id":"pronomen","t":"Pronomen","s":"ready","desc":"Flexion vs. Possessivsuffix; Pro-Drop."},
   {"id":"kompar","t":"Komparation (Adjektive)","s":"ready","desc":"-er/am -sten vs. daha/en; „als“ über Ablativ."},
   {"id":"verben","t":"Verben","s":"ready","desc":"Trennbarkeit & Verbklammer vs. Suffixkette."},
   {"id":"zeit","t":"Zeitformen","s":"ready","desc":"Tempussystem & Evidentialität."},
   {"id":"imperativ","t":"Imperativ","s":"ready","desc":"du/ihr/Sie vs. reichere TR-Höflichkeit."},
   {"id":"konjunktiv","t":"Konjunktiv","s":"ready","desc":"K I/K II vs. Konditional -se/-sa."},
   {"id":"passiv","t":"Passiv","s":"ready","desc":"werden-Passiv vs. Suffix -Il-/-In-."},
   {"id":"praep","t":"Präpositionen vs. Kasussuffixe","s":"ready","desc":"DE-Präposition+Kasus ↔ TR-Suffix."},
   {"id":"adverb","t":"Adverbien","s":"ready","desc":"Adjektiv=Adverb; TeKaMoLo-Stellung."},
 ]},
 {"id":"m3","name":"Modul III · Syntax","topics":[
   {"id":"satzart","t":"Satzarten","s":"ready","desc":"Verbstellung vs. Fragepartikel mi."},
   {"id":"wortstell","t":"Wortstellung (SOV vs. V2)","s":"ready","desc":"TR verbfinal vs. DE Verbzweit/Klammer."},
   {"id":"relativ","t":"Relativsatz","s":"ready","desc":"DE-Relativpronomen vs. TR-Partizipialattribut."},
 ]},
]

# Hilfsfunktionen -----------------------------------------------------------
def k(s):  # türkisches Token (kursiv, eigene Farbe)
    return f'<span class="trk">{s}</span>'
def d(s):  # deutsches/neutrales Beispiel-Token
    return f'<span class="ex">{s}</span>'

def T(rows, head=("Merkmal","Deutsch","Türkisch")):
    h="".join(f"<th>{x}</th>" for x in head)
    body=""
    for r in rows:
        body+=f'<tr><td>{r[0]}</td><td class="de">{r[1]}</td><td class="tr">{r[2]}</td></tr>'
    return f"<table><tr>{h}</tr>{body}</table>"

def ITAB(rows):  # (lernerform, zielform, ursache, typ) ; typ: 'interlingual'|'intralingual'
    body=""
    for f,z,u,typ in rows:
        cls="il" if typ=="interlingual" else "al"
        body+=(f'<tr><td><span class="err">{f}</span></td>'
               f'<td><span class="ok">{z}</span></td><td>{u}</td>'
               f'<td><span class="tag typ {cls}">{typ}</span></td></tr>')
    return ('<table><tr><th>Lernerform</th><th>Zielform</th><th>Ursache</th>'
            f'<th>Typ</th></tr>{body}</table>')

def NOTE(s): return f'<p class="note">{s}</p>'
def P(s): return f"<p>{s}</p>"

# === DETAIL: 5 Blöcke je Thema ============================================
DETAIL = {}

DETAIL["alphabet"]=dict(
 modul="Modul I · Laut & Schrift", titel="Alphabet & Aussprache",
 lead="Das Türkische ist nahezu lautgetreu (ein Buchstabe ≈ ein Laut). Das Deutsche ist es nicht – derselbe Buchstabe kann mehrere Laute tragen. Genau diese Mehrdeutigkeit muss explizit gemacht werden.",
 blocks=[
  T([("Schrift-Laut-Bezug","ein Graphem → oft mehrere Laute","weitgehend 1 Graphem = 1 Laut"),
     ("Sonderzeichen","ä ö ü ß",f"{k('ç ş ğ ı')} (kein ß, kein q/w/x)"),
     ("Beispiele",f"{d('v')}=[f], {d('w')}=[v], {d('z')}=[ts], {d('ch')}=[x]/[ç], {d('ei')}=[aɪ]",
      f"{k('c')}=[dʒ], {k('ç')}=[tʃ], {k('ş')}=[ʃ], {k('j')}=[ʒ]")])
  +NOTE("Kernpunkt: TR-Lernende erwarten Lautgetreue – die deutschen Sonderfälle wirken wie „Ausnahmen“ und müssen als geschlossene Liste vermittelt werden."),
  P("Aussprache <i>und</i> Lesetechnik sind betroffen: Wer ⟨v, w, z, ch, ei, eu⟩ lautgetreu liest, verliest sich systematisch. Früh im DaZ-/Alphabetisierungsprozess zu sichern."),
  ITAB([("[ˈvaːtɐ] für Vater","[ˈfaːtɐ]",f"{k('v')} im Türkischen = [v]","interlingual"),
        ("[zaɪt] für Zeit","[tsaɪt]",f"{k('z')} im Türkischen = [z]","interlingual"),
        ("[ˈwasɐ] für Wasser","[ˈvasɐ]",f"{k('w')} im Türkischen = [v]","interlingual")]),
  P("Laut-Buchstaben-Tabelle der Abweichungen; <b>Minimalpaare</b> (Vater/Wasser, Zeit/seit); Lautgebärden; lautes Lesen mit markierten Sonderfällen ⟨v w z s sch ch ei eu äu st sp⟩."),
  P("Die lautgetreue türkische Orthographie ist ein <b>Lesevorsprung</b> – das Prinzip „Buchstabe→Laut“ beherrschen die Lernenden bereits. Aufgabe: nur die deutschen Abweichungen ergänzen, nicht das Lesen neu lernen."),
 ])

DETAIL["auslaut"]=dict(
 modul="Modul I · Laut & Schrift", titel="Auslautverhärtung",
 lead="Beide Sprachen entstimmen Plosive am Wortende – aber sie verschriften das Ergebnis unterschiedlich. Genau dort entsteht ein orthographischer Interferenzfehler.",
 blocks=[
  T([("Phonolog. Prozess",f"Entstimmung der Obstruenten {d('/b d g/→[p t k]')}",f"Entstimmung der Plosive {k('/b d c g/→[p t ç k]')}"),
     ("gesprochen",f"{d('Tag')} [taːk], {d('Hund')} [hʊnt], {d('lieb')} [liːp]",f"{k('kitap')} [kitap], {k('renk')} [reŋk]"),
     ("Verschriftung",f"<b>morphophonemisch</b>: Graphem bleibt ({d('Tag·e')})",f"<b>oberflächenphonemisch</b>: man schreibt das Gehörte ({k('kitap')}, aber {k('kitabı')})")])
  +NOTE("Kernpunkt: Den <i>Laut</i> kennen TR-Lernende bereits – nur die <i>Schreibkonvention</i> ist neu."),
  P("Doppelt relevant: für die <b>Rechtschreibung</b> (richtiges Endgraphem) und das <b>Leseverstehen</b> (Wortverwandtschaften: "+d("Tag–täglich–Tage")+"). Eine früh zu sichernde Rechtschreibstrategie."),
  ITAB([("Hunt","Hund","türkische Schreibung folgt der Aussprache","interlingual"),
        ("Tak","Tag","finale Entstimmung wird verschriftet","interlingual"),
        ("lip","lieb","L1-Schreibkonvention auf L2 übertragen","interlingual")]),
  P("<b>Verlängerungsprobe.</b> Das Wort verlängern, bis der Auslaut stimmhaft in die nächste Silbe rückt:")
  +"<ul class='li'><li>"+d("Hund → Hun<b>d</b>e")+" → <span class='ok'>d</span></li><li>"+d("Tag → Ta<b>g</b>e")+" → <span class='ok'>g</span></li><li>"+d("lieb → lie<b>b</b>er")+" → <span class='ok'>b</span></li></ul>"
  +P("Parallele zum Türkischen explizit machen: "+k("kitap–kitabı")+" zeigt denselben Wechsel – nur dort wird er <i>geschrieben</i>."),
  P("Die L1 ist hier ein <b>Vorsprung</b>: Die finale Entstimmung existiert im Türkischen bereits ("+k("kitap/kitabı, renk/rengi")+"). Reframing: nicht „ein neuer Laut“, sondern „eine andere <i>Schreibregel</i> für denselben Laut“."),
 ])

DETAIL["sprossv"]=dict(
 modul="Modul I · Laut & Schrift", titel="Konsonantenhäufung & Sprossvokal",
 lead="Das Deutsche erlaubt komplexe Konsonantencluster, das Türkische meidet sie – besonders am Wortanfang. Lernende fügen einen Sprossvokal (Epenthese) ein.",
 blocks=[
  T([("Silbenstruktur",f"komplexe Cluster erlaubt: {d('Strumpf, Herbst, Sprung')}","Anfangscluster gemieden; CV-Präferenz"),
     ("Strategie bei Clustern","–",f"<b>Sprossvokal</b>/Epenthese: {k('tren→tiren, spor→sıpor')}")])
  +NOTE("Die türkische Phonotaktik ist nicht „falsch“, sondern systematisch – sie bricht Cluster durch Vokaleinschub auf."),
  P("Betrifft <b>Aussprache und Schreibung</b> gleichermaßen. Cluster-Wahrnehmung und -Produktion brauchen gezieltes Training (An- und Auslaut)."),
  ITAB([(k('sıport')+" für Sport","Sport","Vokaleinschub vor /sp/ (L1-Phonotaktik)","interlingual"),
        (k('kıraft'),"Kraft","Aufbrechen von /kr/ durch Sprossvokal","interlingual"),
        ("Herbst → Herbs","Herbst","Auslaut-Cluster vereinfacht","intralingual")]),
  P("Silbensegmentierung, langsames Sprechen mit allmählicher Verdichtung, <b>Cluster-Minimalpaare</b> (Stadt/Satt), Sprech-Schreib-Kopplung."),
  P("Den Lernenden bewusst machen: Der Sprossvokal ist eine <i>Regel der L1</i>, kein Defizit. Sichtbar gemachte Kontraste (türkische Silbe vs. deutsches Cluster) entlasten und erklären den eigenen „Akzent“."),
 ])

DETAIL["graphem"]=dict(
 modul="Modul I · Laut & Schrift", titel="Graphem-Kontraste (v/w · z/s · c/ç · ı/i)",
 lead="Viele Buchstaben existieren in beiden Alphabeten – tragen aber andere Lautwerte. Das ist eine besonders zähe, oft unbewusste Interferenzquelle.",
 blocks=[
  T([("⟨v⟩",f"[f] – {d('Vater')}",f"[v] – {k('ev')}"),
     ("⟨w⟩",f"[v] – {d('Wasser')}","existiert nicht"),
     ("⟨z⟩",f"[ts] – {d('Zeit')}",f"[z] – {k('zaman')}"),
     ("⟨c⟩ / ⟨ç⟩","[k]/[ts] (Fremdw.)",f"[dʒ] / [tʃ] – {k('cam / çay')}"),
     ("⟨ı⟩ vs ⟨i⟩","kein ⟨ı⟩; ⟨i⟩=[ɪ]/[iː]",f"[ɯ] vs [i] – {k('kız / kiz')}")],
    head=("Graphem","Deutsch","Türkisch")),
  P("Weil die Buchstaben <i>vertraut</i> aussehen, wird der falsche Lautwert oft unbemerkt übertragen – beim Lesen wie beim Schreiben."),
  ITAB([("[v]ater","[f]ater",f"{k('v')} im Türkischen = [v]","interlingual"),
        ("[z]eit","[ts]eit",f"{k('z')} im Türkischen = [z]","interlingual"),
        ("⟨w⟩ als [w]","[v]","⟨w⟩ existiert im Türkischen nicht","interlingual")]),
  P("Graphem-Phonem-Kontrasttabelle; <b>farbige Markierung</b> der „falschen Freunde“; Minimalpaare (Vater/Wasser, Zeit/seit); Diktat mit Fokus auf ⟨v w z⟩."),
  P("Leitidee bewusst machen: <b>Ein Buchstabe hat keinen universellen Lautwert.</b> Die türkischen Werte sind nicht falsch – sie gelten nur in der L1. Sprachvergleich macht das System sichtbar."),
 ])

DETAIL["vokalh"]=dict(
 modul="Modul I · Laut & Schrift", titel="Vokalharmonie & Umlaut",
 lead="Im Türkischen richten sich Suffixvokale nach dem Stamm (Vokalharmonie). Im Deutschen signalisiert der Umlaut Morphologie (Plural, Komparativ, Diminutiv). Zwei ganz verschiedene Prinzipien.",
 blocks=[
  T([("Phänomen",f"<b>Umlaut</b> a→ä, o→ö, u→ü – morphologisch","<b>Vokalharmonie</b> – phonologisch"),
     ("Beispiel",f"{d('Vater→Väter, alt→älter')}",f"{k('ev-ler / kitap-lar')} (e/a; i/ı/ü/u)"),
     ("ö/ü","Phoneme vorhanden",f"Phoneme vorhanden ({k('göz, gül')})")]),
  P("Doppelter Befund: ö/ü existieren im Türkischen – ein <b>Aussprachevorsprung</b>. Der Umlaut dagegen ist im Deutschen ein <i>Bedeutungssignal</i> (Plural/Komparativ) und muss als solches gelernt werden."),
  ITAB([("die Mutter (Pl.)","die Mütter","Umlaut als Pluralsignal nicht erkannt","intralingual"),
        ("alter (Komp.)","älter","Umlaut beim Komparativ fehlt","intralingual"),
        ("Umlautpunkte weggelassen","ä / ö / ü","Diakritikum als unwichtig behandelt","intralingual")]),
  P("Umlaut als <b>Bedeutungsträger</b> sichtbar machen (Tochter→Töchter, lang→länger); Umlautschreibung sichern; ö/ü-Aussprache aus dem Türkischen positiv nutzen."),
  P("Mehrsprachigkeit als Ressource doppelt: türkische ö/ü erleichtern die Aussprache; und der Kontrast „Harmonie (phonologisch) vs. Umlaut (morphologisch)“ schärft das grammatische Bewusstsein."),
 ])

DETAIL["genus"]=dict(
 modul="Modul II · Morphologie (Nomen)", titel="Genus & Artikel",
 lead="Das Deutsche markiert Genus (der/die/das) und Bestimmtheit am Artikel – das Türkische kennt weder grammatisches Genus noch Artikel. Eine der hartnäckigsten DaZ-Fehlerquellen.",
 blocks=[
  T([("Genus",f"3 Genera, lexikalisch fest: {d('der Tisch, die Lampe, das Buch')}",f"kein Genus – ein Wort: {k('o')}"),
     ("best. Artikel",f"{d('der/die/das')}",f"keiner; Bestimmtheit über <b>Akkusativ</b> ({k('-i')}) & Wortstellung"),
     ("unbest. Artikel",f"{d('ein/eine/ein')}",f"optional {k('bir')}"),
     ("Bestimmtheit am Objekt",f"{d('Ich lese das Buch')}",f"{k('Kitabı okuyorum')} (Akk. markiert das bestimmte Objekt)")])
  +NOTE("Funktional ist Bestimmtheit in <i>beiden</i> Sprachen da – nur die Kodierung unterscheidet sich: Artikel (DE) vs. Kasus/Wortstellung (TR)."),
  P("Genus ist nicht ableitbar und muss <b>mit jedem Nomen mitgelernt</b> werden (Nomen + Artikel als Einheit). Da die L1 die Kategorie nicht besitzt, bleiben Genus-/Artikelfehler oft lange bestehen – ein <b>diagnostischer Dauerbrenner</b>."),
  ITAB([("Ich sehe Mann.","Ich sehe einen Mann.","kein obligatorischer Artikel in der L1","interlingual"),
        ("der Mädchen","das Mädchen","kein Genus in der L1 → Zuweisung unsicher","interlingual"),
        ("ein Brot (gemeint: bestimmt)","das Brot","Bestimmtheit in der L1 über Kasus","interlingual")]),
  P("<b>1. Nomen-Artikel-Kopplung</b> – Vokabeln nie ohne Artikel; Farbcode <span style='color:#1565c0'>der</span>/<span style='color:#c62828'>die</span>/<span style='color:#2e7d32'>das</span>.")
  +"<p><b>2. Genus-Heuristiken:</b></p><ul class='li'><li>"+d("-ung,-heit,-keit,-schaft,-tion,-e")+" → <span class='ok'>die</span></li><li>"+d("-chen,-lein,-ment,-um")+" → <span class='ok'>das</span></li><li>Agens auf "+d("-er")+", Tages-/Jahreszeiten → <span class='ok'>der</span></li></ul>"
  +P("<b>3. Bestimmtheit kontrastiv</b> – türkisches "+k('-i')+"/"+k('bir')+" gezielt auf deutsches "+d('das')+"/"+d('ein')+" abbilden."),
  P("Auch ohne Artikel/Genus <b>grammatikalisiert das Türkische Bestimmtheit</b> – über das Akkusativsuffix "+k('-i')+" und die Wortstellung. Die Lernenden besitzen das <i>Konzept</i> „bestimmt vs. unbestimmt“ also bereits, nur anders kodiert. Der Artikel ist dann die deutsche <i>Bauform</i> einer längst beherrschten Funktion."),
 ])

DETAIL["plural"]=dict(
 modul="Modul II · Morphologie (Nomen)", titel="Plural & Kasus",
 lead="Der deutsche Plural ist unvorhersehbar (mehrere Typen), der türkische denkbar einfach (ein Suffix). Bei den Kasus ist es umgekehrt: vier (DE) gegen sechs (TR), an ganz anderer Stelle markiert.",
 blocks=[
  T([("Plural",f"fünf Grundtypen {d('-e, -er, -(e)n, -s, ∅')} (+ Umlaut), unvorhersehbar",f"ein Suffix {k('-lAr')} (Harmonie: -ler/-lar)"),
     ("Plural nach Zahl",f"obligatorisch: {d('zwei Kinder')}",f"kein Plural: {k('iki çocuk')}"),
     ("Kasus","4: Nom · Akk · Dat · Gen – am <b>Artikel</b> markiert",f"6: {k('Nom ∅, Akk -i, Dat -e, Lok -de, Abl -den, Gen -in')} – am <b>Nomen</b>")]),
  P("Plural: nicht ableitbar → mit Artikel mitlernen. Kasus: DE markiert <i>verteilt</i> (Artikel/Adjektiv), TR <i>agglutinierend</i> am Nomen. Beides braucht je eine eigene Strategie."),
  ITAB([("zwei Kind","zwei Kinder","im Türkischen kein Plural nach Numeral","interlingual"),
        ("die Autos → die Auten","die Autos","Pluraltyp übergeneralisiert","intralingual"),
        ("mit das Auto","mit dem Auto","Kasus am Artikel nicht realisiert","interlingual")]),
  P("Pluraltypen in Gruppen mit Artikel üben; Regel <b>„nach Zahlwort steht im Deutschen der Plural“</b>; Kasustabellen DE (4) ↔ TR (6) nebeneinander; Wechsel Artikelflexion ↔ Suffix bewusst machen."),
  P("Das türkische System ist hochtransparent (ein Pluralsuffix, klare Kasussuffixe). Diese <b>analytische Klarheit</b> als Brücke nutzen, um die deutsche „verteilte“ Markierung am Artikel zu erklären."),
 ])

DETAIL["pronomen"]=dict(
 modul="Modul II · Morphologie", titel="Pronomen",
 lead="Beide Sprachen haben Personalpronomen – doch das Türkische drückt Besitz per Suffix aus und lässt das Subjekt weg (Pro-Drop). Das überträgt sich gern ins Deutsche.",
 blocks=[
  T([("Personalpron.",f"flektiert: {d('ich / mich / mir')}",f"{k('ben / sen / o')}"),
     ("Possessiv",f"eigenes Wort: {d('mein Buch')}",f"Suffix (+ optional Pron.): {k('(benim) kitab-ım')}"),
     ("Subjekt",f"obligatorisch (auch {d('es')})",f"weglassbar – <b>Pro-Drop</b>: {k('geliyorum')}")]),
  P("Zwei Strukturunterschiede mit hoher Fehlerlast: das obligatorische deutsche Subjekt und der Possessivartikel als eigenständiges Wort."),
  ITAB([("Komme morgen.","Ich komme morgen.","Pro-Drop der L1 übertragen","interlingual"),
        ("benim mein Buch","mein Buch","Possessiv-Doppelung (Suffix-Logik der L1)","interlingual"),
        ("Regnet.","Es regnet.","kein formales Subjekt in der L1","interlingual")]),
  P("Obligatorisches Subjekt im Deutschen (inkl. "+d('es')+") gezielt üben; Possessivartikel-Tabelle (mein/dein/sein …); Reflexivpronomen (mich/dich/sich)."),
  P("Pro-Drop ist ein <b>Systemmerkmal</b> des Türkischen, kein Flüchtigkeitsfehler. Bewusst kontrastieren: „Im Deutschen trägt das Subjekt die Personeninfo, im Türkischen das Verbsuffix.“"),
 ])

DETAIL["kompar"]=dict(
 modul="Modul II · Morphologie", titel="Komparation (Adjektive)",
 lead="Das Deutsche steigert synthetisch (Endung am Wort), das Türkische analytisch (mit Partikeln daha/en). Auch das „als“ funktioniert anders – im Türkischen über den Ablativ.",
 blocks=[
  T([("Komparativ",f"Endung {d('-er')}: schön→schöner",f"Partikel {k('daha')}: {k('daha güzel')}"),
     ("Superlativ",f"{d('am schönsten / der schönste')}",f"Partikel {k('en')}: {k('en güzel')}"),
     ("Vergleich „als“",f"{d('größer als ich')}",f"Ablativ {k('-den')}: {k('benden büyük')}")],
    head=("Stufe","Deutsch","Türkisch")),
  P("Die synthetische deutsche Steigerung (Endung) und der Anschluss mit "+d('als')+" sind die zentralen Lernpunkte; unregelmäßige Formen (gut/besser, viel/mehr) kommen hinzu."),
  ITAB([("mehr schön","schöner",f"analytische Steigerung nach türkischem {k('daha güzel')}","interlingual"),
        ("Ali ist groß von Ahmet","Ali ist größer als Ahmet",f"türkisches {k('-den')} (Ablativ) als „von“ übertragen","interlingual"),
        ("guter (Komparativ)","besser","unregelmäßige Form übergeneralisiert","intralingual")]),
  P("Muster "+d('-er … als')+" und "+d('am -sten')+" automatisieren; unregelmäßige Reihen (gut–besser–am besten); <i>als</i> nach Komparativ fest verankern."),
  P("Das türkische System ("+k('daha/en')+") ist analytisch-transparent. Den Kontrast „TR: extra Wort vs. DE: Endung am Adjektiv“ explizit machen – so wird die deutsche Synthese als bloß <i>andere Bauform</i> erkennbar."),
 ])

DETAIL["verben"]=dict(
 modul="Modul II · Morphologie", titel="Verben",
 lead="Das deutsche Verb verteilt seine Information auf Hilfsverben, Vorsilben und eine Satzklammer. Das türkische Verb bündelt alles in einer Suffixkette am Wortende. Daraus folgen typische Stellungsfehler.",
 blocks=[
  T([("Bauprinzip","analytisch: Hilfsverb + Partizip/Infinitiv",f"agglutinierend: {k('gel-iyor-um')} (Stamm+Tempus/Aspekt+Person)"),
     ("Trennbare Verben",f"{d('aufstehen → ich stehe … auf')} (Klammer)","keine trennbaren Verben"),
     ("Verbposition","V2 / Satzende (Klammer)","stets am <b>Satzende</b>")]),
  P("Trennbare Verben + Verbklammer und die Hilfsverbwahl (haben/sein) sind die großen Baustellen. Das türkische Verb ist hochregelmäßig – die deutsche Verteilung wirkt dagegen „zerrissen“."),
  ITAB([("Ich aufstehe um 7.","Ich stehe um 7 auf.","keine trennbaren Verben in der L1","interlingual"),
        ("Ich habe gegangen.","Ich bin gegangen.","Hilfsverbwahl (Bewegung → sein)","intralingual"),
        ("du gehst → du geht","du gehst","Kongruenzendung ausgelassen","intralingual")]),
  P("Trennbare Verben mit der <b>Satzklammer</b> visualisieren (steht … auf); haben/sein-Regeln (Bewegung/Zustandswechsel → sein); Konjugationsmuster sichern."),
  P("Die türkische Suffixkette ist maximal transparent – alle Information sitzt am Verb. Genau diese Erwartung erklärt die Fehler im Deutschen. Kontrast „gebündelt (TR) vs. geklammert (DE)“ schafft Verständnis statt Frust."),
 ])

DETAIL["zeit"]=dict(
 modul="Modul II · Morphologie", titel="Zeitformen",
 lead="Die Tempora bilden nur scheinbar 1:1 aufeinander ab. Das Türkische grammatikalisiert zusätzlich Evidentialität – eine Kategorie, die das Deutsche gar nicht hat.",
 blocks=[
  T([("Vergangenheit","Perfekt (mündl.) / Präteritum (schriftl.)",f"{k('-di')} (bezeugt) vs. {k('-miş')} (nicht bezeugt)"),
     ("Gegenwart","Präsens (auch futurisch)",f"{k('-iyor')} (Verlauf) / Aorist {k('-r')}"),
     ("Zukunft","Futur I (oft Präsens+Adverb)",f"{k('-ecek')}")],
    head=("Bereich","Deutsch","Türkisch")),
  P("Lernschwer ist nicht die Form, sondern der <b>Gebrauch</b>: Perfekt vs. Präteritum, Aorist → Präsens, und die fehlende deutsche Evidentialität."),
  ITAB([("Ich ging gestern (mündlich)","Ich bin … gegangen","Präteritum statt mündlichem Perfekt","intralingual"),
        ("Ich gehe morgen (ohne Markierung)","Ich werde gehen / Ich gehe morgen","Präsens für Zukunft","intralingual"),
        (k('-miş')+"-Bedeutung nicht ausgedrückt","er sei gekommen / er soll …","Evidentialität der L1 nicht 1:1 kodierbar","interlingual")]),
  P("Perfekt als <b>mündliche</b> Vergangenheit etablieren; Tempusgebrauch funktional statt 1:1; Evidentialität ("+k('-di/-miş')+") im Deutschen lexikalisch wiedergeben (angeblich, soll, sei)."),
  P("Die türkische Evidentialität ("+k('-di/-miş')+") ist ein <b>Ausdrucksreichtum</b>, kein Hindernis. Sie schärft den Blick dafür, wie das Deutsche dieselbe Bedeutung mit Wörtern (statt Suffixen) leistet."),
 ])

DETAIL["imperativ"]=dict(
 modul="Modul II · Morphologie", titel="Imperativ",
 lead="Beide Sprachen befehlen und bitten – das Türkische verfügt aber über mehr Höflichkeitsstufen und sogar einen Imperativ der 3. Person. Im Deutschen sind die Formen an die Anrede gebunden.",
 blocks=[
  T([("du-Form",f"{d('Komm(e)! Arbeite!')}",f"{k('gel!')}"),
     ("ihr / höflich",f"{d('Kommt!')} · {d('Kommen Sie!')} (+ Pron.)",f"{k('gelin / geliniz')}"),
     ("3. Person",f"nur umschrieben ({d('er soll kommen')})",f"echter Imperativ: {k('gelsin')}")],
    head=("Form","Deutsch","Türkisch")),
  P("Die drei deutschen Formen (du/ihr/Sie) und die Pflicht-Inversion bei "+d('Sie')+" sind zentral; die reiche türkische Höflichkeit erzeugt Wahlunsicherheit."),
  ITAB([("Komme Sie!","Kommen Sie!","Sie-Form + Pronomen + Inversion","intralingual"),
        ("Arbeit!","Arbeite!","obligatorisches -e nach Stamm auf -t","intralingual"),
        ("Du komm!","Komm!","Pronomen bei du/ihr entfällt","intralingual")]),
  P("du/ihr/Sie-Formen kontrastiv; bei "+d('Sie')+": Verb + <i>Sie</i> + Rest; -e-Regeln (atme!, arbeite!); Höflichkeit über bitte/Konjunktiv ergänzen."),
  P("Der türkische Imperativ der 3. Person ("+k('gelsin')+") entspricht dem deutschen „er soll …“; die türkische Höflichkeitskultur lässt sich als Anlass nutzen, deutsche Höflichkeitsmittel (Sie, Konjunktiv, bitte) bewusst zu machen."),
 ])

DETAIL["konjunktiv"]=dict(
 modul="Modul II · Morphologie", titel="Konjunktiv",
 lead="Der deutsche Konjunktiv hat zwei Aufgaben: Irrealis/Höflichkeit (K II) und indirekte Rede (K I). Das Türkische deckt das Irreale mit dem Konditional -se/-sa ab – einen Modus der indirekten Rede kennt es nicht.",
 blocks=[
  T([("Irrealis",f"K II: {d('käme, hätte, würde … kommen')}",f"Konditional {k('-se/-sa')}: {k('gelse')}"),
     ("Höflichkeit",f"K II: {d('Ich hätte gern …')}","Optativ/Umschreibung"),
     ("Indirekte Rede",f"K I: {d('er komme, er habe')}","kein Modus – einfache Einbettung")],
    head=("Funktion","Deutsch","Türkisch")),
  P("K II (Irrealis + Höflichkeit) ist für DaZ am wichtigsten; K I (indirekte Rede) ist bildungssprachlich und im Türkischen ohne direktes Äquivalent."),
  ITAB([("Wenn ich reich bin, … (irreal)","Wenn ich reich wäre, …",f"Irrealis in der L1 über {k('-se')} markiert, im DE nicht übertragen","interlingual"),
        ("Ich will einen Kaffee (höflich)","Ich hätte gern einen Kaffee","K II als Höflichkeitsmittel unbekannt","intralingual"),
        ("er sagt, er kommt","er sagt, er komme","indirekte Rede ohne K I","intralingual")]),
  P("K II zuerst (würde-Form + wäre/hätte) für Irrealis und Höflichkeit; K I als bildungssprachliches Mittel der indirekten Rede; Konditionalsätze Typ II/III."),
  P("Das türkische Konditional "+k('-se/-sa')+" deckt die K-II-<i>Funktion</i> bereits ab – darauf lässt sich aufbauen. Der Konjunktiv I der indirekten Rede ist dagegen eine echte deutsche Besonderheit, die explizit eingeführt werden muss."),
 ])

DETAIL["passiv"]=dict(
 modul="Modul II · Morphologie", titel="Passiv",
 lead="Das deutsche Passiv ist analytisch (werden + Partizip II), das türkische synthetisch (ein Suffix am Verb). Außerdem unterscheidet das Deutsche Vorgangs- und Zustandspassiv.",
 blocks=[
  T([("Bildung",f"{d('werden')} + Partizip II: {d('wird geschrieben')}",f"Suffix {k('-Il-/-In-')}: {k('yaz-ıl-ır')}"),
     ("Zustandspassiv",f"{d('sein')} + Part. II: {d('ist geöffnet')}","meist über Resultativ/Adjektiv"),
     ("Agens",f"{d('von')}+Dativ / {d('durch')}+Akk",f"{k('tarafından')} (oft weggelassen)")]),
  P("Zwei Lernpunkte: die <b>werden/sein</b>-Unterscheidung (Vorgang vs. Zustand) und die Agens-Markierung mit "+d('von/durch')+". Das Objekt des Aktivs wird zum Subjekt im Nominativ."),
  ITAB([("Der Brief ist geschrieben (Vorgang gemeint)","… wird geschrieben","Vorgangs-/Zustandspassiv vermischt","intralingual"),
        ("wird von durch mir","von mir","Agens-Präposition + Rektion","intralingual"),
        ("Der Brief schreibt.","… wird geschrieben","Passivbildung fehlt","intralingual")]),
  P("<span class='ex'>werden</span>+Partizip II sichern; Vorgangs- vs. Zustandspassiv (wird geöffnet / ist geöffnet); Agens "+d('von')+"+Dativ; Umformung Aktiv↔Passiv üben."),
  P("Das synthetische türkische Passiv ("+k('-ıl-')+" direkt am Verb) ist transparent. Der Kontrast „ein Suffix (TR) vs. Hilfsverb + Partizip (DE)“ macht die deutsche Konstruktion durchschaubar."),
 ])

DETAIL["praep"]=dict(
 modul="Modul II · Morphologie", titel="Präpositionen vs. Kasussuffixe",
 lead="Wo das Deutsche eine Präposition vor das Nomen stellt (mit Kasusrektion), hängt das Türkische ein Kasussuffix an. Lokalrelationen werden so an entgegengesetzten Enden des Wortes kodiert.",
 blocks=[
  T([("Position",f"<b>vor</b> dem Nomen: {d('in dem Haus')}",f"<b>Suffix</b> am Nomen: {k('ev-de')}"),
     ("Lokal/Direktional","Wechselpräp. an/in/auf + Akk(wohin)/Dat(wo)",f"{k('Lokativ -de / Dativ -e / Ablativ -den')}"),
     ("Rektion","Präp. fordert festen Kasus (mit+Dat, für+Akk)","Suffix trägt die Relation selbst")]),
  P("Doppelte Hürde: die <b>Wahl</b> der Präposition und ihre <b>Kasusrektion</b> – besonders bei Wechselpräpositionen (wohin? Akkusativ / wo? Dativ)."),
  ITAB([("in das Haus (Ort gemeint)","in dem Haus","wohin/wo nicht getrennt","intralingual"),
        ("mit der Auto","mit dem Auto","feste Rektion (mit+Dativ)","intralingual"),
        (k('ev-de')+" → „Haus-in“ Wortfolge","im Haus","Suffix-Logik der L1 statt vorangestellter Präposition","interlingual")]),
  P("Präpositionen in Kasusgruppen lernen (Akk-/Dativ-/Wechsel-/Genitivgruppe); Wechselpräp.: <i>wohin?→Akk</i>, <i>wo?→Dat</i>; türkisches Suffix ↔ deutsche Präposition gegenüberstellen."),
  P("Das türkische Kasussystem ("+k('Lokativ/Dativ/Ablativ')+") ist klar und konsequent. Diese Bedeutungen sind die <b>Brücke</b> zu in/auf/an/aus – die Lernenden kennen die Relationen, sie müssen sie nur „nach vorn“ (zur Präposition) umkodieren."),
 ])

DETAIL["adverb"]=dict(
 modul="Modul II · Morphologie", titel="Adverbien",
 lead="Im Deutschen ist das Adverb oft formgleich mit dem Adjektiv und unflektiert; seine Stellung folgt einer eigenen Logik (TeKaMoLo). Das Türkische bildet manche Adverbien mit -CA.",
 blocks=[
  T([("Form",f"oft = Adjektiv, <b>unflektiert</b>: {d('schnell')}",f"teils Suffix {k('-CA')} ({k('güzel-ce')}), teils = Adjektiv ({k('hızlı')})"),
     ("Stellung",f"relativ frei, Tendenz {d('Te-Ka-Mo-Lo')}","vor dem Verb / Satzende-orientiert")],
    head=("Merkmal","Deutsch","Türkisch")),
  P("Zwei Punkte: das Adverb bleibt <b>unflektiert</b>, und die Reihung mehrerer Angaben folgt der Faustregel "+d('temporal–kausal–modal–lokal')+"."),
  ITAB([("Er fährt schnelle.","Er fährt schnell.","Adverb fälschlich flektiert","intralingual"),
        ("Ich gehe ins Kino heute.","Ich gehe heute ins Kino.","Stellung der Angaben (Te-Ka-Mo-Lo) verletzt","intralingual"),
        ("guter Spieler → er spielt guter","er spielt gut","Adjektiv/Adverb-Abgrenzung","intralingual")]),
  P("Adverb = unflektiert sichern; <b>TeKaMoLo</b> als Stellungsfaustregel; Abgrenzung adverbialer vs. attributiver Gebrauch (er fährt schnell / das schnelle Auto)."),
  P("Der türkische Marker "+k('-CA')+" macht Adverbialität teils sichtbar; im Deutschen fehlt diese Markierung – das bewusst zu kontrastieren erklärt, warum „schnell“ unverändert bleibt."),
 ])

DETAIL["satzart"]=dict(
 modul="Modul III · Syntax", titel="Satzarten",
 lead="Das Deutsche signalisiert den Satztyp über die Stellung des finiten Verbs, das Türkische über Partikeln und Intonation – das Verb bleibt dabei am Satzende.",
 blocks=[
  T([("Aussage","Verb an 2. Stelle (V2)","Verb am Ende"),
     ("Ja/Nein-Frage",f"Verb voran: {d('Kommst du?')}",f"Partikel {k('mi')}: {k('Geliyor mu?')}"),
     ("W-Frage",f"W-Wort + V2: {d('Wann kommst du?')}","Fragewort + Verb final")],
    head=("Satztyp","Deutsch","Türkisch")),
  P("Die Fragebildung ist der Knackpunkt: Deutsch verschiebt das Verb (Inversion), Türkisch hängt die Partikel "+k('mi')+" an – das Verb bleibt stehen."),
  ITAB([("Du kommst? (nur Intonation)","Kommst du?",f"türkische {k('mi')}-Logik: keine Inversion","interlingual"),
        ("Wann du kommst?","Wann kommst du?","W-Wort ohne V2","interlingual"),
        ("Du kommst mu?","Kommst du?","Fragepartikel der L1 übertragen","interlingual")]),
  P("Inversion bei Ja/Nein-Fragen (finites Verb voran); W-Wort + finites Verb an 2. Stelle; Intonationsfragen vom Standard abgrenzen."),
  P("Die türkische Partikel "+k('mi')+" und die deutsche Inversion erfüllen <i>dieselbe Funktion</i> (Frage markieren) mit verschiedenen Mitteln. Diese Äquivalenz explizit zu machen nimmt der Inversion das Willkürliche."),
 ])

DETAIL["wortstell"]=dict(
 modul="Modul III · Syntax", titel="Wortstellung (SOV vs. V2)",
 lead="Das Türkische ist konsequent verbfinal (SOV). Das Deutsche ist „gemischt“: Verbzweit im Hauptsatz mit Satzklammer, verbfinal im Nebensatz. Dieser Wechsel ist eine der größten syntaktischen Hürden.",
 blocks=[
  T([("Grundabfolge","S–V–O / Verbzweit (V2)","S–O–V – konsequent verbfinal"),
     ("Hauptsatz",f"finites Verb an 2. Stelle, Klammer: {d('Ich habe … gekauft')}",f"Verb am Ende: {k('… aldım')}"),
     ("Nebensatz",f"verbfinal: {d('…, weil er kommt')}","ebenfalls verbfinal (Partizip/Konverb)")])
  +NOTE("Grundabfolge im Kontrast: deutscher Hauptsatz <b>S–V–O</b> (Verbzweit), türkischer Satz <b>S–O–V</b> (verbfinal)."),
  P("Lernschwer ist nicht eine einzelne Regel, sondern der <b>Wechsel</b>: V2 im Hauptsatz, Klammer, dann wieder verbfinal im Nebensatz."),
  ITAB([("Ich morgen nach Hause gehe.","Ich gehe morgen nach Hause.","verbfinale Grundabfolge (SOV) der L1","interlingual"),
        ("Ich habe gekauft ein Buch.","Ich habe ein Buch gekauft.","Verbklammer nicht geschlossen","interlingual"),
        ("…, weil er kommt nicht.","…, weil er nicht kommt.","Negationsstellung im Nebensatz","intralingual")]),
  P("V2-Regel (finites Verb an 2. Stelle) markieren; <b>Satzklammer</b> visualisieren; Nebensatz = Verb ans Ende; Umstell- und Klammerübungen."),
  P("Das türkische SOV ist ein <b>einheitlicher</b> Parameter – verlässlich verbfinal. Genau diese Einheitlichkeit macht den deutschen Wechsel (V2 vs. verbfinal) erklärungsbedürftig; bewusst kontrastiert wird er lernbar."),
 ])

DETAIL["relativ"]=dict(
 modul="Modul III · Syntax", titel="Relativsatz",
 lead="Das Deutsche stellt den Relativsatz mit Relativpronomen hinter das Nomen. Das Türkische bildet stattdessen ein vorangestelltes Partizipialattribut – ganz ohne Relativpronomen.",
 blocks=[
  T([("Bauform","nachgestellter Satz + Relativpronomen","vorangestelltes <b>Partizip</b>, kein Pronomen"),
     ("Beispiel",f"der Mann, {d('der')} liest",f"{k('oku-yan')} adam (lesender Mann)"),
     ("„den ich sah“",f"der Mann, {d('den')} ich sah",f"{k('gör-düğüm')} adam")],
    head=("Merkmal","Deutsch","Türkisch")),
  P("Die deutsche Lösung verlangt <b>Relativpronomen</b> (Genus/Numerus vom Bezugswort, Kasus aus der Funktion im Relativsatz) und Verbendstellung – im Türkischen gibt es nichts Vergleichbares."),
  ITAB([("die Frau, die ich helfe","der Frau, der ich helfe","Kasus im Relativsatz (Funktion) nicht bestimmt","intralingual"),
        ("das Mann, der …","der Mann, der …","Genuskongruenz mit dem Bezugswort","intralingual"),
        ("Vermeidung des Relativsatzes","der Mann, der liest","prä-nominales Partizipmuster der L1","interlingual")]),
  P("Relativpronomen-Tabelle (der/die/das, dessen/deren, dem/denen); Kasus nach Funktion im Nebensatz bestimmen; Verb ans Ende; vom türkischen Partizip zum deutschen Relativsatz „übersetzen“."),
  P("Das türkische Partizipialattribut ("+k('okuyan')+", "+k('okuduğum')+") ist das funktionale Äquivalent. Es als Ausgangspunkt zu nehmen („dieselbe Bedeutung, andere Bauform: nachgestellter Satz mit Pronomen“) nutzt vorhandene Kompetenz."),
 ])

# === Arbeitsblätter (DaZ) ==================================================
SHEETS = [
 {"id":"ab_auslaut","t":"Auslautverhärtung","lvl":"A2–B1 / Alphabetisierung",
  "desc":"Verlängern, Fehler korrigieren, kontrastive Brücke + Lösungen.",
  "pdf":"arbeitsblaetter/ab_auslautverhaertung.pdf"},
 {"id":"ab_genus","t":"Genus, Artikel & Bestimmtheit","lvl":"A2–B1",
  "desc":"Genus-Heuristik, Artikel-Korrektur, TR↔DE-Bestimmtheit + Lösungen.",
  "pdf":"arbeitsblaetter/ab_genus-artikel.pdf"},
 {"id":"ab_wortstell","t":"Wortstellung: V2 & Satzklammer","lvl":"A2–B1",
  "desc":"Verb an 2. Stelle, Klammer schließen, Nebensatz verbfinal + Lösungen.",
  "pdf":"arbeitsblaetter/ab_wortstellung.pdf"},
 {"id":"ab_praep","t":"Präpositionen & Kasus (Wechselpräp.)","lvl":"A2–B1",
  "desc":"wohin?/wo?, Suffix↔Präposition, Rektion + Lösungen.",
  "pdf":"arbeitsblaetter/ab_praepositionen.pdf"},
]
SHEET_FOR = {"auslaut":SHEETS[0]["pdf"],"genus":SHEETS[1]["pdf"],
             "wortstell":SHEETS[2]["pdf"],"praep":SHEETS[3]["pdf"]}

# === Literatur ============================================================
LIT = {
 "Kontrastive Grammatik & Sprachvergleich DE–TR": [
  dict(a="Balcı, Tahir", y="o. J.", t="Grundzüge der türkisch-deutschen kontrastiven Grammatik",
       q="Çukurova Üniversitesi (Substantiv, Adjektiv, Verben, Artikel, Interferenzfehler)", proj=True),
  dict(a="Balcı, Tahir", y="1998", t="Abriss der türkisch-deutschen kontrastiven Grammatik",
       q="Diyarbakır: Üniversite (Lehrbuch DaF)"),
  dict(a="Cimilli, N. / Liebe-Harkort, K.", y="1976", t="Sprachvergleich Türkisch–Deutsch",
       q="Düsseldorf: Schwann"),
  dict(a="Rehbein, Jochen", y="1995", t="Grammatik kontrastiv",
       q="Jahrbuch Deutsch als Fremdsprache 21, 265–292"),
  dict(a="Hoffmann, L. / Naumovich, O. / Selmani, L.", y="2018", t="Funktionale Grammatik und Sprachvergleich",
       q="Berlin: Erich Schmidt Verlag"),
 ],
 "Türkische Grammatik & Turkologie": [
  dict(a="Johanson, Lars / Csató, Éva Á. (Hg.)", y="1998", t="The Turkic Languages",
       q="London/New York: Routledge", proj=True),
  dict(a="Johanson, Lars", y="2002", t="Structural Factors in Turkic Language Contacts",
       q="London: Curzon / Routledge", proj=True),
  dict(a="Ersen-Rasch, Margarete I.", y="2001/2012", t="Türkische Grammatik für Anfänger und Fortgeschrittene",
       q="Ismaning: Hueber", proj=True),
  dict(a="Göksel, Aslı / Kerslake, Celia", y="2005", t="Turkish. A Comprehensive Grammar",
       q="London: Routledge"),
 ],
 "Phonetik / Graphematik / Schriftspracherwerb": [
  dict(a="Buchberger (KALiPho)", y="o. J.", t="Schriftsprachliche Interferenzen der Erstsprache Türkisch im DaZ-Erwerb",
       q="Univ. Kiel, Arbeitsberichte", proj=True),
  dict(a="Özen, Erhan", y="1985", t="Untersuchungen zu einer kontrastiven Phonetik Türkisch–Deutsch",
       q="Hamburg: Buske"),
  dict(a="Adıyaman, A. / Bayrak, A.", y="2020", t="Kontrastive Analyse der phonetischen Interferenzfehler von DaF-Studenten mit türkischer Muttersprache",
       q="Akademik Sosyal Araştırmalar Dergisi 8(104), 412–432", cur=True),
 ],
 "Interferenz, Fehleranalyse & Determination": [
  dict(a="Hansen, Björn", y="1995", t="Die deutschen Artikel und ihre Wiedergabe im Türkischen",
       q="Arbeiten zur Mehrsprachigkeit 53"),
  dict(a="Selmani, Lirim", y="2011", t="Determination im Sprachvergleich Deutsch–Türkisch–Albanisch",
       q="in: Hoffmann/Ekinci-Kocks (Hg.), Sprachdidaktik in mehrsprachigen Lerngruppen, 40–52"),
  dict(a="Grießhaber, Wilhelm", y="1999", t="Die relationierende Prozedur. Lokale Präpositionen und ihre Verwendung durch türkische Deutschlerner",
       q="Münster: Waxmann"),
  dict(a="Uslu, Zeki", y="o. J.", t="Almanca ve Türkçe Önermelerde Nedensellik İşlevi",
       q="Doktora-Arbeit (Kausalität DE–TR)", proj=True),
 ],
 "DaZ, Mehrsprachigkeit & Didaktik (aktuell)": [
  dict(a="Koch, Nikolas / Riehl, Claudia Maria", y="2024", t="Migrationslinguistik. Eine Einführung",
       q="Tübingen: Narr Francke Attempto", cur=True),
  dict(a="Tan, Nimet", y="2023", t="Mehrsprachigkeit und Nachhaltigkeitsaspekte in der Deutschlehrkräfteausbildung",
       q="(dt./türk.); sowie: Sprachvergleiche mittels KI in der Hochschullehre", cur=True),
  dict(a="Selmani, Lirim", y="2024", t="Das Passiv im Deutschen und Albanischen. Formenbildung und Funktion",
       q="Deutsche Sprache 2/2024, 139–170", cur=True),
  dict(a="Ekinci-Kocks, Y. / Hoffmann, L. u. a. (Hg.)", y="2013", t="Migration – Mehrsprachigkeit – Bildung",
       q="Tübingen: Stauffenburg"),
 ],
}
LIT_INTRO = ("Auswahlbibliografie zum Sprachvergleich Deutsch–Türkisch und zur DaZ-Didaktik. "
  "Mit ● markierte Titel liegen als Referenzmaterial im Projekt vor; mit ✦ markierte sind "
  "aktuelle Arbeiten (2020+). Die Liste dient als Referenz – Konzept und Inhalt der Plattform "
  "stammen von Dr. Ergun Özsoy.")

def app_json():
    return {"modules":MODULES,"detail":DETAIL,"sheets":SHEETS,
            "sheetFor":SHEET_FOR,"blocknames":BLOCKNAMES,"lit":LIT,"litIntro":LIT_INTRO}
