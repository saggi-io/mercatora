# Mercatora · Sprint 0 / Release 0

Stand: 15. November 2026. Entwurf zur Abnahme, nicht live veröffentlicht.

## Ergebnis

Bestehende statische Website im verifizierten Repository `saggi-io/mercatora` überarbeitet. B2B-Fokus: Kleingewerbe, Selbstständige, Mittelstand und Vereine. Leistungen: KI-Lösungen, App-Entwicklung, Automatisierung, Projektplanung und Umsetzung. Keine beworbene Website-Optimierung, kein Titel „KI-Ingenieur“, keine Bewertungen, Erfolgskennzahlen oder erfundenen Preise.

Die Projekte BDKNG, Kinnicher FFC und Kabine sind als kommende Projektvorstellungen enthalten. Es wird keine konkrete Leistung als fertig dargestellt. Die Seite kann nach Freigabe auch in diesem zurückhaltenden Zustand starten; ausführliche Fallstudien sind kein technischer Release-Blocker.

Handel und Whiskybereich bleiben erreichbar. Die bisherige Google-Flaschenliste bleibt unverändert verlinkt. Beispielpreise, unbelegte Flaschenzahl und vorgetäuschte Kauf-/Freigabefunktionen wurden entfernt. Google-Inhalte werden erst nach einem bewussten Linkaufruf geladen.

## Nachgewiesener Bestand

- Repository: https://github.com/saggi-io/mercatora
- Ausgangscommit: `1eb05bcca569be34be80d3785d8776f3cdf33708`
- Getrennter lokaler Branch: `release/0-2026-11-15`
- `CNAME` enthält `www.mercatora.eu`; `www` verweist per DNS auf `saggi-io.github.io`.
- Live-Startseite liefert HTTP 200 mit `Server: GitHub.com`; Struktur und Inhalte stimmen mit dem Repository überein.
- HTTP sowie HTTPS ohne „www“ liefern eine 301-Weiterleitung auf `https://www.mercatora.eu/`, danach HTTP 200. Zertifikatsprüfung beim Abruf erfolgreich; kein unsicherer Abruf verwendet.
- Statisches HTML/CSS; kein Anwendungsserver, kein Shop-Backend, kein funktionierender Formularserver im Bestand.
- Öffentliche Pages-Konfigurations-API liefert 404; konkrete Deployment-Einstellungen und Schreibzugriff wurden damit nicht bestätigt. Vor Merge/Veröffentlichung Pages-Quellbranch im GitHub-Konto prüfen.
- Erste Repository-Listen beider Kontoverbindungen zeigten Mercatora nicht. Erst die gezielte Suche nach `user:saggi-io` fand das passende Repository. Keine Zuordnung zu „one“ oder „spieltag-app“ vorgenommen.
- Mail-Domain besitzt IONOS-MX-Einträge. Das belegt keinen Empfang eines bestimmten Postfachs.
- Das genannte Arbeitsbriefing unter `/mnt/data/…` war nicht vorhanden. Die referenzierte Unterhaltung wurde gelesen; ihre alten Assistentenantworten waren nur als Inhaltsverweise verfügbar. Basis ist deshalb das vollständige Briefing der aktuellen Anfrage.

## Vorschau und Dateien

- `mercatora-release-0/index.html`: direkt lokal öffnen; alle Hauptseiten funktionieren ohne JavaScript.
- `Mercatora-Desktop.png` und `Mercatora-Mobil.png`: vollständige visuelle Vorschauen.
- `Mercatora-Release-0.zip`: Website und lokale Schriften, ohne Git-Historie oder Zugangsdaten. Zum lokalen Testen entpacken, `Vorschau-starten.cmd` starten und im Browser `http://127.0.0.1:8766` öffnen. Zum Beenden das Konsolenfenster schließen.
- `Mercatora-Bestand-vor-Release-0.zip`: teilbares Backup der ursprünglichen Website-Dateien. Historie, sensible Altdatei und nicht benötigte alte ZIP-/PDF-Dateien sind bewusst ausgeschlossen.
- Vollständiges Git-Bundle und Live-HTML/HTTP-Belege liegen ausschließlich im Arbeitsverzeichnis `work/`. Das Bundle enthält sensible historische Altbestände und darf nicht veröffentlicht oder als Website hochgeladen werden.

## Gestaltung für Website und Canva

| Element | Vorgabe |
|---|---|
| Hauptfarbe / Flächen | Navy `#112338` |
| Links / Hervorhebungen auf hell | Petrol `#0B7776` |
| CTA / Akzent auf Navy | Mint `#45D9CE` mit Navy-Schrift |
| Dezenter Schmuckakzent | Bronze `#C89B55` |
| Heller Hintergrund | Off-White `#F5F7F8` |
| Überschriften | Manrope, meist 650 |
| Fließtext | Inter, 400–700 |
| Stil | Ruhig, großzügige Abstände, klare Linien, sparsame Rundungen |

Beide Schriften sind lokal eingebunden; Lizenztexte liegen bei. Die Farb- und Schriftvorgaben lassen sich direkt in Canva übernehmen. Ein vorhandenes Canva-Brand-Kit war nicht benannt und wurde nicht verändert oder als geprüft ausgegeben. Der bestehende Bildbestand und das Favicon bleiben erhalten; im Seitenkopf steht eine schlichte typografische M-Marke mit Wortmarke.

## Prüfungen

