import os
ROOT = os.path.expanduser('~/Developer/_sites/Cogwisp')
BASE = 'https://pinkysworld.github.io/Cogwisp/'
ADDR = 'Michel Nguyen<br>Minh Nguyen Studios<br>Windmühlenstr. 74<br>07937 Zeulenroda-Triebes<br>{country}'
MAIL = '<a href="mailto:mip@gmx.biz">mip@gmx.biz</a>'

T = {
 'de': dict(tag='Rätselspiel für Android', home='Startseite', support='Hilfe &amp; Support', privacy='Datenschutz',
            imprint='Impressum', skip='Zum Inhalt', other='en', otherlabel='EN', otheraria='Switch to English',
            foot='Keine Cookies, keine Tracker, keine externen Skripte.', country='Deutschland', locale='de_DE'),
 'en': dict(tag='Puzzle game for Android', home='Home', support='Help &amp; Support', privacy='Privacy',
            imprint='Legal notice', skip='Skip to content', other='de', otherlabel='DE', otheraria='Auf Deutsch wechseln',
            foot='No cookies, no trackers, no external scripts.', country='Germany', locale='en_US'),
}

def page(lang, name, title, desc, body, cls=''):
    t = T[lang]; pre = '' if lang == 'de' else '../'
    path = name if lang == 'de' else 'en/' + name
    urlname = '' if name == 'index.html' else name
    de_url = BASE + urlname; en_url = BASE + 'en/' + urlname
    other_href = ('en/' if lang == 'de' else '../') + (urlname or '')
    if not other_href: other_href = './'
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#2a1c13">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{de_url if lang=='de' else en_url}">
<link rel="alternate" hreflang="de" href="{de_url}">
<link rel="alternate" hreflang="en" href="{en_url}">
<link rel="alternate" hreflang="x-default" href="{de_url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Cogwisp">
<meta property="og:locale" content="{t['locale']}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{de_url if lang=='de' else en_url}">
<meta property="og:image" content="{BASE}img/feature-{lang}.webp">
<link rel="icon" href="{pre}favicon.png">
<link rel="apple-touch-icon" href="{pre}img/icon-192.png">
<link rel="stylesheet" href="{pre}style.css">
</head>
<body class="{cls}">
<a class="skip" href="#main">{t['skip']}</a>
<header class="top"><nav class="wrap" aria-label="Navigation">
<a class="brand" href="./"><img src="{pre}img/icon.webp" width="40" height="40" alt=""><span>Cogwisp<small>{t['tag']}</small></span></a>
<div class="links">
<a href="support.html">{t['support']}</a>
<a class="lang" href="{other_href}" hreflang="{t['other']}" lang="{t['other']}" aria-label="{t['otheraria']}">{t['otherlabel']}</a>
</div>
</nav></header>
<main id="main">
{body}
</main>
<footer class="wrap footer">
<p><a href="./">Cogwisp</a> · <a href="support.html">{t['support']}</a> · <a href="privacy.html">{t['privacy']}</a> · <a href="impressum.html">{t['imprint']}</a></p>
<p>© 2026 Minh Nguyen Studios · Michel Nguyen</p>
<p>{t['foot']}</p>
</footer>
</body>
</html>
'''

def write(lang, name, html):
    p = os.path.join(ROOT, name if lang == 'de' else 'en/' + name)
    open(p, 'w').write(html)

def doc(h1, sub, sections):
    s = ''.join(f'<section class="card doc-section">\n<h2>{h}</h2>\n{c}\n</section>\n' for h, c in sections)
    sub = f'<p class="stand">{sub}</p>' if sub else ''
    return f'<div class="wrap doc">\n<header class="doc-head"><h1>{h1}</h1>{sub}</header>\n{s}</div>'

# ---------- index ----------
IDX = {
 'de': dict(
  title='Cogwisp – Zahnrad- und Riemenrätsel für Android',
  desc='Verbinde Zahnräder und Riemen. Erwecke kleine Werkstattmaschinen zum Leben. 36 handgebaute Rätselräume, keine Werbung, kein Abo.',
  lead='Verbinde Zahnräder und Riemen. Erwecke kleine Werkstattmaschinen zum Leben.',
  intro='Ein Funke, eine Kurbel und eine Maschine, die wieder laufen möchte. In Cogwisp leitest du mechanische Energie durch eine warme Werkstatt aus Holz und Messing. Drehe Bauteile, versetze bewegliche Teile und finde den passenden Weg von der Quelle zu jedem Ziel.',
  badge='Bald bei Google Play', badgesub='Cogwisp ist noch nicht veröffentlicht.',
  how='So funktioniert’s',
  how_p='Nicht nur die Verbindung zählt: Ziele verlangen die richtige Drehrichtung und Drehzahl. Zahnräder und gekreuzte Riemen kehren die Richtung um, Kupplungen öffnen oder schließen einen Antrieb. Später kommen Freiläufe und Nocken hinzu, deren Arbeitsphasen du aufeinander abstimmst. Einzelschritt und Probelauf helfen dir, die Bewegungen nachzuvollziehen.',
  feat='Deine Werkstatt',
  feats=['36 handgebaute Rätselräume in sechs Kapiteln.',
         'Tippen zum Drehen, Ziehen zum Versetzen oder Tauschen beweglicher Teile.',
         'Unbegrenztes Rückgängigmachen während einer Spielsitzung und ein rückgängig zu machender Neustart des Raums.',
         'Drei gestufte Hinweise pro Raum und eine gesondert aufrufbare Lösung.',
         'Lokal gespeicherter Fortschritt und Rätselzwischenstände.',
         'Deutsch und Englisch, im Menü umschaltbar.',
         'Keine Werbung.'],
  shots='Einblicke', shotalt='Cogwisp-Screenshot',
  price='Prolog gratis, Vollversion einmal kaufen',
  price_p='Sechs Prologräume spielst du kostenlos. Die 30 weiteren Räume schaltest du über einen einmaligen In-App-Kauf frei. Kein Abonnement.',
  offline='Die Rätsel und ein bereits lokal gespeicherter Vollversionszugang sind offline spielbar. Für Kauf und Wiederherstellung ist Google Play mit Internetverbindung erforderlich.',
  featalt='Cogwisp – Werkstatt aus Holz und Messing'),
 'en': dict(
  title='Cogwisp – gear and belt puzzles for Android',
  desc='Connect gears and belts. Bring little workshop machines to life. 36 handcrafted puzzle rooms, no ads, no subscription.',
  lead='Connect gears and belts. Bring little workshop machines to life.',
  intro='A spark, a crank, and a machine waiting to run again. In Cogwisp, route mechanical power through a warm workshop of wood and brass. Rotate parts, move the movable pieces, and find a path from the source to every target.',
  badge='Coming soon to Google Play', badgesub='Cogwisp has not been released yet.',
  how='How it works',
  how_p='A connection is only the beginning: targets need the right rotation and speed. Gears and crossed belts reverse direction, while clutches engage or disconnect a drive. Later, freewheels and cams add new problems, including working phases to coordinate. Step through a cycle or use Test run to see the movement unfold.',
  feat='Your workshop',
  feats=['36 handcrafted puzzle rooms across six chapters.',
         'Tap to rotate; drag to move or swap movable parts.',
         'Unlimited undo during a play session, plus a room reset you can undo.',
         'Three progressive hints per room and a separately available solution.',
         'Progress and unfinished puzzles saved locally.',
         'English and German, switchable in the menu.',
         'No ads.'],
  shots='A look inside', shotalt='Cogwisp screenshot',
  price='Free prologue, buy the full game once',
  price_p='The six prologue rooms are free to play. Unlock the 30 further rooms through a single in-app purchase. No subscription.',
  offline='Puzzles and a full-game unlock already saved locally can be played offline. Purchases and purchase restoration require Google Play and an internet connection.',
  featalt='Cogwisp – a workshop of wood and brass'),
}
for lang, d in IDX.items():
    pre = '' if lang == 'de' else '../'
    feats = ''.join(f'<li>{f}</li>' for f in d['feats'])
    shots = ''.join(f'<figure><img src="{pre}img/{lang}-{n}.webp" width="540" height="960" loading="lazy" alt="{d["shotalt"]} {i+1}"></figure>' for i, n in enumerate(['01','07','13','25']))
    body = f'''<section class="hero"><div class="wrap hero-grid">
