# -*- coding: utf-8 -*-
"""Erzeugt alle PDFs: Themen-Dossiers (themen/<id>.pdf), DaZ-Arbeitsblätter
(arbeitsblaetter/...), Literatur (literatur/literatur-de-tr.pdf).
Quelle: content.py (einzige Inhaltsquelle)."""
import os, datetime
from weasyprint import HTML
import content as C

OUT=os.path.dirname(os.path.abspath(__file__))  # Skript-Ordner – funktioniert lokal & in CI
for d in ("themen","arbeitsblaetter","literatur"):
    os.makedirs(f"{OUT}/{d}", exist_ok=True)

GREEN="#00883A"; GOLD="#C8A45C"; INK="#222629"
DATE=datetime.date.today().strftime("%d.%m.%Y")

CSS=f"""
@page {{ size:A4; margin:20mm 18mm 22mm 18mm;
  @top-left {{ content:"Kontrastive Linguistik DE \\2194 TR"; font:8pt 'Georgia',serif; color:#888; }}
  @top-right {{ content:"Dr. Ergun \\00D6zsoy \\00B7 LMU M\\00FCnchen"; font:8pt 'Georgia',serif; color:#888; }}
  @bottom-left {{ content:"\\00A9 Dr. Ergun \\00D6zsoy \\2013 alle Rechte vorbehalten"; font:8pt sans-serif; color:#999; }}
  @bottom-right {{ content:"Seite " counter(page) " / " counter(pages); font:8pt sans-serif; color:#999; }} }}
*{{box-sizing:border-box}}
body{{font-family:'Calibri','Segoe UI',sans-serif;color:{INK};font-size:10.5pt;line-height:1.5}}
h1,h2,h3{{font-family:'Georgia','Times New Roman',serif;color:{GREEN};line-height:1.25}}
.brandbar{{height:6px;background:{GREEN};border-radius:3px;margin-bottom:4mm}} .brandbar.gold{{background:{GOLD}}}
.kicker{{font-size:8.5pt;letter-spacing:.12em;text-transform:uppercase;color:{GOLD};font-weight:700}}
h1{{font-size:21pt;margin:1mm 0 1mm}} .lead{{color:#555;font-size:10.5pt;margin:0 0 5mm}}
.block{{border:1px solid #e3e3e3;border-left:4px solid {GREEN};border-radius:6px;padding:4mm 5mm;margin:0 0 5mm;break-inside:avoid}}
.block .num{{display:inline-block;min-width:18px;color:{GOLD};font-weight:700;font-family:'Georgia',serif}}
.block h2{{font-size:13pt;margin:0 0 2mm}}
table{{width:100%;border-collapse:collapse;margin:2mm 0;font-size:9.6pt}}
th,td{{border:1px solid #dcdcdc;padding:2mm 3mm;text-align:left;vertical-align:top}}
th{{background:#f3f6f3;color:{GREEN};font-family:'Georgia',serif}}
td.de{{background:#fbfdfb}} td.tr{{background:#fdfbf6}}
.ex{{font-family:'Consolas','Courier New',monospace}}
.trk{{font-family:'Consolas','Courier New',monospace;font-style:italic;color:#9a6a12;font-weight:600}}
td.de .ex{{color:#16407a}}
td.tr .ex{{color:#9a6a12;font-style:italic}}
.err{{color:#b3261e;text-decoration:line-through}} .err::before{{content:"\\2717 ";text-decoration:none;font-weight:700}}
.ok{{color:{GREEN};font-weight:600}} .ok::before{{content:"\\2713 ";font-weight:700}}
.tag.typ.il{{background:#f6efe1;color:#8a6b22;border-color:#e6d4a6}} .tag.typ.al{{background:#eef1f6;color:#3a4a66;border-color:#cdd6e6}}
.tag{{display:inline-block;font-size:8pt;padding:1px 7px;border-radius:10px;background:#eef3ee;color:{GREEN};border:1px solid #cfe0cf}}
.tag.cat{{background:#f6efe1;color:#8a6b22;border-color:#e6d4a6}}
ul,ul.li{{margin:1mm 0 1mm 5mm;padding:0}} li{{margin:1mm 0}}
.note{{font-size:9pt;color:#666;font-style:italic}}
.foot{{margin-top:6mm;padding-top:3mm;border-top:1px solid #e3e3e3;font-size:8.5pt;color:#888}}
.task{{border:1px solid #e3e3e3;border-radius:6px;padding:3.5mm 4mm;margin:0 0 4mm;break-inside:avoid}}
.task h3{{font-size:11.5pt;margin:0 0 1.5mm;color:{INK}}}
.task .meta{{font-size:8.5pt;color:{GOLD};font-weight:700;text-transform:uppercase;letter-spacing:.08em}}
.line{{border-bottom:1px solid #bbb;min-height:6mm}}
.litcat{{font-family:'Georgia',serif;color:{GREEN};font-size:12pt;border-bottom:1px solid #e3e3e3;padding-bottom:1.5mm;margin:5mm 0 2mm;break-after:avoid}}
.lit{{font-size:9.6pt;padding:1.6mm 0;border-bottom:1px dashed #eee;break-inside:avoid}}
.lit .au{{font-weight:600}} .lit .ti{{font-style:italic}} .lit .q{{color:#666}}
.mk{{font-size:7.5pt;border-radius:8px;padding:0 5px;margin-left:4px}} .mk.proj{{background:#e2f0e6;color:#04632c}} .mk.cur{{background:#f6efe1;color:#8a6b22}}
"""

