<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Excel Analyzer</title>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet"/>
  <style>
    /* ── Reset & Variables ──────────────────────────────────────── */
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

    :root {
      --bg:        #f0f4f8;
      --surface:   #ffffff;
      --border:    #dde3ec;
      --accent:    #2563eb;
      --accent2:   #7c3aed;
      --text:      #1e293b;
      --muted:     #64748b;
      --success:   #16a34a;
      --danger:    #dc2626;
      --radius:    14px;
      --shadow:    0 4px 24px rgba(37,99,235,.08);
    }

    body {
      font-family: 'DM Sans', sans-serif;
      background: var(--bg);
      color: var(--text);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    /* ── Header ────────────────────────────────────────────────── */
    header {
      width: 100%;
      background: var(--surface);
      border-bottom: 1px solid var(--border);
      padding: 0 2rem;
      display: flex;
      align-items: center;
      gap: 1rem;
      height: 64px;
      box-shadow: 0 1px 8px rgba(0,0,0,.06);
    }
    .logo-icon {
      width: 36px; height: 36px;
      background: linear-gradient(135deg, var(--accent), var(--accent2));
      border-radius: 10px;
      display: flex; align-items: center; justify-content: center;
      color: #fff; font-family: 'Space Mono', monospace; font-size: 15px; font-weight: 700;
    }
    header h1 { font-size: 1.1rem; font-weight: 600; letter-spacing: -.3px; }
    header span { font-size: .85rem; color: var(--muted); margin-left: auto; }

    /* ── Main content ───────────────────────────────────────────── */
    main {
      width: 100%; max-width: 740px;
      padding: 3rem 1.5rem;
      display: flex; flex-direction: column; gap: 2rem;
    }

    /* ── Hero card ─────────────────────────────────────────────── */
    .hero {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 2.5rem 2.5rem 2rem;
      box-shadow: var(--shadow);
      text-align: center;
    }
    .hero h2 {
      font-size: 1.7rem; font-weight: 600; letter-spacing: -.5px;
      background: linear-gradient(135deg, var(--accent), var(--accent2));
      -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }
    .hero p { color: var(--muted); margin-top: .5rem; font-size: .95rem; }

    /* ── Upload zone ────────────────────────────────────────────── */
    .drop-zone {
      margin-top: 1.8rem;
      border: 2px dashed var(--border);
      border-radius: var(--radius);
      padding: 2.2rem 1.5rem;
      transition: border-color .2s, background .2s;
      cursor: pointer;
      position: relative;
    }
    .drop-zone:hover, .drop-zone.drag-over {
      border-color: var(--accent);
      background: #eff6ff;
    }
    .drop-zone input[type="file"] {
      position: absolute; inset: 0; opacity: 0; cursor: pointer; width: 100%; height: 100%;
    }
    .drop-icon { font-size: 2.4rem; }
    .drop-zone p { color: var(--muted); font-size: .9rem; margin-top: .4rem; }
    .drop-zone strong { color: var(--accent); }
    #file-name { font-size: .82rem; color: var(--success); margin-top: .5rem; font-family: 'Space Mono', monospace; }

    /* ── Upload button ─────────────────────────────────────────── */
    .btn-upload {
      display: block; width: 100%; margin-top: 1.4rem;
      padding: .85rem;
      background: linear-gradient(135deg, var(--accent), var(--accent2));
      color: #fff; border: none; border-radius: 10px;
      font-family: 'DM Sans', sans-serif; font-size: 1rem; font-weight: 600;
      cursor: pointer; letter-spacing: .2px;
      transition: opacity .2s, transform .15s;
    }
    .btn-upload:hover { opacity: .9; transform: translateY(-1px); }
    .btn-upload:active { transform: translateY(0); }

    /* ── Flash messages ─────────────────────────────────────────── */
    .flash { padding: .9rem 1.2rem; border-radius: 10px; font-size: .9rem; }
    .flash.error   { background: #fef2f2; border: 1px solid #fca5a5; color: var(--danger); }
    .flash.success { background: #f0fdf4; border: 1px solid #86efac; color: var(--success); }

    /* ── Features strip ─────────────────────────────────────────── */
    .features {
      display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem;
    }
    .feat {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 1.2rem 1rem;
      text-align: center;
    }
    .feat .icon { font-size: 1.6rem; }
    .feat h3 { font-size: .9rem; font-weight: 600; margin-top: .4rem; }
    .feat p  { font-size: .78rem; color: var(--muted); margin-top: .25rem; }

    footer { color: var(--muted); font-size: .8rem; padding: 2rem; }

    @media (max-width: 560px) {
      .features { grid-template-columns: 1fr; }
      .hero { padding: 1.8rem 1.2rem 1.4rem; }
    }
  </style>
</head>
<body>

<header>
  <div class="logo-icon">EX</div>
  <h1>Excel Analyzer</h1>
  <span>v1.0 — basic structure</span>
</header>

<main>

  <!-- Flash messages -->
  {% with messages = get_flashed_messages(with_categories=true) %}
    {% for category, message in messages %}
      <div class="flash {{ category }}">⚠ {{ message }}</div>
    {% endfor %}
  {% endwith %}

  <!-- Upload card -->
  <div class="hero">
    <h2>Upload &amp; Analyze Excel</h2>
    <p>Drop your .xlsx file below. We'll clean it, extract the date, and plot every variable.</p>

    <form action="/upload" method="POST" enctype="multipart/form-data" id="uploadForm">
      <div class="drop-zone" id="dropZone">
        <input type="file" name="file" id="fileInput" accept=".xlsx,.xls" required/>
        <div class="drop-icon">📊</div>
        <p><strong>Click to browse</strong> or drag &amp; drop</p>
        <p>.xlsx / .xls — max 32 MB</p>
        <div id="file-name"></div>
      </div>
      <button type="submit" class="btn-upload">⚡ Process File</button>
    </form>
  </div>

  <!-- Features -->
  <div class="features">
    <div class="feat">
      <div class="icon">🧹</div>
      <h3>Data Cleaning</h3>
      <p>NaN &amp; negative values removed automatically</p>
    </div>
    <div class="feat">
      <div class="icon">📅</div>
      <h3>Date Extraction</h3>
      <p>File date parsed from the first column</p>
    </div>
    <div class="feat">
      <div class="icon">📈</div>
      <h3>Auto Plots</h3>
      <p>One chart per numeric column, saved as PNG</p>
    </div>
  </div>

</main>

<footer>Excel Analyzer · Flask + Pandas + Matplotlib · Basic structure — upgradeable</footer>

<script>
  const input    = document.getElementById("fileInput");
  const nameTag  = document.getElementById("file-name");
  const dropZone = document.getElementById("dropZone");

  input.addEventListener("change", () => {
    nameTag.textContent = input.files[0] ? "📎 " + input.files[0].name : "";
  });

  ["dragover","dragenter"].forEach(evt =>
    dropZone.addEventListener(evt, e => { e.preventDefault(); dropZone.classList.add("drag-over"); }));
  ["dragleave","drop"].forEach(evt =>
    dropZone.addEventListener(evt, () => dropZone.classList.remove("drag-over")));
</script>

</body>
</html>
