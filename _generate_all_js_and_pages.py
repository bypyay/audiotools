import os
import json
from _build_all_audio_tools import AUDIO_TOOLS, CATEGORIES, BASE_DIR, TOOLS_DIR, JS_TOOLS_DIR
from _generate_tool_templates import generate_tool_html, make_header, make_footer, SITE_URL

# 1. Generate All Tool HTML Pages
for t in AUDIO_TOOLS:
    slug = t["slug"]
    tool_dir = os.path.join(TOOLS_DIR, slug)
    os.makedirs(tool_dir, exist_ok=True)
    html = generate_tool_html(t)
    with open(os.path.join(tool_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)

print("Generated all 23 tool HTML pages.")

# 2. Generate Homepage Hub (index.html)
tab_buttons_html = ""
for cat_key, cat_name, cat_icon, count in CATEGORIES:
    active = " active" if cat_key == "all" else ""
    tab_buttons_html += f"""
    <button class="category-tab{active}" data-category="{cat_key}">
      <span>{cat_icon} {cat_name}</span>
      <span class="tab-count">{count}</span>
    </button>
    """

tool_cards_html = ""
for t in AUDIO_TOOLS:
    tool_cards_html += f"""
    <a href="tools/{t['slug']}/" class="tool-card" data-category="{t['category']}" data-title="{t['name'].lower()}" data-desc="{t['desc'].lower()}">
      <div class="icon" style="background:{t['color']};">{t['icon']}</div>
      <h3>{t['name']}</h3>
      <p>{t['desc']}</p>
    </a>
    """

home_schema = {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "name": "Daily1Step Audio Tools",
    "url": f"{SITE_URL}/",
    "description": "Free online audio tools suite. Cut, merge, volume boost, pitch shift, compress, and edit audio files directly in your web browser with 100% privacy.",
    "potentialAction": {
        "@type": "SearchAction",
        "target": f"{SITE_URL}/?q={{search_term_string}}",
        "query-input": "required name=search_term_string"
    }
}

home_faqs = [
    ("Are all audio tools on Daily1Step free?", "Yes! All 23 audio tools are 100% free to use with zero hidden limits, subscriptions, or watermarks."),
    ("Are my audio files uploaded to a server?", "No! Daily1Step uses cutting-edge HTML5 Web Audio API technology to execute all processing locally in your browser memory. Your files never leave your computer or smartphone."),
    ("Can I use these tools on mobile (Android / iPhone)?", "Yes! Our responsive web application works flawlessly on mobile browsers including Safari, Chrome, Edge, and Firefox."),
    ("What audio formats are supported?", "We support MP3, WAV, AAC, M4A, OGG, FLAC, and WebM audio, as well as MP4 video audio extraction.")
]

home_faq_html = ""
for q, a in home_faqs:
    home_faq_html += f"""
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

home_html = make_header("", "Daily1Step Audio Tools — Free Online Audio Editor, Cutter & Converter", "Edit, merge, cut, boost volume, change pitch, and compress audio files online for free. 100% private, browser-based Web Audio tools with no uploads.", f"{SITE_URL}/") + f"""
<script type="application/ld+json">
{json.dumps(home_schema, indent=2)}
</script>

<section class="hero">
  <div class="container">
    <h1>Every Audio Tool You Need, In One Place</h1>
    <p>Cut, merge, boost volume, change pitch &amp; speed, compress, and record audio &mdash; 100% free, no signup, and processed directly inside your web browser.</p>
  </div>
</section>

<!-- Ad Slot Top -->
<div class="container">
  <div class="ad-slot-wrap">
    <span>Advertisement</span>
  </div>
</div>

<section class="container" id="tools">
  <div class="tool-controls-wrap">
    <div class="tool-search-box">
      <span class="search-icon">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
      </span>
      <input type="text" id="toolSearchInput" placeholder="Search 23 audio tools (e.g. cut, merge, volume booster, pitch)..." autocomplete="off">
    </div>

    <div class="category-tabs" id="categoryTabs">
      {tab_buttons_html}
    </div>
  </div>

  <div class="tool-grid" id="mainToolGrid">
    {tool_cards_html}
  </div>

  <div id="noResultsMsg" style="display:none; text-align:center; padding:50px 20px; color:var(--ink-soft);">
    <p style="font-size:1.4rem; font-weight:700; color:var(--ink); margin-bottom:6px;">No audio tools found</p>
    <p>Try searching for different keywords like "cut", "volume", "pitch", "merge", or "compress".</p>
  </div>
</section>

<!-- Ad Slot Middle -->
<div class="container">
  <div class="ad-slot-wrap">
    <span>Advertisement</span>
  </div>
</div>

<article class="seo-article">
  <div class="content-container">
    <h2>Why Choose Daily1Step Audio Tools?</h2>
    <p>Daily1Step Audio runs entirely in your web browser. Unlike conventional audio converter portals that require you to upload private audio to cloud servers, all processing on Daily1Step happens on your device using client-side JavaScript, Web Audio API, and WebAssembly.</p>

    <div class="step-card-grid">
      <div class="step-card">
        <div class="step-num">⚡</div>
        <h4>Instant Local Speed</h4>
        <p>No waiting in queue. Your files are rendered and encoded in real-time by your device hardware.</p>
      </div>
      <div class="step-card">
        <div class="step-num">🔒</div>
        <h4>100% Privacy &amp; Security</h4>
        <p>Your songs, podcast takes, and voice recordings never leave your computer or phone.</p>
      </div>
      <div class="step-card">
        <div class="step-num">🎛️</div>
        <h4>23 Studio-Grade Tools</h4>
        <p>Everything you need: trimming, sequencing, volume boosting, pitch shifting, reverb, and tagging.</p>
      </div>
      <div class="step-card">
        <div class="step-num">💯</div>
        <h4>Always 100% Free</h4>
        <p>No subscription fees, no limits, no watermarks, and no registration required.</p>
      </div>
    </div>

    <h2>Frequently Asked Questions</h2>
    <div class="faq-list">
      {home_faq_html}
    </div>
  </div>
</article>

<script>
(function() {{
  var searchInput = document.getElementById('toolSearchInput');
  var categoryTabs = document.querySelectorAll('.category-tab');
  var toolCards = document.querySelectorAll('.tool-card');
  var noResults = document.getElementById('noResultsMsg');
  var currentCategory = 'all';

  function filterTools() {{
    var query = (searchInput.value || '').trim().toLowerCase();
    var visibleCount = 0;

    toolCards.forEach(function(card) {{
      var cat = card.getAttribute('data-category');
      var title = card.getAttribute('data-title');
      var desc = card.getAttribute('data-desc');

      var matchesCat = (currentCategory === 'all' || cat === currentCategory);
      var matchesQuery = !query || title.indexOf(query) !== -1 || desc.indexOf(query) !== -1;

      if (matchesCat && matchesQuery) {{
        card.style.display = 'flex';
        visibleCount++;
      }} else {{
        card.style.display = 'none';
      }}
    }});

    if (noResults) {{
      noResults.style.display = (visibleCount === 0) ? 'block' : 'none';
    }}
  }}

  categoryTabs.forEach(function(tab) {{
    tab.addEventListener('click', function() {{
      categoryTabs.forEach(function(t) {{ t.classList.remove('active'); }});
      tab.classList.add('active');
      currentCategory = tab.getAttribute('data-category');
      filterTools();
    }});
  }});

  if (searchInput) {{
    searchInput.addEventListener('input', filterTools);
  }}

  // FAQ Accordion
  document.querySelectorAll('.faq-question').forEach(function(btn) {{
    btn.addEventListener('click', function() {{
      var ans = btn.nextElementSibling;
      var isOpen = ans.style.display === 'block';
      ans.style.display = isOpen ? 'none' : 'block';
      btn.querySelector('span:last-child').textContent = isOpen ? '+' : '−';
    }});
  }});
}})();
</script>
""" + make_footer("")

with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(home_html)

print("Generated homepage index.html.")

# 3. Generate sitemap.xml
sitemap_urls = [
    f"{SITE_URL}/",
    f"{SITE_URL}/about.html",
    f"{SITE_URL}/contact.html",
    f"{SITE_URL}/privacy-policy.html",
    f"{SITE_URL}/terms.html",
]
for t in AUDIO_TOOLS:
    sitemap_urls.append(f"{SITE_URL}/tools/{t['slug']}/")

sitemap_xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
"""
for u in sitemap_urls:
    sitemap_xml += f"""  <url>
    <loc>{u}</loc>
    <lastmod>2026-08-17</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
"""
sitemap_xml += "</urlset>\n"

with open(os.path.join(BASE_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write(sitemap_xml)

print("Generated sitemap.xml with 28 URLs.")