| Prüfung | Ergebnis / Grenze |
|---|---|
| Smartphone, Tablet, Desktop | Browserprüfung bei 320, 390, 768, 1024, 1440 px; kein horizontaler Überlauf |
| Hauptseiten und Assets | HTTP 200 lokal; Seiten, CSS, Favicon und WOFF2-Dateien vorhanden |
| Verlinkungen | Alle internen Dateien und Anker geprüft; Kontakt- und Datenschutznavigation sowie Wechsel zum Whiskybereich im Browser getestet |
| Struktur | Deutsch als Seitensprache, je eine H1, eindeutige IDs, beschriftete Navigation |
| Tastatur | Sichtbarer Fokus und „Zum Inhalt“-Link im Browser geprüft; Navigation ohne verstecktes Skriptmenü |
| Mobile Bedienung | Navigationslinks mit mindestens 44 px Höhe; Lesereihenfolge und einspaltiges Layout |
| Schriften | Dateien besitzen gültige WOFF2-Kennung, beide Schriftfamilien im Browser verfügbar |
| SEO | Titel, Beschreibungen, kanonische Startseitenadresse, robots.txt, gültige XML-Sitemap |
| Basisabsicherung | Keine Formulareingaben, kein JavaScript, kein Tracking, keine automatischen Drittanbieter-Einbettungen; restriktive Meta-CSP und Referrer-Vorgabe |
| Browserkonsole | Bei den geprüften lokalen Seiten keine Warnungen/Fehler gemeldet |
| Kontakt | E-Mail- und Telefonlinks korrekt; tatsächlicher Versand/Empfang und Telefonannahme nicht getestet |
| Externe Links | Bestehende Google-Listenadresse übernommen; Freigaben und Inhalt der Liste nicht verändert oder als geprüft dargestellt |
| Rechtstexte | Bestandsangaben übernommen; § 5 TMG auf § 5 DDG aktualisiert; Datenschutzhinweise an lokalen Schriftbezug und Link statt Google-Einbettung angepasst |

Die Prüfungen sind eine Basisprüfung, kein vollständiges Barrierefreiheits-, Rechts- oder Sicherheitsaudit. GitHub Pages erlaubt nicht alle zusätzlichen HTTP-Sicherheitsheader über Website-Dateien. Insbesondere ist eine Meta-CSP kein Ersatz für einen serverseitigen `frame-ancestors`-Header. Es wurde keine Serverkonfiguration verändert.

## Kurze Freigabe-Checkliste

- [ ] Gestaltung und B2B-Texte freigeben.
- [ ] `kontakt@mercatora.eu` sowie `info@mercatora.eu` auf tatsächlichen Empfang prüfen; eine eigene Testmail senden und Eingang bestätigen.
- [ ] Felix Sagmeister, Bleichstraße 10, 64732 Bad König, Telefon 06063 2090, Fax und Kleinunternehmerangabe im Impressum bestätigen bzw. korrigieren.
- [ ] Datenschutzhinweise insbesondere zu Hosting, internationaler Übermittlung und tatsächlicher Kontaktverarbeitung abschließend prüfen.
- [ ] Projektvorstellungen vorerst ohne Leistungsnachweis freigeben oder pro Projekt die tatsächlich abgeschlossene Leistung nennen.
- [ ] Sicherheitsfund behandeln: Im öffentlichen Bestand lag eine Datei mit 2FA-Backup-Codes. Sie ist aus dem Release-Baum entfernt, bleibt aber in der bisherigen öffentlichen Historie. Codes beim Anbieter erneuern, danach historische Entfernung und gegebenenfalls weitere Bereinigung planen. Keine Codes in die Freigabeantwort kopieren.
- [ ] Pages-Konfiguration und Veröffentlichungsweg im zugehörigen GitHub-Konto bestätigen; danach ausdrücklich den Live-Publish dieses Entwurfs freigeben.

Die Live-Seite, der Hauptbranch und BDKNG wurden nicht verändert. Nach Freigabe: genau diesen Release-Stand übernehmen, Deployment prüfen, HTTPS-Startseite und Unterseiten erneut testen. BDKNG kann dann auf `https://mercatora.eu/` verlinken; die vorhandene Weiterleitung führt zur kanonischen www-Adresse. Ein Rollback erfolgt über einen neuen Wiederherstellungscommit der Website-Dateien; die sensible Altdatei darf dabei nicht zurückkehren.

## Scrum: kleiner Umfang, klarer Abschluss

| Etappe | Ziel | Abnahme |
|---|---|---|
| Sprint 0 · Vorbereitung | Bestand verstehen, sichern, Zugang und Risiken erfassen | Repositorybeleg, Backup, separater Branch |
| Release 0 · heutiger Umfang | Seriöse B2B-Startseite als Ziel des BDKNG-Footerlinks | Vorschau, Basistests, Kontakt-/Rechtsprüfung, ausdrückliche Live-Freigabe |
| Nächster kleiner Sprint | Verifizierte Projektvorstellungen ergänzen | Konkrete Leistungen und Bilder vom Inhaber bestätigt |
| Separater Folgepunkt | 1–3 eBay-Artikel vorbereiten | Artikel, Zustand, Preis und Verkaufsbedingungen einzeln klären; blockiert Release 0 nicht |

Der Inhaber priorisiert und nimmt ab; Umsetzung und Tests werden pro Etappe dokumentiert. Keine Shop-, Social-Account- oder Inbox-Entwicklung in diesem Release.

## Quellen

- Bestand: https://www.mercatora.eu/ und https://github.com/saggi-io/mercatora
- Anbieterkennzeichnung: https://www.gesetze-im-internet.de/ddg/__5.html
- GitHub Pages / HTTPS: https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https
- GitHub Datenschutz: https://docs.github.com/de/site-policy/privacy-policies/github-general-privacy-statement
