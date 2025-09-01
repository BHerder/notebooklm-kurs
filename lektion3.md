# Lektion 3: Mit Quellen arbeiten: Hinzufügen und Verwalten deiner Forschungsmaterialien

**Lernziele:**

*   Die verschiedenen Arten von Quellen kennenlernen, die du in NotebookLM verwenden kannst.
*   Dokumente vom eigenen Computer hochladen.
*   Dateien direkt aus Google Drive importieren.
*   Texte von Webseiten oder aus anderen Quellen kopieren und einfügen.
*   Quellen umbenennen, löschen und gezielt für die Analyse auswählen.

---

## Einführung: Futter für deinen KI-Assistenten

Herzlich willkommen zur dritten Lektion! Nachdem wir uns mit der Benutzeroberfläche von NotebookLM vertraut gemacht haben, kommen wir nun zum Herzstück jeder Recherche: den Quellen. Ein Forschungsassistent ist nur so gut wie die Informationen, die man ihm gibt. In dieser Lektion lernst du alles, was du wissen musst, um dein Notebook mit den notwendigen Materialien zu „füttern“.

Wir werden die verschiedenen Wege erkunden, auf denen du deine Dokumente, Artikel und Notizen in NotebookLM importieren kannst. Ob sie als PDF auf deinem Computer liegen, in deiner Google Drive-Cloud gespeichert sind oder du einfach nur einen Textabschnitt von einer Webseite verwenden möchtest – NotebookLM bietet für jeden Fall eine einfache Lösung. Außerdem zeigen wir dir, wie du deine Quellen nach dem Import verwalten kannst, um stets den Überblick zu behalten. Am Ende dieser Lektion wirst du in der Lage sein, ein Notebook vollständig mit relevanten Materialien zu bestücken und es für die Analyse mit dem KI-Assistenten vorzubereiten.

Lass uns also die Tore öffnen und die Informationen hereinlassen!

---

## Welche Arten von Quellen kann ich verwenden?

NotebookLM ist flexibel und unterstützt eine Vielzahl von gängigen Formaten. Die Entwickler arbeiten ständig daran, weitere Formate hinzuzufügen, aber zum jetzigen Zeitpunkt kannst du hauptsächlich mit textbasierten Quellen arbeiten.

**Unterstützte Quellenarten:**

*   **PDF-Dateien (.pdf):** Ideal für wissenschaftliche Artikel, Berichte, E-Books und gescannte Dokumente.
*   **Textdateien (.txt):** Einfache Textdateien ohne Formatierung.
*   **Google Docs:** Dokumente, die in deinem Google Drive gespeichert sind. Dies ist eine der nahtlosesten Integrationsmöglichkeiten.
*   **Kopierter Text:** Du kannst Text aus jeder beliebigen Quelle (z. B. Webseiten, E-Mails) kopieren und direkt als neue Quelle in NotebookLM einfügen.
*   **Webseiten-Links (in Entwicklung):** Google arbeitet daran, das direkte Einfügen von URLs zu ermöglichen, um den Inhalt von Webseiten automatisch zu importieren. Zum Zeitpunkt der Erstellung dieses Kurses ist das Kopieren und Einfügen des Textes jedoch der zuverlässigste Weg.

<div class="callout-box">
    **Wichtiger Hinweis zu Bildern und Tabellen:** NotebookLM ist primär auf die Verarbeitung von Text spezialisiert. Während es Text aus PDFs extrahieren kann (auch aus gescannten Dokumenten mittels OCR – Optical Character Recognition), kann es den *Inhalt* von Bildern, Diagrammen oder komplexen Tabellen nicht interpretieren. Es liest den Text, aber es „sieht“ nicht die visuellen Elemente.
</div>

---

## Schritt-für-Schritt: Quellen zu deinem Notebook hinzufügen

Öffne eines deiner Notebooks. Im Quellenbereich auf der linken Seite siehst du den prominenten Button **„+ Quelle hinzufügen“** („+ Add Source“). Ein Klick darauf öffnet ein Menü mit den folgenden Optionen:

### Option 1: Von Google Drive importieren

Dies ist die empfohlene Methode, wenn du bereits Google Drive nutzt.

1.  Klicke auf **„+ Quelle hinzufügen“** und wähle **„Google Drive“**.
2.  Es öffnet sich ein Fenster, das dir eine Ansicht deines Google Drive-Kontos zeigt. Du kannst hier durch deine Ordner navigieren oder die Suchfunktion nutzen, um eine bestimmte Datei zu finden.
3.  Wähle eine oder mehrere Dateien aus (du kannst mehrere Dokumente gleichzeitig importieren, indem du die `Strg`- oder `Cmd`-Taste gedrückt hältst).
4.  Klicke auf **„Einfügen“** („Insert“) oder **„Auswählen“** („Select“).
5.  NotebookLM beginnt sofort mit der Verarbeitung der Dokumente. Je nach Größe kann dies einige Sekunden dauern. Sobald der Prozess abgeschlossen ist, erscheint die Datei in deiner Quellenliste.

### Option 2: Vom Computer hochladen

Verwende diese Option für Dateien, die lokal auf deiner Festplatte gespeichert sind.

1.  Klicke auf **„+ Quelle hinzufügen“** und wähle **„Hochladen“** („Upload file“).
2.  Es öffnet sich der Dateiauswahldialog deines Betriebssystems (Windows Explorer oder Mac Finder).
3.  Navigiere zum Speicherort der Datei, wähle sie aus und klicke auf **„Öffnen“**.
4.  Genau wie beim Drive-Import wird die Datei verarbeitet und anschließend in deiner Quellenliste angezeigt.

### Option 3: Text kopieren und einfügen

Dies ist die flexibelste Methode und perfekt für Inhalte von Webseiten oder aus anderen Anwendungen.

1.  Markiere den gewünschten Text in deiner ursprünglichen Quelle (z. B. auf einer Nachrichtenseite oder in einer E-Mail) und kopiere ihn in die Zwischenablage (`Strg+C` oder `Cmd+C`).
2.  Klicke in NotebookLM auf **„+ Quelle hinzufügen“** und wähle **„Text kopieren“** („Copied text“).
3.  Es erscheint ein Textfeld. Füge den kopierten Text hier ein (`Strg+V` oder `Cmd+V`).
4.  Klicke auf **„Einfügen“** („Insert“).
5.  Der eingefügte Text wird nun als neue, eigenständige Quelle behandelt. Standardmäßig erhält sie einen Namen wie „Kopierter Text 1“. Es ist sehr empfehlenswert, diese Quelle sofort umzubenennen (siehe nächster Abschnitt), damit du weißt, woher der Text stammt.

<div class="callout-box">
    **Praxis-Tipp:** Wenn du einen langen Online-Artikel verwendest, kopiere nicht nur den Text, sondern füge am Anfang oder Ende des eingefügten Textes auch den Link zur Original-URL hinzu. So kannst du später leicht zur Originalquelle zurückkehren.
</div>

---

## Deine Quellen verwalten

Nachdem du einige Quellen hinzugefügt hast, wird deine Quellenliste schnell wachsen. Ein gutes Management ist entscheidend, um den Überblick zu behalten.

### Quellen umbenennen

Dateinamen wie `final_draft_v3_notes.pdf` oder `Kopierter Text 2` sind nicht sehr aussagekräftig. Gib deinen Quellen klare, verständliche Namen.

1.  Bewege den Mauszeiger über die Quelle, die du umbenennen möchtest.
2.  Klicke auf die drei kleinen Punkte, die rechts neben dem Namen erscheinen.
3.  Wähle im Menü **„Umbenennen“** („Rename“).
4.  Gib den neuen Namen ein und drücke die Eingabetaste.

**Beispiel:** Benenne `Kopierter Text 2` um in `Artikel: Auswirkungen von KI auf den Arbeitsmarkt (NYT, 2023)`.