def render(path, inner, gold=False):
    HTML(string=f"<!doctype html><html lang='de'><head><meta charset='utf-8'><style>{CSS}</style></head>"
                f"<body><div class='brandbar {'gold' if gold else ''}'></div>{inner}</body></html>"
        ).write_pdf(path)
    print("  ->", path.split("/")[-1], os.path.getsize(path), "B")

# ---- Themen-Dossiers ------------------------------------------------------
def topic_pdf(tid, d):
    parts=[f'<div class="kicker">{d["modul"]} &middot; Sprachvergleich</div>'
           f'<h1>{d["titel"]}</h1><p class="lead">{d["lead"]}</p>']
    for i,b in enumerate(d["blocks"]):
        parts.append(f'<div class="block"><h2><span class="num">{i+1}</span>{C.BLOCKNAMES[i]}</h2>{b}</div>')
    parts.append(f'<div class="foot">Lernerformen nach Ursache: <i>intralingual</i> (systematisch) vs. '
                 f'<i>interlingual</i> (aus der L1). Quellen: siehe Literatur-Seite. '
                 f'&middot; Stand: {DATE} &middot; Konzept &amp; Inhalt: Dr. Ergun &Ouml;zsoy, LMU M&uuml;nchen.</div>')
    render(f"{OUT}/themen/{tid}.pdf", "".join(parts))

print("Themen-Dossiers:")
for tid,d in C.DETAIL.items():
    topic_pdf(tid,d)

# ---- Arbeitsblätter -------------------------------------------------------
def worksheet(path, meta, intro, tasks, solutions):
    head=(f'<div class="kicker">DaZ-Arbeitsblatt &middot; {meta["modul"]}</div><h1>{meta["titel"]}</h1>'
          f'<p class="lead">{meta["niveau"]} &middot; {meta["ziel"]}</p><p>{intro}</p>')
    body="".join(f'<div class="task"><div class="meta">Aufgabe {i+1} &middot; {t["typ"]}</div>'
                 f'<h3>{t["titel"]}</h3>{t["html"]}</div>' for i,t in enumerate(tasks))
    sol=('<div style="break-before:page"></div><div class="brandbar gold"></div>'
         '<div class="kicker">L&ouml;sungsschl&uuml;ssel</div>'
         f'<h1 style="font-size:17pt">L&ouml;sungen &amp; Lehrerhinweise</h1>{solutions}')
    foot=(f'<div class="foot">DaZ-Material zum Sprachvergleich DE&ndash;TR &middot; '
          f'Konzept: Dr. Ergun &Ouml;zsoy, LMU M&uuml;nchen &middot; Stand: {DATE}</div>')
    render(path, head+body+foot+sol, gold=True)

