import os

# Lesson data
lessons = [
    {
        "num": 2,
        "title": "Die Benutzeroberfläche verstehen",
        "subtitle": "Navigation und wichtige Funktionen erklärt",
        "description": "Meistere die Navigation und verstehe alle wichtigen Funktionen der NotebookLM-Oberfläche.",
        "progress": 28.6
    },
    {
        "num": 3,
        "title": "Mit Quellen arbeiten",
        "subtitle": "Hinzufügen und Verwalten deiner Forschungsmaterialien",
        "description": "Lerne, wie du deine Forschungsmaterialien hinzufügst, organisierst und optimal verwaltest.",
        "progress": 42.9
    },
    {
        "num": 4,
        "title": "Den KI-Assistenten nutzen",
        "subtitle": "Antworten und Erkenntnisse aus deinen Quellen erhalten",
        "description": "Entdecke die Macht der KI! Stelle effektive Fragen und erhalte präzise Antworten aus deinen Quellen.",
        "progress": 57.2
    },
    {
        "num": 5,
        "title": "Dein erstes Forschungsprojekt erstellen",
        "subtitle": "Schritt-für-Schritt-Anleitung",
        "description": "Führe dein erstes komplettes Forschungsprojekt durch - von der Idee bis zum fertigen Entwurf.",
        "progress": 71.5
    },
    {
        "num": 6,
        "title": "Erweiterte Funktionen und Techniken",
        "subtitle": "Deine Fähigkeiten auf die nächste Stufe bringen",
        "description": "Werde zum Power-User! Lerne fortgeschrittene Techniken und versteckte Features kennen.",
        "progress": 85.8
    },
    {
        "num": 7,
        "title": "Praktische Anwendungen",
        "subtitle": "Anwendungsfälle und Beispiele aus der Praxis",
        "description": "Entdecke reale Anwendungsfälle und lass dich von praktischen Beispielen inspirieren.",
        "progress": 100.0
    }
]

def create_lesson_html(lesson):
    num = lesson["num"]
    title = lesson["title"]
    subtitle = lesson["subtitle"]
    description = lesson["description"]
    progress = lesson["progress"]
    
    prev_lesson = num - 1 if num > 1 else None
    next_lesson = num + 1 if num < 7 else None
    
    # Read the markdown content
    md_file = f"lektion{num}.md"
    if os.path.exists(md_file):
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract content after the first heading
        lines = content.split('\n')
        content_lines = []
        in_content = False
        
        for line in lines:
            if line.startswith('## Einführung') or in_content:
                in_content = True
                if line.startswith('**Navigation:**'):
                    break
                content_lines.append(line)
        
        markdown_content = '\n'.join(content_lines)
        
        # Convert basic markdown to HTML
        html_content = markdown_content
        html_content = html_content.replace('**', '<strong>').replace('**', '</strong>')
        html_content = html_content.replace('*', '<em>').replace('*', '</em>')
        html_content = html_content.replace('## ', '<h2>').replace('\n', '</h2>\n', 1)
        html_content = html_content.replace('### ', '<h3>').replace('\n', '</h3>\n', 1)
        
        # Convert paragraphs
        paragraphs = html_content.split('\n\n')
        formatted_paragraphs = []
        
        for para in paragraphs:
            para = para.strip()
            if para and not para.startswith('<h') and not para.startswith('<div'):
                if para.startswith('*   '):
                    # Convert to list
                    items = para.split('\n*   ')
                    list_html = '<ul>\n'
                    for item in items:
                        item = item.replace('*   ', '').strip()
                        if item:
                            list_html += f'    <li>{item}</li>\n'
                    list_html += '</ul>'
                    formatted_paragraphs.append(list_html)
                else:
                    formatted_paragraphs.append(f'<p>{para}</p>')
            else:
                formatted_paragraphs.append(para)
        
        html_content = '\n\n'.join(formatted_paragraphs)
    else:
        html_content = f"<p>Inhalt für Lektion {num} wird geladen...</p>"

    html_template = f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lektion {num}: {title} - NotebookLM Meisterkurs</title>
    <meta name="description" content="{description}">
    <link rel="stylesheet" href="../css/styles.css">
    <link rel="icon" type="image/png" href="../images/logo.png">