<div>
<h1>Cogwisp</h1>
<p class="lead">{d['lead']}</p>
<p>{d['intro']}</p>
<p class="badge"><strong>{d['badge']}</strong><span>{d['badgesub']}</span></p>
</div>
<img class="feature" src="{pre}img/feature-{lang}.webp" width="1024" height="500" alt="{d['featalt']}">
</div></section>
<section class="wrap block"><h2>{d['how']}</h2><p>{d['how_p']}</p></section>
<section class="wrap block"><h2>{d['shots']}</h2><div class="shots">{shots}</div></section>
<section class="wrap block two">
<div class="card"><h2>{d['feat']}</h2><ul class="gears">{feats}</ul></div>
<div class="card accent"><h2>{d['price']}</h2><p>{d['price_p']}</p><p class="muted">{d['offline']}</p></div>
</section>'''
    write(lang, 'index.html', page(lang, 'index.html', d['title'], d['desc'], body, 'home'))

# ---------- impressum ----------
write('de', 'impressum.html', page('de', 'impressum.html', 'Impressum – Cogwisp', 'Impressum und Anbieterkennzeichnung für Cogwisp.', doc('Impressum', '', [
 ('Angaben gemäß § 5 DDG', '<address>' + ADDR.format(country='Deutschland') + '</address>'),
 ('Kontakt', f'<p>E-Mail: {MAIL}</p>'),
 ('Geltungsbereich', '<p>Dieses Impressum gilt für diese Website und die Android-App „Cogwisp“.</p>'),
 ('Verbraucherstreitbeilegung', '<p>Wir sind nicht bereit oder verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.</p><p><a href="privacy.html">Datenschutzerklärung</a></p>'),
]), 'document-page'))
write('en', 'impressum.html', page('en', 'impressum.html', 'Legal notice – Cogwisp', 'Legal notice (Impressum) for Cogwisp.', doc('Legal notice (Impressum)', '', [
 ('Information pursuant to § 5 DDG', '<address>' + ADDR.format(country='Germany') + '</address>'),
 ('Contact', f'<p>Email: {MAIL}</p>'),
 ('Scope', '<p>This legal notice applies to this website and the Android app “Cogwisp”.</p>'),
 ('Consumer dispute resolution', '<p>We are neither willing nor obliged to participate in dispute resolution proceedings before a consumer arbitration board.</p><p><a href="privacy.html">Privacy policy</a></p>'),
]), 'document-page'))

# ---------- privacy ----------
GPRIV = '<a href="https://policies.google.com/privacy" rel="noopener">{}</a>'
GHPRIV = '<a href="https://docs.github.com/site-policy/privacy-policies/github-general-privacy-statement" rel="noopener">{}</a>'
write('de', 'privacy.html', page('de', 'privacy.html', 'Datenschutzerklärung – Cogwisp', 'Datenschutzerklärung für die Android-App Cogwisp und diese Website.', doc('Datenschutzerklärung', 'Stand: 31. Oktober 2026', [
 ('Kurz gesagt', '<p>Cogwisp ist ein Offline-Rätselspiel ohne eigenes Benutzerkonto, ohne eigenen Server, ohne Werbung und ohne eigenes Tracking oder Analytics. Dein Spielstand bleibt auf deinem Gerät. Für den Kauf der Vollversion nutzt die App Google Play Billing; dabei verarbeitet Google Daten – darunter technische Diagnosedaten, die die Billing-Bibliothek an Google sendet. Diese Website setzt keine Cookies und verwendet keine Tracker.</p>'),
 ('Verantwortlicher', '<address>' + ADDR.format(country='Deutschland') + f'<br>E-Mail: {MAIL}</address>'),
 ('Die App „Cogwisp“: lokale Daten', '''<p><strong>Kein Konto, kein eigener Server:</strong> Der eigene Code der App enthält keinen Netzwerk-Client, kein Werbe- und kein Analyse-SDK. Wir erhalten aus der App keine Daten von dir.</p>