print("Arbeitsblätter:")
worksheet(f"{OUT}/arbeitsblaetter/ab_auslautverhaertung.pdf",
 {"modul":"Laut &amp; Schrift","titel":"Auslautverh&auml;rtung &ndash; richtig h&ouml;ren, richtig schreiben",
  "niveau":"A2&ndash;B1 / Alphabetisierung","ziel":"Rechtschreibstrategie &bdquo;Verl&auml;ngern&ldquo;"},
 "Im Deutschen spricht man am Wortende oft [p t k], schreibt aber <b>b d g</b>. Verl&auml;ngere das Wort, dann h&ouml;rst du den richtigen Buchstaben.",
 [{"typ":"Verl&auml;ngern","titel":"Finde das richtige Endgraphem","html":"""
   <p>Verl&auml;ngere und entscheide: <b>b/p</b>, <b>d/t</b> oder <b>g/k</b>?</p>
   <table><tr><th>Wort</th><th>verl&auml;ngert &rarr;</th><th>Endbuchstabe</th></tr>
   <tr><td class="ex">Hun__</td><td class="line"></td><td class="line"></td></tr>
   <tr><td class="ex">Ta__</td><td class="line"></td><td class="line"></td></tr>
   <tr><td class="ex">lie__</td><td class="line"></td><td class="line"></td></tr>
   <tr><td class="ex">Kor__ (Korb)</td><td class="line"></td><td class="line"></td></tr>
   <tr><td class="ex">Zu__ (Zug)</td><td class="line"></td><td class="line"></td></tr></table>"""},
  {"typ":"Fehler korrigieren","titel":"Verbessere die Schreibung","html":"""
   <p>Diese Schreibungen folgen der t&uuml;rkischen Regel &bdquo;schreib, was du h&ouml;rst&ldquo;. Schreibe die deutsche Form daneben.</p>
   <table><tr><th>falsch</th><th>richtig</th></tr>
   <tr><td class="ex">der Hunt</td><td class="line"></td></tr><tr><td class="ex">am Tak</td><td class="line"></td></tr>
   <tr><td class="ex">das Kint</td><td class="line"></td></tr><tr><td class="ex">der Berk</td><td class="line"></td></tr></table>"""},
  {"typ":"Kontrastiv","titel":"Br&uuml;cke zum T&uuml;rkischen","html":"""
   <p>Im T&uuml;rkischen wechselt der Laut auch &ndash; aber man <i>schreibt</i> ihn: <span class="trk">kitap &ndash; kitab&#305;</span>. Erg&auml;nze und markiere, wo Deutsch das Graphem <b>beh&auml;lt</b>:</p>
   <p class="ex">Tag &ndash; Ta__e &nbsp;|&nbsp; Hund &ndash; Hun__e &nbsp;|&nbsp; lieb &ndash; lie__er</p>"""}],
 """<ul><li><b>A1:</b> Hun<b>d</b> &middot; Ta<b>g</b> &middot; lie<b>b</b> &middot; Kor<b>b</b> &middot; Zu<b>g</b>.</li>
    <li><b>A2:</b> Hund &middot; Tag &middot; Kind &middot; Berg.</li>
    <li><b>A3:</b> Ta<b>g</b>e &middot; Hun<b>d</b>e &middot; lie<b>b</b>er &ndash; das Graphem bleibt.</li>
    <li class="note">Den Prozess kennen die Lernenden aus dem T&uuml;rkischen; nur die Schreibkonvention ist neu.</li></ul>""")

