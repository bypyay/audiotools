import os
import json
from _build_all_audio_tools import AUDIO_TOOLS, CATEGORIES, BASE_DIR, TOOLS_DIR, JS_TOOLS_DIR

SITE_URL = "https://bypyay.github.io/audiotools"

def make_header(root_rel, page_title, page_desc, canonical_url, active_slug=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{page_title}</title>
<meta name="description" content="{page_desc}">
<link rel="canonical" href="{canonical_url}">
<meta property="og:title" content="{page_title}">
<meta property="og:description" content="{page_desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical_url}">
<meta name="twitter:card" content="summary_large_image">
<meta name="robots" content="index, follow">
<link rel="stylesheet" href="{root_rel}assets/css/style.css">
</head>
<body>
<header class="site-header">
  <div class="container">
    <a href="{root_rel}index.html" class="brand">Daily1Step Audio<span class="dot">.</span></a>
    <nav class="main-nav">
      <a href="{root_rel}index.html">All Tools</a>
      <a href="{root_rel}tools/audio-cutter/">Cut Audio</a>
      <a href="{root_rel}tools/merge-audio/">Merge Audio</a>
      <a href="{root_rel}tools/mp3-volume-booster/">Volume Booster</a>
      <a href="{root_rel}tools/compress-audio/">Compress Audio</a>
      <a href="{root_rel}about.html">About</a>
    </nav>
  </div>
</header>
"""

def make_footer(root_rel):
    return f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-col">
        <h4>Daily1Step Audio Tools</h4>
        <p style="font-size:.88rem; line-height:1.6; margin-top:8px;">Fast, private, and 100% browser-based audio editing tools. Cut, merge, boost, convert, and edit audio files directly in your web browser with zero server uploads.</p>
      </div>
      <div class="footer-col">
        <h4>Popular Tools</h4>
        <ul>
          <li><a href="{root_rel}tools/audio-cutter/">Audio Cutter & Trimmer</a></li>
          <li><a href="{root_rel}tools/merge-audio/">Merge Audio Files</a></li>
          <li><a href="{root_rel}tools/mp3-volume-booster/">MP3 Volume Booster</a></li>
          <li><a href="{root_rel}tools/audio-speed-changer-online/">Change Audio Speed</a></li>
          <li><a href="{root_rel}tools/compress-audio/">Compress Audio</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Effects & Recording</h4>
        <ul>
          <li><a href="{root_rel}tools/music-pitch-changer/">Audio Pitch Changer</a></li>
          <li><a href="{root_rel}tools/audio-recorder/">Online Voice Recorder</a></li>
          <li><a href="{root_rel}tools/ringtone-maker/">Ringtone Maker</a></li>
          <li><a href="{root_rel}tools/add-reverb-to-audio/">Add Reverb to Audio</a></li>
          <li><a href="{root_rel}tools/video-to-mp3/">Video to MP3 Converter</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Company & Legal</h4>
        <ul>
          <li><a href="{root_rel}about.html">About Us</a></li>
          <li><a href="{root_rel}contact.html">Contact Us</a></li>
          <li><a href="{root_rel}privacy-policy.html">Privacy Policy</a></li>
          <li><a href="{root_rel}terms.html">Terms of Service</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <div>&copy; 2026 Daily1Step Audio. All rights reserved. 100% Browser-Based Processing.</div>
      <div>
        <a href="{root_rel}privacy-policy.html" style="margin-right:12px;">Privacy Policy</a>
        <a href="{root_rel}terms.html">Terms of Service</a>
      </div>
    </div>
  </div>
</footer>
<script src="{root_rel}vendor/lame.min.js"></script>
<script src="{root_rel}vendor/browser-id3-writer.min.js"></script>
<script src="{root_rel}vendor/jsmediatags.min.js"></script>
<script src="{root_rel}assets/js/audio-core.js"></script>
</body>
</html>
"""

def generate_tool_html(t):
    slug = t["slug"]
    name = t["name"]
    title = t["title"]
    desc = t["desc"]
    h1 = t["h1"]
    tagline = t["tagline"]
    canonical = f"{SITE_URL}/tools/{slug}/"

    # JSON-LD Schemas (WebApplication + FAQPage + Breadcrumbs)
    faq_entities = []
    faq_html = ""
    for q, a in t["faqs"]:
        faq_entities.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": a
            }
        })
        faq_html += f"""
        <div class="faq-item">
          <button class="faq-question" type="button">
            <span>{q}</span>
            <span style="font-size:1.2rem;">+</span>
          </button>
          <div class="faq-answer" style="display:none;">
            <p>{a}</p>
          </div>
        </div>
        """

    schema_data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebApplication",
                "name": name,
                "url": canonical,
                "description": desc,
                "applicationCategory": "MultimediaApplication",
                "operatingSystem": "All modern browsers (Windows, Mac, iOS, Android)",
                "offers": {
                    "@type": "Offer",
                    "price": "0",
                    "priceCurrency": "USD"
                }
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "name": "Home",
                        "item": f"{SITE_URL}/"
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "name": "Audio Tools",
                        "item": f"{SITE_URL}/#tools"
                    },
                    {
                        "@type": "ListItem",
                        "position": 3,
                        "name": name,
                        "item": canonical
                    }
                ]
            },
            {
                "@type": "FAQPage",
                "mainEntity": faq_entities
            }
        ]
    }

    schema_json = json.dumps(schema_data, indent=2)

    # Tool specific UI workspace builder
    workspace_ui = build_workspace_ui(t)

    html = make_header("../../", title, desc, canonical, slug) + f"""
<script type="application/ld+json">
{schema_json}
</script>

<main class="tool-page">
  <div class="container">
    <div class="breadcrumb" style="max-width:920px; margin:0 auto 16px;">
      <a href="../../index.html">Home</a> &gt; <a href="../../index.html">Tools</a> &gt; <span>{name}</span>
    </div>

    <div class="tool-header">
      <h1>{h1}</h1>
      <p>{tagline}</p>
    </div>

    <!-- Ad Slot Top -->
    <div class="ad-slot-wrap">
      <span>Advertisement</span>
    </div>

    {workspace_ui}

    <!-- Ad Slot Middle -->
    <div class="ad-slot-wrap" style="margin-top:32px;">
      <span>Advertisement</span>
    </div>

  </div>
</main>

<article class="seo-article">
  <div class="content-container">
    <h2>How to Use {name} in 3 Simple Steps</h2>
    <div class="step-card-grid">
      <div class="step-card">
        <div class="step-num">1</div>
        <h4>Upload Your Audio</h4>
        <p>Drag and drop your audio file or click the upload area to select files from your computer, iPhone, or Android device.</p>
      </div>
      <div class="step-card">
        <div class="step-num">2</div>
        <h4>Adjust &amp; Preview</h4>
        <p>Fine-tune settings using real-time sliders and waveform region selectors. Click Play to verify your edits before saving.</p>
      </div>
      <div class="step-card">
        <div class="step-num">3</div>
        <h4>Export &amp; Download</h4>
        <p>Click the export button to process your audio locally and download pristine MP3 or WAV files instantly.</p>
      </div>
    </div>

    <h2>Why Use Daily1Step {name}?</h2>
    <p>Daily1Step {name} provides unmatched audio quality, speed, and privacy. Unlike conventional cloud converters that upload your audio to third-party servers, our software executes all signal processing directly inside your browser using the <strong>HTML5 Web Audio API</strong>.</p>
    <ul>
      <li><strong>100% Privacy Guaranteed:</strong> Files are never uploaded or stored on any server.</li>
      <li><strong>Instant Local Processing:</strong> Zero queue wait times or slow upload/download bandwidth bottlenecks.</li>
      <li><strong>Lossless Audio Quality:</strong> High-resolution 32-bit floating point PCM signal rendering.</li>
      <li><strong>Universal Format Compatibility:</strong> Works seamlessly with MP3, WAV, AAC, M4A, OGG, and video formats.</li>
    </ul>

    <h2>Supported Audio &amp; Video Formats</h2>
    <p>Our audio engine is compatible with all modern audio containers: <strong>MP3 (.mp3)</strong>, <strong>WAV (.wav)</strong>, <strong>AAC (.aac)</strong>, <strong>Apple Lossless / M4A (.m4a)</strong>, <strong>Ogg Vorbis (.ogg)</strong>, <strong>FLAC (.flac)</strong>, <strong>WebM (.webm)</strong>, and <strong>MP4 Video (.mp4)</strong>.</p>

    <h2>Frequently Asked Questions (FAQ)</h2>
    <div class="faq-list">
      {faq_html}
    </div>

    <!-- Ad Slot Bottom -->
    <div class="ad-slot-wrap" style="margin-top:40px;">
      <span>Advertisement</span>
    </div>
  </div>
</article>

<script src="../../assets/js/tools/{slug}.js"></script>
<script>
// FAQ Accordion interaction
document.querySelectorAll('.faq-question').forEach(function(btn) {{
  btn.addEventListener('click', function() {{
    var ans = btn.nextElementSibling;
    var isOpen = ans.style.display === 'block';
    ans.style.display = isOpen ? 'none' : 'block';
    btn.querySelector('span:last-child').textContent = isOpen ? '+' : '−';
  }});
}});
</script>
""" + make_footer("../../")
    return html