<p><strong>Lokale Speicherung:</strong> Fortschritt, Spracheinstellung und Rätselzwischenstände werden ausschließlich lokal im App-Speicher deines Geräts abgelegt. Die Freischaltung der Vollversion wird ebenfalls lokal vermerkt; die App speichert dort keine Zahlungsdaten. Android-Datensicherung (Backup) ist für die App deaktiviert.</p>
<p><strong>Berechtigungen:</strong> Die App fordert keinen Zugriff auf Kamera, Mikrofon, Kontakte, Speicher, Standort, Werbe-ID oder Benachrichtigungen an. Deklariert sind die Google-Play-Kaufberechtigung sowie – durch die eingebundenen Google-Bibliotheken – Internetzugriff und Abfrage des Netzwerkstatus.</p>
<p><strong>Löschen:</strong> Über „Speicherinhalt löschen“ in den Android-Einstellungen oder durch Deinstallation entfernst du alle lokalen App-Daten. Das storniert keinen Kauf und löscht keine bereits an Google übermittelten Daten. Nach einer Neuinstallation kannst du den Kauf wiederherstellen.</p>'''),
 ('Kauf der Vollversion über Google Play', f'''<p>Der Prolog ist kostenlos. Die Vollversion wird per einmaligem In-App-Kauf über Google Play Billing freigeschaltet. Bezahlung und Kaufabwicklung führt Google durch; wir erhalten keine Zahlungs- oder Kartendaten. Die App verarbeitet Produktkennung, Kaufstatus und ein Kauftoken, um den Kauf gegenüber Google Play zu bestätigen und die Freischaltung zu speichern. Google verarbeitet Kauf-, Zahlungs- und Kontodaten in eigener Verantwortung nach der {GPRIV.format("Datenschutzerklärung von Google")}.</p>