</head>
<body>
    <!-- Header -->
    <header class="header">
        <div class="container">
            <a href="../index.html" class="logo">
                <img src="../images/logo.png" alt="NotebookLM Kurs Logo">
                NotebookLM Meisterkurs
            </a>
            <nav>
                <ul class="nav">
                    <li><a href="../index.html">Startseite</a></li>
                    <li><a href="lektion1.html"{'class="active"' if num == 1 else ''}>Lektion 1</a></li>
                    <li><a href="lektion2.html"{'class="active"' if num == 2 else ''}>Lektion 2</a></li>
                    <li><a href="lektion3.html"{'class="active"' if num == 3 else ''}>Lektion 3</a></li>
                    <li><a href="lektion4.html"{'class="active"' if num == 4 else ''}>Lektion 4</a></li>
                    <li><a href="lektion5.html"{'class="active"' if num == 5 else ''}>Lektion 5</a></li>
                    <li><a href="lektion6.html"{'class="active"' if num == 6 else ''}>Lektion 6</a></li>
                    <li><a href="lektion7.html"{'class="active"' if num == 7 else ''}>Lektion 7</a></li>
                </ul>
                <button class="mobile-menu-toggle">☰</button>
            </nav>
        </div>
    </header>

    <!-- Lesson Header -->
    <section class="hero" style="padding: 40px 0; background-image: url('../images/header-lektion{num}.png'); background-size: cover; background-position: center;">
        <div class="container">
            <h1>Lektion {num}: {title}</h1>
            <p>{subtitle}</p>
        </div>
    </section>

    <!-- Lesson Content -->
    <section class="section">
        <div class="container">
            <div style="max-width: 800px; margin: 0 auto;">
                {html_content}
                
                <!-- Mark Complete Button -->
                <div class="text-center" style="margin: 3rem 0;">
                    <button class="btn btn-secondary mark-complete-btn">Lektion als abgeschlossen markieren</button>
                </div>
            </div>
        </div>
    </section>

    <!-- Lesson Navigation -->
    <section class="lesson-nav">
        <div class="container">
            {'<a href="lektion' + str(prev_lesson) + '.html" class="btn btn-outline">← Lektion ' + str(prev_lesson) + '</a>' if prev_lesson else '<a href="../index.html" class="btn btn-outline">← Zurück zur Startseite</a>'}
            <div class="lesson-progress">
                <h4>Lektion {num} von 7</h4>
                <div class="progress-container">
                    <div class="progress-bar" style="width: {progress}%"></div>
                </div>
            </div>
            {'<a href="lektion' + str(next_lesson) + '.html" class="btn btn-primary">Lektion ' + str(next_lesson) + ' →</a>' if next_lesson else '<a href="../index.html" class="btn btn-primary">Kurs abgeschlossen! →</a>'}
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h4>NotebookLM Meisterkurs</h4>
                    <p>Revolutioniere deine Forschung mit KI-gestützten Tools.</p>
                </div>
                
                <div class="footer-section">
                    <h4>Navigation</h4>
                    <a href="../index.html">Startseite</a>
                    <a href="lektion1.html">Lektion 1</a>
                    <a href="lektion2.html">Lektion 2</a>
                    <a href="lektion3.html">Lektion 3</a>
                </div>
                
                <div class="footer-section">
                    <h4>Weitere Lektionen</h4>
                    <a href="lektion4.html">Lektion 4</a>
                    <a href="lektion5.html">Lektion 5</a>
                    <a href="lektion6.html">Lektion 6</a>
                    <a href="lektion7.html">Lektion 7</a>
                </div>
                
                <div class="footer-section">
                    <h4>Support</h4>
                    <a href="mailto:support@notebooklm-kurs.de">E-Mail Support</a>
                    <a href="../index.html#faq">FAQ</a>
                </div>
            </div>
            
            <div class="footer-bottom">
                <p>&copy; 2024 NotebookLM Meisterkurs. Alle Rechte vorbehalten.</p>
            </div>
        </div>
    </footer>

    <script src="../js/main.js"></script>
</body>
</html>"""
    
    return html_template

# Generate all lesson HTML files
for lesson in lessons:
    html_content = create_lesson_html(lesson)
    filename = f"lektion{lesson['num']}.html"
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Generated {filename}")

print("All lesson HTML files generated successfully!")
