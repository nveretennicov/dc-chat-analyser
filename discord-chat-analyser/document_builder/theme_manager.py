class ThemeManager:
    
    @staticmethod
    def get_css():
        return ThemeManager._default_theme()

    @staticmethod
    def _default_theme():
        return """
        @import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;1,9..40,300&display=swap');

        /* ── Design Tokens ─────────────────────────────── */
        :root {
            --ink:       #0f0e0c;
            --ink-2:     #2e2c29;
            --ink-3:     #6b6760;
            --rule:      #e4e0d8;
            --surface:   #faf9f7;
            --paper:     #ffffff;
            --accent:    #c8491a;
            --accent-2:  #e8d5c4;
            --code-bg:   #f3f1ed;
            --radius:    4px;
            --serif:     'DM Serif Display', Georgia, serif;
            --sans:      'DM Sans', 'Helvetica Neue', sans-serif;
        }

        /* ── Page Setup ─────────────────────────────────── */
        @page {
            size: A4;
            margin: 1.6cm 2cm;
        }

        /* ── Base ───────────────────────────────────────── */
        body {
            font-family: var(--sans);
            font-size: 10.5pt;
            font-weight: 300;
            line-height: 1.55;
            color: var(--ink-2);
            background: var(--paper);
            text-rendering: optimizeLegibility;
            -webkit-font-smoothing: antialiased;
        }

        /* ── Header ─────────────────────────────────────── */
        .header {
            margin-bottom: 24px;
            padding-bottom: 16px;
            border-bottom: 1px solid var(--rule);
            position: relative;
        }

        .header::before {
            content: '';
            display: block;
            width: 36px;
            height: 3px;
            background: var(--accent);
            margin-bottom: 12px;
        }

        .header h1 {
            font-family: var(--serif);
            font-size: 22pt;
            font-weight: 400;
            font-style: italic;
            letter-spacing: -0.5px;
            margin: 0 0 4px;
            color: var(--ink);
            line-height: 1.15;
        }

        .header p {
            margin: 0;
            font-size: 8.5pt;
            font-weight: 400;
            color: var(--ink-3);
            letter-spacing: 0.5px;
            text-transform: uppercase;
        }

        /* ── Sections ───────────────────────────────────── */
        .section {
            margin-bottom: 18px;
            padding: 12px 16px;
            background: var(--surface);
            border-left: 3px solid var(--accent);
            border-radius: 0 var(--radius) var(--radius) 0;
            page-break-inside: avoid;
        }

        .section h2 {
            font-family: var(--serif);
            font-size: 13pt;
            font-weight: 400;
            margin: 0 0 8px;
            color: var(--ink);
            letter-spacing: -0.2px;
        }

        .section p {
            margin: 6px 0;
            color: var(--ink-2);
        }

        /* ── Typography ─────────────────────────────────── */
        h3, h4 {
            font-family: var(--sans);
            font-weight: 600;
            color: var(--ink);
        }

        h3 { font-size: 11pt; }
        h4 { font-size: 10pt; color: var(--ink-3); text-transform: uppercase; letter-spacing: 0.6px; }

        a {
            color: var(--accent);
            text-decoration: underline;
            text-decoration-thickness: 1px;
            text-underline-offset: 3px;
        }

        strong { font-weight: 600; color: var(--ink); }

        em { font-family: var(--serif); font-style: italic; }

        /* ── Tables ─────────────────────────────────────── */
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 12px 0;
            font-size: 9.5pt;
        }

        thead tr {
            border-bottom: 2px solid var(--ink);
        }

        th {
            font-weight: 600;
            font-size: 8pt;
            letter-spacing: 0.7px;
            text-transform: uppercase;
            color: var(--ink);
            padding: 6px 10px;
            text-align: left;
        }

        td {
            padding: 6px 10px;
            color: var(--ink-2);
            border-bottom: 1px solid var(--rule);
        }

        tbody tr:last-child td {
            border-bottom: none;
        }

        tbody tr:nth-child(even) td {
            background: var(--surface);
        }

        /* ── Code ───────────────────────────────────────── */
        pre {
            background: var(--code-bg);
            border: 1px solid var(--rule);
            border-left: 3px solid var(--ink-3);
            border-radius: 0 var(--radius) var(--radius) 0;
            padding: 9px 12px;
            font-family: 'Courier New', 'Menlo', monospace;
            font-size: 9pt;
            line-height: 1.5;
            color: var(--ink);
            overflow-x: auto;
        }

        code {
            font-family: 'Courier New', 'Menlo', monospace;
            font-size: 9pt;
            background: var(--code-bg);
            color: var(--accent);
            padding: 1px 4px;
            border-radius: 2px;
        }

        /* ── Blockquote ─────────────────────────────────── */
        blockquote {
            margin: 12px 0;
            padding: 9px 14px;
            background: var(--accent-2);
            border-left: 3px solid var(--accent);
            font-family: var(--serif);
            font-style: italic;
            font-size: 11.5pt;
            color: var(--ink);
            border-radius: 0 var(--radius) var(--radius) 0;
        }

        blockquote p { margin: 0; }

        /* ── Images ─────────────────────────────────────── */
        .image, img {
            display: block;
            margin: 4px 0;
            max-width: 100%;
            border-radius: var(--radius);
            border: 2px solid var(--rule);
        }

        .image-caption {
            font-size: 8.5pt;
            color: var(--ink-3);
            margin-top: -6px;
            margin-bottom: 12px;
            font-style: italic;
        }

        /* ── Footnote ───────────────────────────────────── */
        .footnote {
            font-size: 8pt;
            color: var(--ink-3);
            border-top: 1px solid var(--rule);
            margin-top: 14px;
            padding-top: 6px;
            line-height: 1.4;
        }

        /* ── Divider ────────────────────────────────────── */
        hr {
            border: none;
            border-top: 1px solid var(--rule);
            margin: 18px 0;
        }

        /* ── Utility ────────────────────────────────────── */
        .page-break { page-break-before: always; }

        .label {
            display: inline-block;
            font-size: 7.5pt;
            font-weight: 600;
            letter-spacing: 0.6px;
            text-transform: uppercase;
            color: var(--paper);
            background: var(--accent);
            padding: 1px 6px;
            border-radius: 2px;
        }

        /* ── Print ──────────────────────────────────────── */
        @media print {
            body { background: white; }
            .section { background: white; }
        }
        """