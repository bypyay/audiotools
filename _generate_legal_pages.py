import os

BASE_DIR = r"D:\Codding\Claude Cowork code\Audio Tools"

HEADER_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Daily1Step Audio Tools</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://bypyay.github.io/audiotools/{filename}">
<meta property="og:title" content="{title} — Daily1Step Audio Tools">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta name="robots" content="index, follow">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
<header class="site-header">
  <div class="container">
    <a href="index.html" class="brand">Daily1Step Audio<span class="dot">.</span></a>
    <nav class="main-nav">
      <a href="index.html">All Audio Tools</a>
      <a href="tools/audio-cutter/">Audio Cutter</a>
      <a href="tools/merge-audio/">Merge Audio</a>
      <a href="tools/mp3-volume-booster/">Volume Booster</a>
      <a href="tools/compress-audio/">Compress MP3</a>
      <a href="about.html">About</a>
    </nav>
  </div>
</header>
"""

FOOTER_TEMPLATE = """<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-col">
        <h4>Daily1Step Audio Tools</h4>
        <p style="font-size:.88rem; line-height:1.6; margin-top:8px;">Fast, private, and 100% browser-based audio editing tools. Cut, merge, boost, convert, and edit audio files directly in your web browser with zero server uploads.</p>
      </div>
      <div class="footer-col">
        <h4>Popular Tools</h4>
        <ul>
          <li><a href="tools/audio-cutter/">Audio Cutter & Trimmer</a></li>
          <li><a href="tools/merge-audio/">Merge Audio Files</a></li>
          <li><a href="tools/mp3-volume-booster/">MP3 Volume Booster</a></li>
          <li><a href="tools/audio-speed-changer-online/">Change Audio Speed</a></li>
          <li><a href="tools/compress-audio/">Compress Audio</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Effects & Recording</h4>
        <ul>
          <li><a href="tools/music-pitch-changer/">Audio Pitch Changer</a></li>
          <li><a href="tools/audio-recorder/">Online Voice Recorder</a></li>
          <li><a href="tools/ringtone-maker/">Ringtone Maker</a></li>
          <li><a href="tools/add-reverb-to-audio/">Add Reverb to Audio</a></li>
          <li><a href="tools/video-to-mp3/">Video to MP3 Converter</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Company & Legal</h4>
        <ul>
          <li><a href="about.html">About Us</a></li>
          <li><a href="contact.html">Contact Us</a></li>
          <li><a href="privacy-policy.html">Privacy Policy</a></li>
          <li><a href="terms.html">Terms of Service</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <div>&copy; 2026 Daily1Step Audio. All rights reserved. 100% Browser-Based Processing.</div>
      <div>
        <a href="privacy-policy.html" style="margin-right:12px;">Privacy Policy</a>
        <a href="terms.html">Terms of Service</a>
      </div>
    </div>
  </div>