def build_workspace_ui(t):
    slug = t["slug"]
    
    if slug == "merge-audio":
        return """
    <div class="dropzone" id="dropzone">
      <input type="file" id="fileInput" accept="audio/*" multiple>
      <div class="dropzone-icon">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M8 3v3a2 2 0 0 1-2 2H3"/><path d="M21 8h-3a2 2 0 0 1-2-2V3"/><path d="M3 16h3a2 2 0 0 1 2 2v3"/><path d="M16 21v-3a2 2 0 0 1 2-2h3"/><line x1="12" y1="8" x2="12" y2="16"/></svg>
      </div>
      <p><strong>Click to choose audio files</strong> or drag and drop multiple tracks</p>
      <p style="color:var(--ink-soft); font-size:.85rem; margin-top:4px;">Supports MP3, WAV, AAC, M4A, OGG</p>
    </div>

    <div id="workspace" class="audio-workspace" style="display:none;">
      <h3 style="font-size:1.15rem; margin-bottom:12px;">Track Sequence (Drag or use buttons to reorder)</h3>
      <div id="trackList" style="display:flex; flex-direction:column; gap:8px; margin-bottom:16px;"></div>

      <div style="display:flex; gap:12px; align-items:center; flex-wrap:wrap; margin:16px 0; padding:14px; background:var(--bg-soft); border-radius:var(--radius-sm); border:1px solid var(--border);">
        <label style="font-weight:700; font-size:.9rem;">Output Format:</label>
        <select id="formatSelect" style="padding:6px 12px; border-radius:var(--radius-sm); border:1px solid var(--border); font-weight:600;">
          <option value="mp3-192">MP3 (192 kbps Standard)</option>
          <option value="mp3-320">MP3 (320 kbps High Quality)</option>
          <option value="wav">WAV (Uncompressed Lossless)</option>
        </select>
        <button type="button" class="btn sm secondary" id="addMoreBtn">+ Add More Files</button>
      </div>

      <button type="button" class="btn success" id="processBtn" style="width:100%; padding:14px;">Merge Tracks into One File</button>
      <div id="progressBar" style="display:none; width:100%; height:6px; background:#e2e8f0; border-radius:3px; margin-top:12px; overflow:hidden;">
        <div id="progressFill" style="width:0%; height:100%; background:var(--primary); transition:width .1s;"></div>
      </div>
    </div>

    <div class="result-box" id="resultBox">
      <div class="check">&#10003;</div>
      <h3>Audio Files Merged Successfully!</h3>
      <p id="resultInfo"></p>
      <a class="btn success" id="downloadBtn" download="merged_audio.mp3">Download Merged Audio</a>
      <div style="margin-top:12px;"><button class="btn secondary sm" id="resetBtn">Merge more audio</button></div>
    </div>
        """
    elif slug == "audio-recorder":
        return """
    <div class="audio-workspace" style="text-align:center; padding:36px 20px;">
      <div id="recVisualizerWrap" style="background:var(--bg-player); border-radius:var(--radius-md); overflow:hidden; margin-bottom:20px;">
        <canvas id="recCanvas" width="800" height="140" style="width:100%; height:140px; display:block;"></canvas>
      </div>
      
      <div class="time-display" id="recTime" style="display:inline-block; font-size:1.8rem; padding:8px 24px; margin-bottom:20px;">00:00.00</div>
      
      <div style="display:flex; justify-content:center; gap:12px; flex-wrap:wrap;">
        <button type="button" class="btn" id="startRecBtn" style="background:#e11d48; padding:14px 28px; font-size:1.1rem;">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><circle cx="12" cy="12" r="10"/></svg>
          <span>Start Recording</span>
        </button>
        <button type="button" class="btn secondary" id="pauseRecBtn" style="display:none;">Pause</button>
        <button type="button" class="btn danger" id="stopRecBtn" style="display:none;">Stop &amp; Save</button>
      </div>
    </div>

    <div class="result-box" id="resultBox">
      <div class="check">&#10003;</div>
      <h3>Recording Completed!</h3>
      <p id="resultInfo"></p>
      <div style="margin:16px 0;">
        <audio id="playbackAudio" controls style="width:100%; max-width:400px;"></audio>
      </div>
      <a class="btn success" id="downloadBtn" download="voice_recording.mp3">Download Recording (MP3)</a>
      <div style="margin-top:12px;"><button class="btn secondary sm" id="resetBtn">Record Another Take</button></div>
    </div>
        """
    else:
        # Standard Single File Waveform Tool
        return """
    <div class="dropzone" id="dropzone">
      <input type="file" id="fileInput" accept="audio/*, video/*">
      <div class="dropzone-icon">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" y1="19" x2="12" y2="23"/><line x1="8" y1="23" x2="16" y2="23"/></svg>
      </div>
      <p><strong>Click to choose an audio file</strong> or drag and drop here</p>
      <p style="color:var(--ink-soft); font-size:.85rem; margin-top:4px;">Supports MP3, WAV, AAC, M4A, FLAC, OGG, MP4</p>
    </div>

    <div id="workspace" class="audio-workspace" style="display:none;">
      <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px;">
        <span style="font-weight:700; font-size:1rem; color:var(--ink);" id="fileName">song.mp3</span>
        <span style="font-size:.85rem; color:var(--ink-soft);" id="fileDuration">00:00 / 00:00</span>
      </div>

      <div class="waveform-wrap">
        <canvas id="waveformCanvas" class="waveform-canvas"></canvas>
      </div>

      <div class="transport-bar">
        <div style="display:flex; gap:8px; align-items:center;">
          <button type="button" class="btn sm" id="playBtn">▶ Play</button>
          <button type="button" class="btn sm secondary" id="stopBtn">⏹ Stop</button>
          <button type="button" class="btn sm secondary" id="loopBtn">🔁 Loop</button>
        </div>
        <div class="time-display" id="timeDisplay">00:00.00</div>
      </div>

      <!-- Tool Controls Container -->
      <div id="toolControls" style="margin:20px 0; padding:18px; background:var(--bg-soft); border-radius:var(--radius-sm); border:1px solid var(--border);"></div>

      <button type="button" class="btn success" id="processBtn" style="width:100%; padding:14px;">Process &amp; Export Audio</button>
      <div id="progressBar" style="display:none; width:100%; height:6px; background:#e2e8f0; border-radius:3px; margin-top:12px; overflow:hidden;">
        <div id="progressFill" style="width:0%; height:100%; background:var(--primary); transition:width .1s;"></div>
      </div>
    </div>

    <div class="result-box" id="resultBox">
      <div class="check">&#10003;</div>
      <h3>Audio Processed Successfully!</h3>
      <p id="resultInfo"></p>
      <a class="btn success" id="downloadBtn" download="output.mp3">Download Processed Audio</a>
      <div style="margin-top:12px;"><button class="btn secondary sm" id="resetBtn">Process another file</button></div>
    </div>
        """

print("Tool template generator ready.")
