# Mercatora: zweite Prüfung von Rechtstexten, SEO und Sicherheit

Stand: 15. November 2026. Geprüft wurden der Release-Entwurf und öffentlich abrufbare Antworten der bisherigen Live-Seite. Keine Live-Veröffentlichung, keine DNS-Änderung, keine Angriffs- oder Lasttests.

## Ergebnis und Änderungen

Der untere Abschnitt „Weitere Bereiche“ ist vollständig entfernt. Handel und Whisky werden auf der Hauptseite auch im Footer nicht mehr beworben. Die vorhandene Datei `sdk.html` bleibt erhalten und wird nicht gelöscht. Das echte Logo ist weiterhin eingebunden.

Impressum und Datenschutz wurden nochmals überarbeitet. Die Anbieterangaben enthalten den bestätigten Namen, die bestätigte Anschrift, Telefonnummer und `info@mercatora.eu`. Die unbestätigte, freiwillige Faxangabe wurde entfernt. Die Kleinunternehmerregelung wurde nach Rückmeldung des Inhabers mit der richtigen Vorschrift § 19 UStG benannt. Die Unternehmereigenschaft und die Anwendung dieser Regelung wurden nicht steuerlich geprüft.

**Noch zwingend zu klären:** Ob und welche USt-IdNr. oder W-IdNr. zugeteilt wurde. Eine solche Nummer gehört bei Vorhandensein gemäß § 5 Abs. 1 Nr. 6 DDG ins Impressum – auch bei Kleinunternehmern. Keine persönliche Steuer-ID oder normale Steuernummer veröffentlichen. Im Entwurf steht keine erfundene Nummer.

IONOS wurde vom Inhaber als direkt genutzter E-Mail-Anbieter bestätigt und in den Datenschutzhinweisen ergänzt. Sprachnachrichten über die FRITZ!Box werden ebenfalls beschrieben. Ausschließlich lokale Speicherung wird nicht behauptet: Der Inhaber hat den Versand der AB-Nachrichten per E-Mail über IONOS bestätigt; dies wurde in den Datenschutzhinweisen ausdrücklich ergänzt. Der IONOS-Vertrag zur Auftragsverarbeitung und eventuelle zusätzliche Mail-/Telefonverarbeitung wurden nicht im Kundenkonto geprüft.

Die Datenschutzhinweise behandeln Verantwortlichkeit, Hosting, Kontaktzwecke, Rechtsgrundlagen, Löschkriterien, Betroffenenrechte, Beschwerdemöglichkeit, freiwillige Datenangaben sowie das Fehlen einer automatisierten Entscheidung durch die Website. GitHub weist auf internationale Übermittlungen hin; die Erklärung nennt hierfür die vom Anbieter beschriebenen Mechanismen. Eine feste Aufbewahrungsfrist für Pages-IP-Protokolle wurde nicht erfunden. Der separate Whiskybereich verlinkt Google erst nach einem bewussten Klick; es gibt keine automatische Einbettung.

## Suchmaschinen

| Punkt | Bisher live | Release-Entwurf |
|---|---|---|
| HTTPS-Startseite | HTTP 200 | HTML ohne JavaScript lesbar |
| HTTP / Domain ohne www | Zuvor geprüfte 301-Weiterleitung auf HTTPS-www | Kanonische Adresse bleibt gleich |
| Googlebot-/Bingbot-Kennung | Je HTTP 200 bei normalem Abruf mit entsprechender User-Agent-Kennung | Keine Crawler-Sperre vorbereitet |
| robots.txt | HTTP 404 | Vorhanden; erlaubt Abruf und verweist auf Sitemap |
| sitemap.xml | HTTP 404 | Gültige XML-Sitemap mit Startseite, SDK und Rechtstexten |
| Canonicals | Nicht umfassend im Bestand vorhanden | Pro Inhaltsseite auf die passende HTTPS-www-Adresse gesetzt |
| Titel / Beschreibung / Sprache | Bestand | Individuelle Titel und Beschreibungen, Deutsch, eine H1 pro Seite |
| Fehlerseiten | Unbekannte Test-URL liefert echtes HTTP 404 | Eigene 404-Vorlage mit noindex vorbereitet |
| Geteilte Startseite | Bestand | Open-Graph-Titel, Beschreibung und URL ohne erfundene Unternehmensdaten |