worksheet(f"{OUT}/arbeitsblaetter/ab_genus-artikel.pdf",
 {"modul":"Nomen","titel":"Genus, Artikel &amp; Bestimmtheit","niveau":"A2&ndash;B1","ziel":"Artikel sichern, Bestimmtheit kontrastiv verstehen"},
 "Das T&uuml;rkische hat keinen Artikel und kein Genus. Diese &Uuml;bungen sichern <b>der/die/das</b> und zeigen, wie das T&uuml;rkische Bestimmtheit anders ausdr&uuml;ckt.",
 [{"typ":"Genus-Heuristik","titel":"der, die oder das?","html":"""
   <p>Nutze die Endungen-Regeln. Trage den Artikel ein.</p>
   <table><tr><th>Nomen</th><th>Artikel</th><th>Nomen</th><th>Artikel</th></tr>
   <tr><td class="ex">Zeitung</td><td class="line"></td><td class="ex">M&auml;dchen</td><td class="line"></td></tr>
   <tr><td class="ex">Freiheit</td><td class="line"></td><td class="ex">Lehrer</td><td class="line"></td></tr>
   <tr><td class="ex">Nation</td><td class="line"></td><td class="ex">Dokument</td><td class="line"></td></tr>
   <tr><td class="ex">Freundschaft</td><td class="line"></td><td class="ex">Sommer</td><td class="line"></td></tr></table>"""},
  {"typ":"Fehler korrigieren","titel":"Artikel erg&auml;nzen / korrigieren","html":"""
   <table><tr><th>Lernersatz</th><th>korrekt</th></tr>
   <tr><td class="ex">Ich sehe Mann.</td><td class="line"></td></tr>
   <tr><td class="ex">der M&auml;dchen lacht.</td><td class="line"></td></tr>
   <tr><td class="ex">Ich brauche Buch.</td><td class="line"></td></tr></table>"""},
  {"typ":"Kontrastiv","titel":"Bestimmtheit: T&uuml;rkisch &harr; Deutsch","html":"""
   <p>Im T&uuml;rkischen zeigt <span class="ex">-i</span> ein <b>bestimmtes</b> Objekt. Erg&auml;nze den deutschen Artikel:</p>
   <table><tr><th>T&uuml;rkisch</th><th>Deutsch</th></tr>
   <tr><td class="trk">Kitab&#305; okuyorum.</td><td>Ich lese ____ Buch.</td></tr>
   <tr><td class="trk">Bir kitap okuyorum.</td><td>Ich lese ____ Buch.</td></tr>
   <tr><td class="trk">Adam&#305; g&ouml;r&uuml;yorum.</td><td>Ich sehe ____ Mann.</td></tr></table>"""}],
 """<ul><li><b>A1:</b> die Zeitung &middot; das M&auml;dchen &middot; die Freiheit &middot; der Lehrer &middot; die Nation &middot; das Dokument &middot; die Freundschaft &middot; der Sommer.</li>
    <li><b>A2:</b> Ich sehe <b>einen</b> Mann. &middot; <b>Das</b> M&auml;dchen lacht. &middot; Ich brauche <b>ein</b> Buch.</li>
    <li><b>A3:</b> <b>das</b> Buch &middot; <b>ein</b> Buch &middot; <b>den</b> Mann.</li>
    <li class="note">A3 macht sichtbar: Bestimmtheit ist aus dem T&uuml;rkischen (Kasus) bekannt und wird nur deutsch umkodiert.</li></ul>""")

worksheet(f"{OUT}/arbeitsblaetter/ab_wortstellung.pdf",
 {"modul":"Syntax","titel":"Wortstellung: Verbzweit &amp; Satzklammer","niveau":"A2&ndash;B1","ziel":"V2 sichern, Klammer schlie&szlig;en, Nebensatz verbfinal"},
 "Im T&uuml;rkischen steht das Verb am Ende. Im Deutschen steht das finite Verb im Hauptsatz an <b>2. Stelle</b> &ndash; im Nebensatz aber am Ende.",
 [{"typ":"V2 herstellen","titel":"Bring das Verb an die 2. Stelle","html":"""
   <p>Beginne mit dem <u>fett</u> markierten Satzglied.</p>
   <table><tr><th>durcheinander</th><th>richtig</th></tr>
   <tr><td class="ex"><b>Morgen</b> / ich / fahre / nach Berlin</td><td class="line"></td></tr>
   <tr><td class="ex"><b>Heute</b> / wir / lernen / Deutsch</td><td class="line"></td></tr></table>"""},
  {"typ":"Klammer schlie&szlig;en","titel":"Setze das zweite Verbteil ans Ende","html":"""
   <table><tr><th>Lernersatz</th><th>richtig</th></tr>
   <tr><td class="ex">Ich habe gekauft ein Buch.</td><td class="line"></td></tr>
   <tr><td class="ex">Er ist gegangen schnell nach Hause.</td><td class="line"></td></tr>
   <tr><td class="ex">Ich aufstehe um sieben.</td><td class="line"></td></tr></table>"""},
  {"typ":"Nebensatz","titel":"Verb ans Ende (weil/dass)","html":"""
   <table><tr><th>Hauptsatz + …</th><th>Nebensatz</th></tr>
   <tr><td>Er kommt nicht, weil … (er / ist / krank)</td><td class="line"></td></tr>
   <tr><td>Ich wei&szlig;, dass … (du / Deutsch / lernst)</td><td class="line"></td></tr></table>"""}],
 """<ul><li><b>A1:</b> Morgen <b>fahre</b> ich nach Berlin. &middot; Heute <b>lernen</b> wir Deutsch. (finites Verb an 2. Stelle)</li>
    <li><b>A2:</b> Ich habe ein Buch <b>gekauft</b>. &middot; Er ist schnell nach Hause <b>gegangen</b>. &middot; Ich <b>stehe</b> um sieben <b>auf</b>.</li>
    <li><b>A3:</b> …, weil er krank <b>ist</b>. &middot; …, dass du Deutsch <b>lernst</b>. (Verb am Ende)</li>
    <li class="note">Kontrast: TR ist immer verbfinal; DE wechselt zwischen V2 (Hauptsatz) und verbfinal (Nebensatz).</li></ul>""")