<p><strong>Technische Diagnosedaten:</strong> Die in die App eingebundene Google-Play-Billing-Bibliothek überträgt technische Diagnosedaten an Google (Endpunkt firebaselogging.googleapis.com). Beobachtet wurden u. a. Status- bzw. Fehlermeldungen der Billing-Funktion, App-Paketname, App- und Bibliotheksversion, Gerätemodell, Hersteller, Betriebssystemversion/-build, Sprache und Land, Zeitzone, Netzwerktyp sowie Mobilfunk-Ländercode und -Netzbetreiber (MCC/MNC). Diese Daten werden zunächst lokal zwischengespeichert und bei bestehender Verbindung gesendet. Nicht alle Felder dieser Übertragung konnten von uns entschlüsselt werden; wir können daher nicht ausschließen, dass sie weitere technische Kennungen enthält.</p>
<p><strong>Wann das passiert:</strong> Ohne gespeicherten Kauf bleibt die Billing-Bibliothek inaktiv, bis du die Kaufseite öffnest oder einen Kauf wiederherstellst. Ist bereits ein Kauf gespeichert oder ein Kaufvorgang noch offen, wird die Bibliothek beim App-Start aktiviert, um den Kaufstatus mit Google Play abzugleichen (z. B. bei Erstattungen); sie bleibt dann für die laufende Sitzung aktiv und kann auch danach noch Daten senden. Eine Möglichkeit, diese Diagnoseübertragung abzuschalten, bietet die Bibliothek nicht. Wir selbst erhalten diese Diagnosedaten nicht.</p>
<p>Rechtsgrundlage ist die Erfüllung des Kaufvertrags bzw. vorvertraglicher Maßnahmen (Art. 6 Abs. 1 lit. b DSGVO) sowie unser berechtigtes Interesse an einer funktionierenden Kaufabwicklung (Art. 6 Abs. 1 lit. f DSGVO). Eine Übermittlung in die USA ist möglich; Google ist nach dem EU-US Data Privacy Framework zertifiziert.</p>
<p><strong>Google Play allgemein:</strong> Download, Installation und Updates erfolgen über Google Play; dabei verarbeitet Google Daten nach eigener Datenschutzerklärung.</p>'''),
 ('Diese Website', f'''<p>Die Website verwendet keine Cookies, keine Tracker, keine Analyse-Werkzeuge und lädt keine externen Skripte oder Schriften.</p>