### Quellen löschen

Wenn eine Quelle nicht mehr relevant ist oder du sie versehentlich hinzugefügt hast, kannst du sie einfach entfernen.

1.  Bewege den Mauszeiger über die Quelle.
2.  Klicke auf die drei kleinen Punkte.
3.  Wähle **„Löschen“** („Delete“).
4.  Bestätige die Sicherheitsabfrage. Achtung: Dieser Vorgang kann nicht rückgängig gemacht werden!

### Quellen für die Analyse auswählen (Fokussieren)

Dies ist eine der leistungsstärksten, aber oft übersehenen Funktionen. Standardmäßig durchsucht der KI-Assistent **alle** Quellen in deinem Notebook, wenn du eine Frage stellst. Manchmal möchtest du dich aber nur auf ein oder zwei Dokumente konzentrieren.

*   Neben jeder Quelle in der Liste befindet sich ein **Kontrollkästchen**. 
*   Um die KI auf bestimmte Quellen zu beschränken, **entferne die Häkchen** bei allen Quellen, die du ignorieren möchtest.
*   Wenn du nur eine einzige Quelle analysieren willst, klicke auf das Kästchen neben dieser Quelle und wähle die Option **„Nur diese auswählen“** („Select only“), die eventuell erscheint, oder deaktiviere alle anderen manuell.

Diese Funktion ist extrem nützlich, um die Antworten der KI präziser zu machen und Verwirrung durch zu viele Informationen zu vermeiden.

---

## Übungsaufgabe

1.  **Finde drei verschiedene Quellen:** Suche einen kurzen Online-Artikel zu einem Thema, das dich interessiert, lade einen relevanten wissenschaftlichen Artikel als PDF herunter (z. B. von Google Scholar) und erstelle ein kurzes Google Doc mit eigenen Notizen zum selben Thema.
2.  **Bestücke dein Test-Notebook:** Gehe zu deinem „Mein erster Test“-Notebook.
    *   Füge das Google Doc über die **Google Drive**-Option hinzu.
    *   Lade die **PDF-Datei** von deinem Computer hoch.
    *   Kopiere den Text des **Online-Artikels** und füge ihn als neue Quelle ein.
3.  **Organisiere deine Quellen:**
    *   Benenne die kopierte Textquelle so um, dass sie den Titel des Artikels und die Quelle enthält.
    *   Benenne die PDF- und Google-Doc-Quellen bei Bedarf ebenfalls um, um ihre Namen zu verdeutlichen.
4.  **Fokussiere deine Analyse:** Wähle nur die PDF-Quelle aus, indem du die Häkchen bei den anderen beiden Quellen entfernst.

---

## Zusammenfassung der wichtigsten Erkenntnisse

*   NotebookLM unterstützt **PDFs, Textdateien, Google Docs und kopierten Text**.
*   Quellen können aus **Google Drive**, vom **Computer** oder durch **Kopieren und Einfügen** hinzugefügt werden.
*   Eine gute **Benennung** deiner Quellen ist entscheidend für die Übersichtlichkeit.
*   Du kannst gezielt **Quellen auswählen oder abwählen**, um die Analyse des KI-Assistenten zu steuern.

---

## Fragen zum Verständnis

1.  Welche drei Hauptmethoden gibt es, um Quellen in NotebookLM zu importieren?
2.  Warum ist es wichtig, Quellen, die durch Kopieren und Einfügen erstellt wurden, sofort umzubenennen?
3.  Beschreibe ein Szenario, in dem es sinnvoll wäre, die Analyse auf eine einzige Quelle zu beschränken.
4.  Kann NotebookLM den Inhalt eines Fotos analysieren, das in einem PDF-Dokument enthalten ist? Begründe deine Antwort.

---

**Navigation:**
[← Zurück zu Lektion 2: Die Benutzeroberfläche verstehen](lektion2.html)
[Zur nächsten Lektion: Den KI-Assistenten nutzen →](lektion4.html)