worksheet(f"{OUT}/arbeitsblaetter/ab_praepositionen.pdf",
 {"modul":"Pr&auml;positionen","titel":"Pr&auml;positionen &amp; Kasus","niveau":"A2&ndash;B1","ziel":"Wechselpr&auml;positionen (wohin?/wo?), Suffix &harr; Pr&auml;position"},
 "Das T&uuml;rkische h&auml;ngt ein <b>Suffix</b> ans Nomen (<span class='trk'>ev-de</span> = im Haus). Das Deutsche stellt eine <b>Pr&auml;position davor</b> &ndash; mit festem Kasus.",
 [{"typ":"wohin? / wo?","titel":"Akkusativ oder Dativ?","html":"""
   <p>Wechselpr&auml;position: <b>wohin?</b> &rarr; Akkusativ, <b>wo?</b> &rarr; Dativ.</p>
   <table><tr><th>Satz</th><th>Akk / Dat?</th></tr>
   <tr><td class="ex">Ich gehe in ___ Schule. (wohin?)</td><td class="line"></td></tr>
   <tr><td class="ex">Ich bin in ___ Schule. (wo?)</td><td class="line"></td></tr>
   <tr><td class="ex">Das Bild h&auml;ngt an ___ Wand. (wo?)</td><td class="line"></td></tr></table>"""},
  {"typ":"Suffix &harr; Pr&auml;position","titel":"&Uuml;bersetze die Relation","html":"""
   <table><tr><th>T&uuml;rkisch</th><th>Deutsch</th></tr>
   <tr><td class="trk">ev-de</td><td>____ Haus (wo?)</td></tr>
   <tr><td class="trk">ev-e</td><td>____ Haus (wohin?)</td></tr>
   <tr><td class="trk">ev-den</td><td>____ Haus (woher?)</td></tr></table>"""},
  {"typ":"Rektion","titel":"Fester Kasus","html":"""
   <table><tr><th>Lernersatz</th><th>richtig</th></tr>
   <tr><td class="ex">mit der Auto</td><td class="line"></td></tr>
   <tr><td class="ex">f&uuml;r mein Bruder</td><td class="line"></td></tr></table>"""}],
 """<ul><li><b>A1:</b> in <b>die</b> Schule (Akk) &middot; in <b>der</b> Schule (Dat) &middot; an <b>der</b> Wand (Dat).</li>
    <li><b>A2:</b> <b>im</b> Haus &middot; <b>ins</b> Haus &middot; <b>aus dem</b> Haus. (Lokativ/Dativ/Ablativ &harr; in/in/aus)</li>
    <li><b>A3:</b> mit <b>dem</b> Auto (mit+Dativ) &middot; f&uuml;r <b>meinen</b> Bruder (f&uuml;r+Akk).</li>
    <li class="note">TR kodiert die Relation am Nomen-Suffix; DE an Pr&auml;position + Kasus.</li></ul>""")

# ---- Literatur-PDF --------------------------------------------------------
print("Literatur:")
lit=[f'<div class="kicker">Bibliografie &middot; Sprachvergleich DE&ndash;TR / DaZ</div>',
     '<h1>Literatur</h1>', f'<p class="lead">{C.LIT_INTRO}</p>']
for cat,items in C.LIT.items():
    lit.append(f'<div class="litcat">{cat}</div>')
    for e in items:
        marks=(('<span class="mk proj">&#9679; im Projekt</span>' if e.get("proj") else '')
              +('<span class="mk cur">&#10022; aktuell</span>' if e.get("cur") else ''))
        lit.append(f'<div class="lit"><span class="au">{e["a"]}</span> ({e["y"]}): '
                   f'<span class="ti">{e["t"]}</span>. <span class="q">{e["q"]}.</span>{marks}</div>')
lit.append(f'<div class="foot">Auswahl als Referenzmaterial &middot; Stand: {DATE} &middot; '
           f'Konzept &amp; alle Rechte: Dr. Ergun &Ouml;zsoy, LMU M&uuml;nchen.</div>')
render(f"{OUT}/literatur/literatur-de-tr.pdf", "".join(lit))

print("\nFERTIG.")