<p><strong>Hosting:</strong> Die Website wird über GitHub Pages bereitgestellt (GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, USA). Beim Aufruf verarbeitet GitHub technisch notwendige Daten wie deine IP-Adresse, Datum und Uhrzeit sowie die aufgerufene Seite (Server-Logs), um die Website auszuliefern und abzusichern. Rechtsgrundlage ist unser berechtigtes Interesse an einer sicheren und zuverlässigen Bereitstellung (Art. 6 Abs. 1 lit. f DSGVO). Eine Übermittlung in die USA ist möglich; GitHub ist nach dem EU-US Data Privacy Framework zertifiziert. Details: {GHPRIV.format("Datenschutzerklärung von GitHub")}.</p>'''),
 ('Kontakt per E-Mail', '<p>Wenn du uns schreibst, verwenden wir deine E-Mail-Adresse und den Inhalt nur zur Beantwortung deiner Anfrage (Art. 6 Abs. 1 lit. b bzw. f DSGVO) und löschen sie, wenn sie dafür nicht mehr benötigt werden.</p>'),
 ('Deine Rechte', '<p>Du hast nach Art. 15–21 DSGVO das Recht auf Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Datenübertragbarkeit und Widerspruch. Außerdem kannst du dich bei einer Datenschutz-Aufsichtsbehörde beschweren (Art. 77 DSGVO), etwa beim Thüringer Landesbeauftragten für den Datenschutz und die Informationsfreiheit. Da die App keine Daten an uns übermittelt, liegen uns außer E-Mails keine Daten von dir vor. Für Daten, die Google verarbeitet, wende dich bitte an Google.</p>'),
]), 'document-page'))

write('en', 'privacy.html', page('en', 'privacy.html', 'Privacy policy – Cogwisp', 'Privacy policy for the Android app Cogwisp and this website.', doc('Privacy policy', 'Last updated: 31 October 2026', [
 ('In short', '<p>Cogwisp is an offline puzzle game with no account of its own, no server of its own, no ads and no tracking or analytics of its own. Your progress stays on your device. To buy the full game the app uses Google Play Billing; Google processes data in the process – including technical diagnostic data that the billing library sends to Google. This website sets no cookies and uses no trackers.</p>'),
 ('Controller', '<address>' + ADDR.format(country='Germany') + f'<br>Email: {MAIL}</address>'),
 ('The app “Cogwisp”: local data', '''<p><strong>No account, no server of our own:</strong> The app’s own code contains no network client and no advertising or analytics SDK. We do not receive any data about you from the app.</p>