</footer>
</body>
</html>
"""

# 1. Privacy Policy
privacy_content = HEADER_TEMPLATE.format(
    title="Privacy Policy",
    desc="Privacy policy for Daily1Step Audio Tools. Learn how our 100% client-side Web Audio technology keeps your audio files and personal data private.",
    filename="privacy-policy.html"
) + """
<main class="seo-article">
  <div class="content-container">
    <div class="breadcrumb">
      <a href="index.html">Home</a> &gt; <span>Privacy Policy</span>
    </div>
    <h1>Privacy Policy</h1>
    <p><em>Last updated: August 17, 2026</em></p>

    <h2>1. Overview and Our Core Commitment</h2>
    <p>At Daily1Step Audio Tools (accessible from <code>https://bypyay.github.io/audiotools/</code>), privacy is not an afterthought—it is the foundation of our engineering. We believe that your personal voice notes, music tracks, podcast takes, and private recordings should never be uploaded to remote servers.</p>
    <p>Our platform operates on a <strong>100% Client-Side Architecture</strong>. When you cut, trim, boost, merge, or convert audio files using Daily1Step Audio, the audio data is processed locally inside your web browser's memory using HTML5 Web Audio API and WebAssembly. <strong>Your audio files are NEVER uploaded to our servers, stored in databases, or transmitted over the internet.</strong></p>

    <h2>2. Information We Do NOT Collect</h2>
    <ul>
      <li><strong>No Audio File Uploads:</strong> We never receive, store, or view your audio, music, or video files.</li>
      <li><strong>No Account Registration:</strong> You do not need to create an account, log in, or provide your email address to use any of our 23 audio tools.</li>
      <li><strong>No Personal Identifiers:</strong> We do not ask for your name, phone number, physical address, or payment details.</li>
    </ul>

    <h2>3. Cookies and Advertising Partners (Google AdSense)</h2>
    <p>To keep our audio tools 100% free and accessible to everyone worldwide, we may display advertisements provided by Google AdSense and third-party advertising networks.</p>
    <ul>
      <li>Google, as a third-party vendor, uses cookies (including the DoubleClick cookie) to serve ads based on prior visits to our website or other websites on the Internet.</li>
      <li>Users may opt out of personalized advertising by visiting <a href="https://www.google.com/settings/ads" target="_blank" rel="noopener">Google Ads Settings</a>.</li>
      <li>Alternatively, you can opt out of third-party vendor cookies by visiting <a href="https://www.aboutads.info/choices/" target="_blank" rel="noopener">AboutAds.info</a>.</li>
    </ul>

    <h2>4. Log Files and Web Analytics</h2>
    <p>Like standard web servers and static hosts (GitHub Pages), basic anonymous technical information may be logged when accessing our site, including IP addresses, browser types, Internet Service Providers (ISP), referring/exit pages, date/time stamps, and click counts. These logs contain no personally identifiable information and are used solely for analyzing trends, administering the site, and ensuring server uptime.</p>

    <h2>5. GDPR and CCPA Privacy Rights</h2>
    <p>Under the European Union General Data Protection Regulation (GDPR) and California Consumer Privacy Act (CCPA), users have the right to request information regarding data collection. Because Daily1Step Audio does not collect or store personal data or uploaded audio content, there is no personal data stored on our systems that can be shared or sold.</p>

    <h2>6. Contact Us</h2>
    <p>If you have questions or suggestions regarding our Privacy Policy, please reach out via our <a href="contact.html">Contact Us</a> page.</p>
  </div>
</main>
""" + FOOTER_TEMPLATE

# 2. Terms of Service
terms_content = HEADER_TEMPLATE.format(
    title="Terms of Service",
    desc="Terms of service and acceptable usage guidelines for Daily1Step Audio Tools.",
    filename="terms.html"
) + """
<main class="seo-article">
  <div class="content-container">
    <div class="breadcrumb">
      <a href="index.html">Home</a> &gt; <span>Terms of Service</span>
    </div>
    <h1>Terms of Service</h1>
    <p><em>Last updated: August 17, 2026</em></p>

    <h2>1. Acceptance of Terms</h2>
    <p>By accessing or using Daily1Step Audio Tools ("the Service"), you agree to be bound by these Terms of Service. If you do not agree with any part of these terms, you may not use the Service.</p>

    <h2>2. Description of Service</h2>
    <p>Daily1Step Audio provides free, browser-based audio manipulation utilities, including audio trimming, audio merging, volume boosting, pitch shifting, speed alteration, voice recording, noise removal, and format conversion. All processing is performed locally on the user's client device.</p>

    <h2>3. User Responsibility & Intellectual Property</h2>
    <p>You retain 100% ownership and copyright of any audio files, recordings, or music tracks processed using our tools. You agree that you will not use our Service to infringe upon any third-party copyrights, trademarks, or proprietary rights.</p>

    <h2>4. Disclaimer of Warranties</h2>
    <p>The Service is provided on an "AS IS" and "AS AVAILABLE" basis without warranties of any kind, either express or implied. Daily1Step Audio does not guarantee that the Service will be uninterrupted, error-free, or free from browser compatibility bugs.</p>

    <h2>5. Limitation of Liability</h2>
    <p>In no event shall Daily1Step Audio, its creators, or affiliates be liable for any direct, indirect, incidental, or consequential damages resulting from the use or inability to use the Service.</p>

    <h2>6. Changes to Terms</h2>
    <p>We reserve the right to modify these Terms of Service at any time. Continued use of the Service following any updates constitutes acceptance of the new terms.</p>
  </div>
</main>
""" + FOOTER_TEMPLATE

# 3. About Us
about_content = HEADER_TEMPLATE.format(
    title="About Us",
    desc="About Daily1Step Audio Tools — Our mission to bring fast, secure, and free client-side audio utilities to creators and musicians worldwide.",
    filename="about.html"
) + """
<main class="seo-article">
  <div class="content-container">
    <div class="breadcrumb">
      <a href="index.html">Home</a> &gt; <span>About Us</span>
    </div>
    <h1>About Daily1Step Audio Tools</h1>
    <p class="lead" style="font-size:1.15rem; color:var(--ink-soft); margin-bottom:24px;">Democratizing high-performance audio editing tools for creators, podcasters, students, and musicians worldwide with complete local privacy.</p>

    <h2>Our Mission</h2>
    <p>Traditional online audio converters and editors require users to upload large audio files to remote servers. This results in slow upload/download speeds, server queue delays, bandwidth costs, and severe privacy risks for sensitive recordings.</p>
    <p><strong>Daily1Step Audio was built to solve this problem.</strong> By harnessing cutting-edge modern web technologies—specifically the <strong>HTML5 Web Audio API</strong>, <strong>WebAssembly (WASM)</strong>, and <strong>Client-Side PCM Digital Signal Processing</strong>—we execute all audio transformations directly on your computer or phone's CPU/GPU.</p>

    <h2>Why Choose Daily1Step Audio?</h2>
    <div class="step-card-grid">
      <div class="step-card">
        <div class="step-num">1</div>
        <h4>100% Private &amp; Confidential</h4>
        <p>Your audio files never leave your device. Zero server uploads mean your private podcasts, meetings, and songs remain strictly confidential.</p>
      </div>
      <div class="step-card">
        <div class="step-num">2</div>
        <h4>Lightning-Fast Local Speed</h4>
        <p>No waiting for gigabytes of audio to upload or download. Instant rendering and real-time interactive waveform previews.</p>
      </div>
      <div class="step-card">
        <div class="step-num">3</div>
        <h4>23 Professional Audio Tools</h4>
        <p>Everything from precision audio cutting and multi-track merging to reverb, pitch shifting, ID3 tagging, and video audio extraction.</p>
      </div>
      <div class="step-card">
        <div class="step-num">4</div>
        <h4>Always 100% Free</h4>
        <p>No subscriptions, no watermarks, no file length limits, and no account registrations required.</p>
      </div>
    </div>

    <h2>Technology Stack</h2>
    <p>Our audio processing engine utilizes:</p>
    <ul>
      <li><strong>Web Audio API:</strong> Hardware-accelerated PCM sample buffer manipulation, dynamic biquad filtering, delay lines, and convolution impulse reverbs.</li>
      <li><strong>Pure JavaScript MP3 Encoder (LAME):</strong> High-fidelity psychoacoustic MP3 encoding right in the browser.</li>
      <li><strong>HTML5 Canvas:</strong> High-DPI retina waveform visualization with interactive drag-and-drop region markers and live playhead tracking.</li>
      <li><strong>MediaStream API:</strong> Studio-quality voice recording with real-time audio ducking and background music synchronization.</li>
    </ul>
  </div>
</main>
""" + FOOTER_TEMPLATE

# 4. Contact Us
contact_content = HEADER_TEMPLATE.format(
    title="Contact Us",
    desc="Get in touch with the Daily1Step Audio Tools team for support, feature suggestions, or partnerships.",
    filename="contact.html"
) + """
<main class="seo-article">
  <div class="content-container">
    <div class="breadcrumb">
      <a href="index.html">Home</a> &gt; <span>Contact Us</span>
    </div>
    <h1>Contact Us</h1>
    <p>Have questions, feedback, or suggestions for new audio tools? We'd love to hear from you!</p>

    <div style="max-width:680px; margin:28px 0; background:var(--bg-soft); border:1px solid var(--border); border-radius:var(--radius-lg); padding:28px;">
      <form onsubmit="event.preventDefault(); alert('Thank you for your message! Our team will get back to you soon.');">
        <div style="margin-bottom:16px;">
          <label style="display:block; font-weight:700; font-size:.9rem; margin-bottom:6px; color:var(--ink);">Your Name</label>
          <input type="text" required placeholder="Enter your full name" style="width:100%; padding:12px 14px; border:1px solid var(--border); border-radius:var(--radius-sm); font-size:1rem;">
        </div>
        <div style="margin-bottom:16px;">
          <label style="display:block; font-weight:700; font-size:.9rem; margin-bottom:6px; color:var(--ink);">Your Email</label>
          <input type="email" required placeholder="name@example.com" style="width:100%; padding:12px 14px; border:1px solid var(--border); border-radius:var(--radius-sm); font-size:1rem;">
        </div>
        <div style="margin-bottom:16px;">
          <label style="display:block; font-weight:700; font-size:.9rem; margin-bottom:6px; color:var(--ink);">Subject</label>
          <input type="text" required placeholder="Feedback / Feature Request / Support" style="width:100%; padding:12px 14px; border:1px solid var(--border); border-radius:var(--radius-sm); font-size:1rem;">
        </div>
        <div style="margin-bottom:20px;">
          <label style="display:block; font-weight:700; font-size:.9rem; margin-bottom:6px; color:var(--ink);">Message</label>
          <textarea rows="5" required placeholder="How can we help you?" style="width:100%; padding:12px 14px; border:1px solid var(--border); border-radius:var(--radius-sm); font-size:1rem; font-family:inherit;"></textarea>
        </div>
        <button type="submit" class="btn" style="width:100%;">Send Message</button>
      </form>
    </div>
  </div>
</main>
""" + FOOTER_TEMPLATE

# Write files
with open(os.path.join(BASE_DIR, "privacy-policy.html"), "w", encoding="utf-8") as f:
    f.write(privacy_content)

with open(os.path.join(BASE_DIR, "terms.html"), "w", encoding="utf-8") as f:
    f.write(terms_content)

with open(os.path.join(BASE_DIR, "about.html"), "w", encoding="utf-8") as f:
    f.write(about_content)

with open(os.path.join(BASE_DIR, "contact.html"), "w", encoding="utf-8") as f:
    f.write(contact_content)

# robots.txt
robots_txt = """User-agent: *
Allow: /

Sitemap: https://bypyay.github.io/audiotools/sitemap.xml
"""
with open(os.path.join(BASE_DIR, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(robots_txt)

print("AdSense legal pages and robots.txt generated successfully.")