Ein fehlendes robots.txt bedeutet nicht automatisch eine Crawling-Sperre. Auch eine gültige Sitemap garantiert keine Indexierung. Die Stichprobe `site:mercatora.eu` im verfügbaren Suchdienst lieferte keine Ergebnisse; daraus lässt sich keine verbindliche Aussage über den Google- oder Bing-Index ableiten. Ein User-Agent-Test ist kein Nachweis eines echten Googlebot-Besuchs. Eine Search-Console-/Bing-Webmaster-Verifizierung und Indexprüfung wurden mangels Kontozugriff nicht durchgeführt.

Nach der genehmigten Veröffentlichung müssen robots.txt, Sitemap, Canonicals und Statuscodes erneut auf der echten Domain geprüft werden. Die lokale Vorschau unter 127.0.0.1 ist nicht öffentlich indexierbar.

## Domain und Subdomains

`www.mercatora.eu` ist die vorhandene Hauptdomain im CNAME und wird weiter verwendet. Die bekannte gewünschte Subdomain `sdk.mercatora.eu` liefert aktuell **NXDOMAIN**, also keinen vorhandenen DNS-Namen. Sie wurde nicht von diesem Release entfernt. Die separate Seite `/sdk.html` existiert weiterhin; das ist technisch keine Subdomain.

Für `sdk.mercatora.eu` wären später eine gezielte DNS-Konfiguration, eine zugeordnete HTTPS-Veröffentlichung und die passende Weiterleitung bzw. eigene Auslieferung erforderlich. Ein CNAME auf GitHub allein genügt nicht für eine sichere, korrekt zugeordnete Website. Keine Wildcard-DNS-Einträge anlegen. Andere, nicht benannte Subdomains wurden nicht pauschal aufgelistet oder geprüft.

## Sicherheit für Betreiber und Besucher

Der Entwurf ist eine statische Website ohne JavaScript, Formulare, Uploads, Login, Zahlungsabwicklung, Datenbank oder API. Es gibt damit keine entsprechenden öffentlich angebotenen Eingabe- oder Ausführungsfunktionen. Das senkt die Angriffsfläche, beweist aber keine vollständige Sicherheit.

Die Content-Security-Policy wurde verschärft: Standardzugriffe sind gesperrt, Skripte, Formulare, Einbettungen, Worker und Verbindungsaufrufe ausdrücklich verboten. Bilder, CSS und Schriften dürfen nur aus derselben Herkunft geladen werden. Es gibt keine Inline-Ereignisbehandler oder extern automatisch geladenen Ressourcen im geprüften HTML. Referrer-Weitergabe ist begrenzt. Links zu E-Mail-Programmen senden nichts automatisch; die Seite bietet keinen Nachrichten-Relay für Dritte.

Der neue lokale Build `scripts/build-site.py` kopiert ausschließlich festgelegte Website-Dateien und benötigte Assets nach `_site`. Berichte, Skripte, Archive, Git-Historie und alte Zugangsdaten gehören nicht zum Ausgabeordner. Der Build lädt keine Pakete oder fremden Programme. Die laufende Vorschau wird jetzt aus diesem Ausgabeordner ausgeliefert. Normale lokale Abrufe auf `/.git/HEAD`, `/RELEASE-0.md`, `/scripts/build-site.py` und die bekannte sensible Altdatei liefern dort jeweils 404. Dies sind lokale Dateiausschlussprüfungen, keine Angriffstests auf Live-Systeme.

**Wichtig für die spätere Veröffentlichung:** Nur `_site` veröffentlichen. Bei einem bestehenden GitHub-Pages-Modus, der den Root des Hauptbranches ausliefert, muss der Veröffentlichungsweg vorher auf ein geprüftes Artefakt umgestellt werden. Der Build allein ändert den Hosting-Modus nicht. Nicht einfach den Branch mergen und damit den bisherigen Root-Modus als abgesichert ansehen.

### Offene Sicherheitsmaßnahmen