<p><strong>Local storage:</strong> Progress, language setting and unfinished puzzles are stored only locally in the app’s storage on your device. The full-game unlock is also recorded locally; the app stores no payment data there. Android backup is disabled for the app.</p>
<p><strong>Permissions:</strong> The app requests no access to camera, microphone, contacts, storage, location, advertising ID or notifications. Declared are the Google Play billing permission and – through the included Google libraries – internet access and network state.</p>
<p><strong>Deleting:</strong> “Clear storage” in Android settings or uninstalling removes all local app data. This does not cancel a purchase and does not delete data already sent to Google. After reinstalling you can restore your purchase.</p>'''),
 ('Buying the full game via Google Play', f'''<p>The prologue is free. The full game is unlocked with a single in-app purchase through Google Play Billing. Google handles payment and the purchase; we receive no payment or card data. The app processes the product ID, purchase status and a purchase token to acknowledge the purchase with Google Play and store the unlock. Google processes purchase, payment and account data under its own responsibility according to the {GPRIV.format("Google Privacy Policy")}.</p>
<p><strong>Technical diagnostic data:</strong> The Google Play Billing library included in the app sends technical diagnostic data to Google (endpoint firebaselogging.googleapis.com). Observed fields include status or error messages of the billing function, app package name, app and library version, device model, manufacturer, OS version/build, language and country, time zone, network type and mobile country/network code (MCC/MNC). This data is first cached locally and sent when a connection is available. We were not able to decode every field of this transmission, so we cannot rule out that it contains further technical identifiers.</p>
<p><strong>When this happens:</strong> Without a saved purchase, the billing library stays inactive until you open the purchase page or restore a purchase. If a purchase is already saved or a purchase is still pending, the library is activated at app start to reconcile the purchase status with Google Play (e.g. for refunds); it then stays active for the session and may send data afterwards. The library offers no way to switch off this diagnostic transmission. We do not receive this diagnostic data ourselves.</p>
<p>The legal basis is the performance of the purchase contract or pre-contractual steps (Art. 6(1)(b) GDPR) and our legitimate interest in working purchase handling (Art. 6(1)(f) GDPR). Data may be transferred to the USA; Google is certified under the EU-US Data Privacy Framework.</p>
<p><strong>Google Play in general:</strong> Download, installation and updates take place through Google Play; Google processes data according to its own privacy policy.</p>'''),
 ('This website', f'''<p>This website uses no cookies, no trackers, no analytics tools and loads no external scripts or fonts.</p>