1. **Sensible Altdatei:** Die Datei mit dem Namen von 2FA-Backup-Codes ist im Release entfernt, bleibt jedoch in der bisherigen öffentlichen Historie vorhanden. Betroffene noch gültige Codes beim Anbieter erneuern; danach die historische Bereinigung planen. Ein Löschen in einem neuen Commit macht bereits veröffentlichte Zugangsdaten nicht wieder geheim. Es wurde keine Kontosperrung oder Historienumschreibung durchgeführt.
2. **Domainübernahme vorbeugen:** Für `_github-pages-challenge-saggi-io.mercatora.eu` wurde kein TXT-Eintrag gefunden. Das ist kein vollständiger Nachweis fehlender GitHub-Domainverifizierung, die Verifizierung ist aber nicht belegt. Im richtigen GitHub-Konto prüfen und gegebenenfalls mit dem von GitHub vorgegebenen Wert einrichten; keine erfundenen TXT-Werte verwenden.
3. **Hosting-Schutzheader:** In der geprüften Live-Startseitenantwort fehlen HSTS, HTTP-CSP, X-Content-Type-Options, X-Frame-Options bzw. frame-ancestors, Permissions-Policy und ein Referrer-Policy-HTTP-Header. Der Entwurf enthält CSP und Referrer-Regel als Meta-Angaben. Meta-CSP schützt nicht gegen Einbettung durch fremde Seiten mittels frame-ancestors; HSTS, nosniff und Permissions-Policy lassen sich damit ebenfalls nicht nachrüsten. Der Veröffentlichungsweg muss diese Anforderungen berücksichtigen. Eine unberücksichtigte `_headers`- oder `.htaccess`-Datei wurde nicht als Schutz ausgegeben. Kein HSTS mit includeSubDomains vor ungeprüfter Subdomain-/HTTPS-Konfiguration einschalten.
4. **Kontoschutz:** 2FA, sichere Wiederherstellung, minimale Schreibrechte, Schutz des Hauptbranches und Domainregistrar-/Mailkontozugang prüfen. Die Kontoeinstellungen sind hier nicht vollständig eingesehen. Es wurden keine neuen Berechtigungen erteilt.
5. **E-Mail-Spoofing:** SPF ist vorhanden; `_dmarc.mercatora.eu` verweist auf IONOS mit `p=none`. Das ist eine beobachtende DMARC-Richtlinie und keine Anweisung zur Zurückweisung gefälschter Nachrichten. Vor einer Verschärfung müssen alle legitimen Absender sowie DKIM und Weiterleitungen geprüft werden. Keine Mail-DNS-Einstellungen wurden verändert.
6. **Betrieb und Ausfälle:** Backup und getrennte Versionshistorie sind vorhanden. DDoS-Abwehr, Verfügbarkeit und die Sicherheit der Hostingplattform wurden nicht mit Last- oder Angriffstests geprüft und können durch statische Seitenänderungen nicht garantiert werden.

## Abnahmegrenze

Die Website wurde technisch und inhaltlich anhand des bekannten Sachstands geprüft. Eine Aussage „rechtssicher und gegen alle Angriffe geschützt“ wäre nicht belegt. Vor Live-Freigabe bleiben insbesondere die nachzureichende USt-ID, Auftragsverarbeitung, Domainverifizierung, Erneuerung betroffener Codes und die Auswahl des tatsächlichen Veröffentlichungswegs offen. Keine andere Website, kein anderer Server und keine Domainkonfiguration wurden geändert.

## Primärquellen

- § 5 DDG: https://www.gesetze-im-internet.de/ddg/__5.html
- § 19 UStG: https://www.gesetze-im-internet.de/ustg_1980/__19.html
- GitHub Pages und IP-Protokollierung: https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages
- GitHub Datenschutz: https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement
- GitHub Domainverifizierung: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages
- IONOS Anbieterangaben: https://www.ionos.de/impressum?lang=de
- IONOS Datenschutz und AVV: https://www.ionos.de/hilfe/datenschutz/
- Google robots.txt: https://developers.google.com/search/docs/crawling-indexing/robots/intro
- Google Canonicals: https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls
- OWASP HTTP-Schutzheader: https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html
- CSP: https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy

Nachtrag: Der Inhaber reicht die VAT-/USt-ID nach. Bis dahin bleibt sie im Impressum ohne Platzhalternummer offen. Die AB-Weiterleitung über IONOS wurde bestätigt.