<p><strong>Hosting:</strong> The website is served via GitHub Pages (GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, USA). When you visit, GitHub processes technically necessary data such as your IP address, date and time and the requested page (server logs) to deliver and secure the website. The legal basis is our legitimate interest in secure and reliable delivery (Art. 6(1)(f) GDPR). Data may be transferred to the USA; GitHub is certified under the EU-US Data Privacy Framework. Details: {GHPRIV.format("GitHub Privacy Statement")}.</p>'''),
 ('Contacting us by email', '<p>If you write to us, we use your email address and the content only to answer your request (Art. 6(1)(b) or (f) GDPR) and delete them once they are no longer needed for that purpose.</p>'),
 ('Your rights', '<p>Under Art. 15–21 GDPR you have the right of access, rectification, erasure, restriction of processing, data portability and objection. You may also lodge a complaint with a data protection supervisory authority (Art. 77 GDPR), for example the Thuringian State Commissioner for Data Protection and Freedom of Information. Since the app sends no data to us, we hold no data about you apart from emails. For data processed by Google, please contact Google.</p>'),
]), 'document-page'))

# ---------- support ----------
SUP = {
 'de': ('Hilfe &amp; Support – Cogwisp', 'Kontakt und häufige Fragen zu Cogwisp.', 'Hilfe &amp; Support', [
  ('Kontakt', f'<p>Fragen, Fehler oder Ideen? Schreib an {MAIL}. Hilfreich sind Gerätemodell, Android-Version und – bei einem Rätsel – Kapitel und Raum.</p>'),
  ('Wo wird mein Fortschritt gespeichert?', '<p>Nur lokal auf deinem Gerät. Es gibt kein Konto und keine Cloud-Synchronisierung. Wenn du die App deinstallierst oder ihren Speicher löschst, ist der Fortschritt weg.</p>'),
  ('Wie stelle ich meinen Kauf wieder her?', '<p>Nach einer Neuinstallation oder auf einem anderen Gerät mit demselben Google-Konto öffnest du die Kaufseite in der App und wählst die Wiederherstellung. Dafür sind Google Play und eine Internetverbindung nötig. Ein bereits lokal gespeicherter Vollversionszugang funktioniert auch offline.</p>'),
  ('Wie ändere ich die Sprache?', '<p>Cogwisp gibt es auf Deutsch und Englisch. Die Sprache kannst du im Menü umschalten.</p>'),
  ('Was kostet Cogwisp?', '<p>Die sechs Prologräume sind kostenlos. Die 30 weiteren Räume schaltest du mit einem einmaligen In-App-Kauf frei. Kein Abonnement, keine Werbung.</p>'),
  ('Ich komme in einem Raum nicht weiter.', '<p>Jeder Raum hat drei gestufte Hinweise und eine gesondert aufrufbare Lösung. Einzelschritt und Probelauf zeigen dir, wie sich die Teile bewegen.</p>'),
 ]),
 'en': ('Help &amp; Support – Cogwisp', 'Contact and frequently asked questions about Cogwisp.', 'Help &amp; Support', [
  ('Contact', f'<p>Questions, bugs or ideas? Write to {MAIL}. Device model, Android version and – for a puzzle – chapter and room are helpful.</p>'),
  ('Where is my progress saved?', '<p>Only locally on your device. There is no account and no cloud sync. If you uninstall the app or clear its storage, your progress is gone.</p>'),
  ('How do I restore my purchase?', '<p>After reinstalling, or on another device with the same Google account, open the purchase page in the app and choose restore. This requires Google Play and an internet connection. A full-game unlock already saved locally also works offline.</p>'),
  ('How do I change the language?', '<p>Cogwisp is available in English and German. You can switch the language in the menu.</p>'),
  ('What does Cogwisp cost?', '<p>The six prologue rooms are free. Unlock the 30 further rooms with a single in-app purchase. No subscription, no ads.</p>'),
  ('I am stuck in a room.', '<p>Each room has three progressive hints and a separately available solution. Step-through and Test run show how the parts move.</p>'),
 ]),
}
for lang, (title, desc, h1, secs) in SUP.items():
    write(lang, 'support.html', page(lang, 'support.html', title, desc, doc(h1, '', secs), 'document-page'))

# ---------- 404 (root, absolute-ish links via base path) ----------
nf = page('de', '404.html', 'Seite nicht gefunden – Cogwisp', 'Diese Seite gibt es nicht.', doc('Seite nicht gefunden', 'Page not found', [
 ('Hier läuft kein Zahnrad', '<p>Diese Seite gibt es nicht. <a href="./">Zur Startseite</a></p><p lang="en">This page does not exist. <a href="en/">Go to the English home page</a></p>')]), 'document-page')
# 404 can be served from any path: use base element
nf = nf.replace('href="en/404.html"', 'href="en/"').replace('<meta charset="utf-8">', '<meta charset="utf-8">\n<base href="/Cogwisp/">\n<meta name="robots" content="noindex">')
open(os.path.join(ROOT, '404.html'), 'w').write(nf)

# ---------- sitemap / robots ----------
urls = [u for n in ['', 'support.html', 'privacy.html', 'impressum.html'] for u in (BASE + n, BASE + 'en/' + n)]
open(os.path.join(ROOT, 'sitemap.xml'), 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'<url><loc>{u}</loc><lastmod>2026-10-31</lastmod></url>\n' for u in urls) + '</urlset>\n')
open(os.path.join(ROOT, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n')
open(os.path.join(ROOT, '.nojekyll'), 'w').write('')
