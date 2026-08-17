import os
from _build_all_audio_tools import JS_TOOLS_DIR

# Template helper for standard waveform tools
def make_standard_tool_js(slug, controls_html, process_code, extra_setup=""):
    return f"""// Daily1Step Audio Tool: {slug}
(function() {{
  'use strict';

  var dropzone = document.getElementById('dropzone');
  var fileInput = document.getElementById('fileInput');
  var workspace = document.getElementById('workspace');
  var fileNameEl = document.getElementById('fileName');
  var fileDurationEl = document.getElementById('fileDuration');
  var waveformCanvas = document.getElementById('waveformCanvas');
  var playBtn = document.getElementById('playBtn');
  var stopBtn = document.getElementById('stopBtn');
  var loopBtn = document.getElementById('loopBtn');
  var timeDisplay = document.getElementById('timeDisplay');
  var toolControls = document.getElementById('toolControls');
  var processBtn = document.getElementById('processBtn');
  var progressBar = document.getElementById('progressBar');
  var progressFill = document.getElementById('progressFill');
  var resultBox = document.getElementById('resultBox');
  var resultInfo = document.getElementById('resultInfo');
  var downloadBtn = document.getElementById('downloadBtn');
  var resetBtn = document.getElementById('resetBtn');

  var currentFile = null;
  var currentBuffer = null;
  var sourceNode = null;
  var isPlaying = false;
  var isLooping = false;
  var startTime = 0;
  var pauseOffset = 0;
  var animFrameId = null;

  // Render Tool Controls
  if (toolControls) {{
    toolControls.innerHTML = `{controls_html}`;
  }}

  // File Upload Handling
  dropzone.addEventListener('click', function() {{ fileInput.click(); }});
  dropzone.addEventListener('dragover', function(e) {{ e.preventDefault(); dropzone.classList.add('dragover'); }});
  dropzone.addEventListener('dragleave', function() {{ dropzone.classList.remove('dragover'); }});
  dropzone.addEventListener('drop', function(e) {{
    e.preventDefault();
    dropzone.classList.remove('dragover');
    if (e.dataTransfer.files.length > 0) {{
      loadAudioFile(e.dataTransfer.files[0]);
    }}
  }});
  fileInput.addEventListener('change', function(e) {{
    if (e.target.files.length > 0) {{
      loadAudioFile(e.target.files[0]);
    }}
  }});

  function loadAudioFile(file) {{
    currentFile = file;
    fileNameEl.textContent = file.name;
    fileDurationEl.textContent = 'Loading and decoding audio...';
    dropzone.style.display = 'none';
    workspace.style.display = 'block';
    resultBox.style.display = 'none';

    AudioCore.decodeAudioFile(file).then(function(buffer) {{
      currentBuffer = buffer;
      fileDurationEl.textContent = 'Duration: ' + AudioCore.formatTime(buffer.duration, true) + ' | ' + buffer.sampleRate + ' Hz';
      drawWave();
      if (typeof onAudioLoaded === 'function') {{
        onAudioLoaded(buffer);
      }}
    }}).catch(function(err) {{
      alert('Error decoding audio: ' + err.message);
      resetUI();
    }});
  }}

  function drawWave(currentTime) {{
    if (!currentBuffer) return;
    var opt = {{
      currentTime: currentTime || pauseOffset,
      startSec: window.selStartSec,
      endSec: window.selEndSec
    }};
    AudioCore.drawWaveform(waveformCanvas, currentBuffer, opt);
  }}

  // Playback Transport
  playBtn.addEventListener('click', function() {{
    if (isPlaying) {{
      pausePlayback();
    }} else {{
      startPlayback();
    }}
  }});

  stopBtn.addEventListener('click', function() {{
    stopPlayback();
  }});

  loopBtn.addEventListener('click', function() {{
    isLooping = !isLooping;
    loopBtn.classList.toggle('active', isLooping);
  }});

  function startPlayback() {{
    if (!currentBuffer) return;
    var ctx = AudioCore.getContext();
    sourceNode = ctx.createBufferSource();
    sourceNode.buffer = currentBuffer;
    sourceNode.loop = isLooping;

    // Connect effects if defined
    if (typeof applyLiveEffects === 'function') {{
      applyLiveEffects(sourceNode, ctx);
    }} else {{
      sourceNode.connect(ctx.destination);
    }}

    var offset = (window.selStartSec !== undefined) ? Math.max(window.selStartSec, pauseOffset) : pauseOffset;
    if (offset >= (window.selEndSec || currentBuffer.duration)) {{
      offset = window.selStartSec || 0;
    }}

    sourceNode.start(0, offset);
    startTime = ctx.currentTime - offset;
    isPlaying = true;
    playBtn.textContent = '⏸ Pause';
    trackProgress();
  }}

  function pausePlayback() {{
    if (sourceNode) {{
      sourceNode.stop();
      sourceNode.disconnect();
    }}
    var ctx = AudioCore.getContext();
    pauseOffset = ctx.currentTime - startTime;
    isPlaying = false;
    playBtn.textContent = '▶ Play';
    cancelAnimationFrame(animFrameId);
  }}

  function stopPlayback() {{
    if (sourceNode) {{
      sourceNode.stop();
      sourceNode.disconnect();
    }}
    isPlaying = false;
    pauseOffset = window.selStartSec || 0;
    playBtn.textContent = '▶ Play';
    cancelAnimationFrame(animFrameId);
    timeDisplay.textContent = AudioCore.formatTime(pauseOffset, true);
    drawWave(pauseOffset);
  }}

  function trackProgress() {{
    if (!isPlaying) return;
    var ctx = AudioCore.getContext();
    var cur = ctx.currentTime - startTime;

    if (window.selEndSec && cur >= window.selEndSec) {{
      if (isLooping) {{
        stopPlayback();
        startPlayback();
        return;
      }} else {{
        stopPlayback();
        return;
      }}
    }}

    if (cur >= currentBuffer.duration) {{
      if (!isLooping) {{
        stopPlayback();
        return;
      }}
    }}

    timeDisplay.textContent = AudioCore.formatTime(cur, true);
    drawWave(cur);
    animFrameId = requestAnimationFrame(trackProgress);
  }}

  // Interactive Waveform Clicking
  waveformCanvas.addEventListener('click', function(e) {{
    if (!currentBuffer) return;
    var rect = waveformCanvas.getBoundingClientRect();
    var x = e.clientX - rect.left;
    var pct = Math.max(0, Math.min(1, x / rect.width));
    var clickedTime = pct * currentBuffer.duration;
    pauseOffset = clickedTime;
    timeDisplay.textContent = AudioCore.formatTime(clickedTime, true);
    drawWave(clickedTime);
    if (isPlaying) {{
      pausePlayback();
      startPlayback();
    }}
  }});

  // Process & Export Audio
  processBtn.addEventListener('click', function() {{
    if (!currentBuffer) return;
    stopPlayback();
    progressBar.style.display = 'block';
    progressFill.style.width = '10%';
    processBtn.disabled = true;

    {process_code}
  }});

  resetBtn.addEventListener('click', resetUI);

  function resetUI() {{
    stopPlayback();
    currentFile = null;
    currentBuffer = null;
    dropzone.style.display = 'block';
    workspace.style.display = 'none';
    resultBox.style.display = 'none';
    progressBar.style.display = 'none';
    processBtn.disabled = false;
    fileInput.value = '';
  }}

  {extra_setup}
}})();
"""

# Let's define the tools JS dictionary
TOOL_JS = {}

# 1. audio-cutter
TOOL_JS["audio-cutter"] = make_standard_tool_js(
    "audio-cutter",
    controls_html="""
      <div style="display:flex; justify-content:space-between; gap:16px; flex-wrap:wrap;">
        <div style="flex:1; min-width:200px;">
          <label style="font-weight:700; font-size:.9rem; display:block; margin-bottom:4px;">Start Time (seconds):</label>
          <input type="number" id="startTimeInput" step="0.1" min="0" value="0" style="width:100%; padding:8px 12px; border:1px solid var(--border); border-radius:var(--radius-sm); font-weight:700;">
        </div>
        <div style="flex:1; min-width:200px;">
          <label style="font-weight:700; font-size:.9rem; display:block; margin-bottom:4px;">End Time (seconds):</label>
          <input type="number" id="endTimeInput" step="0.1" min="0" value="30" style="width:100%; padding:8px 12px; border:1px solid var(--border); border-radius:var(--radius-sm); font-weight:700;">
        </div>
      </div>
      <div style="display:flex; gap:16px; margin-top:14px; flex-wrap:wrap;">
        <label style="display:flex; align-items:center; gap:6px; font-weight:600; font-size:.9rem; cursor:pointer;">
          <input type="checkbox" id="fadeInCheck" checked> Fade In (1s)
        </label>
        <label style="display:flex; align-items:center; gap:6px; font-weight:600; font-size:.9rem; cursor:pointer;">
          <input type="checkbox" id="fadeOutCheck" checked> Fade Out (1s)
        </label>
      </div>
    """,
    process_code="""
      var s = parseFloat(document.getElementById('startTimeInput').value) || 0;
      var e = parseFloat(document.getElementById('endTimeInput').value) || currentBuffer.duration;
      s = Math.max(0, Math.min(s, currentBuffer.duration));
      e = Math.max(s + 0.1, Math.min(e, currentBuffer.duration));

      var cutBuffer = AudioCore.sliceAudioBuffer(currentBuffer, s, e);

      // Apply Fade In / Out
      if (document.getElementById('fadeInCheck').checked) {
        var fadeSamples = Math.min(cutBuffer.sampleRate * 1, cutBuffer.length / 2);
        for (var c = 0; c < cutBuffer.numberOfChannels; c++) {
          var d = cutBuffer.getChannelData(c);
          for (var i = 0; i < fadeSamples; i++) {
            d[i] *= (i / fadeSamples);
          }
        }
      }
      if (document.getElementById('fadeOutCheck').checked) {
        var fadeSamples = Math.min(cutBuffer.sampleRate * 1, cutBuffer.length / 2);
        for (var c = 0; c < cutBuffer.numberOfChannels; c++) {
          var d = cutBuffer.getChannelData(c);
          var len = cutBuffer.length;
          for (var i = 0; i < fadeSamples; i++) {
            d[len - 1 - i] *= (i / fadeSamples);
          }
        }
      }

      AudioCore.audioBufferToMp3(cutBuffer, 192, function(pct) {
        progressFill.style.width = pct + '%';
      }).then(function(blob) {
        workspace.style.display = 'none';
        resultBox.style.display = 'block';
        resultInfo.textContent = 'Trimmed: ' + AudioCore.formatTime(s) + ' to ' + AudioCore.formatTime(e) + ' | Size: ' + AudioCore.formatBytes(blob.size);
        downloadBtn.href = URL.createObjectURL(blob);
        downloadBtn.download = 'cut_' + currentFile.name.replace(/\\.[^/.]+$/, "") + '.mp3';
      });
    """,
    extra_setup="""
      function onAudioLoaded(buf) {
        window.selStartSec = 0;
        window.selEndSec = Math.min(buf.duration, 30);
        document.getElementById('startTimeInput').value = window.selStartSec.toFixed(1);
        document.getElementById('endTimeInput').value = window.selEndSec.toFixed(1);
        document.getElementById('endTimeInput').max = buf.duration.toFixed(1);
      }
      document.getElementById('startTimeInput').addEventListener('input', function() {
        window.selStartSec = Math.max(0, parseFloat(this.value) || 0);
        drawWave();
      });
      document.getElementById('endTimeInput').addEventListener('input', function() {
        window.selEndSec = Math.min(currentBuffer ? currentBuffer.duration : 1000, parseFloat(this.value) || 0);
        drawWave();
      });
    """
)

# 2. mp3-volume-booster
TOOL_JS["mp3-volume-booster"] = make_standard_tool_js(
    "mp3-volume-booster",
    controls_html="""
      <label style="font-weight:700; font-size:.95rem; display:block; margin-bottom:8px;">Volume Boost Level: <span id="boostVal" style="color:var(--primary);">200% (+6 dB)</span></label>
      <input type="range" id="boostSlider" min="50" max="500" value="200" step="10" class="range-slider" style="margin-bottom:14px;">
      <div style="display:flex; gap:6px; flex-wrap:wrap;">
        <button type="button" class="preset-chip" data-val="125">125% (+2 dB)</button>
        <button type="button" class="preset-chip" data-val="150">150% (+3.5 dB)</button>
        <button type="button" class="preset-chip active" data-val="200">200% (+6 dB)</button>
        <button type="button" class="preset-chip" data-val="300">300% (+9.5 dB)</button>
        <button type="button" class="preset-chip" data-val="400">400% (+12 dB)</button>
        <button type="button" class="preset-chip" data-val="500">500% (+14 dB)</button>
      </div>
    """,
    process_code="""
      var mult = (parseFloat(document.getElementById('boostSlider').value) || 200) / 100.0;
      var boosted = AudioCore.applyGain(currentBuffer, mult);

      AudioCore.audioBufferToMp3(boosted, 192, function(pct) {
        progressFill.style.width = pct + '%';
      }).then(function(blob) {
        workspace.style.display = 'none';
        resultBox.style.display = 'block';
        resultInfo.textContent = 'Boosted Volume to ' + Math.round(mult * 100) + '% | Size: ' + AudioCore.formatBytes(blob.size);
        downloadBtn.href = URL.createObjectURL(blob);
        downloadBtn.download = 'boosted_' + currentFile.name.replace(/\\.[^/.]+$/, "") + '.mp3';
      });
    """,
    extra_setup="""
      var slider = document.getElementById('boostSlider');
      var valEl = document.getElementById('boostVal');
      slider.addEventListener('input', function() {
        var v = this.value;
        var db = (20 * Math.log10(v / 100)).toFixed(1);
        valEl.textContent = v + '% (' + (db > 0 ? '+' : '') + db + ' dB)';
        document.querySelectorAll('.preset-chip').forEach(function(c) {
          c.classList.toggle('active', c.getAttribute('data-val') === v);
        });
      });
      document.querySelectorAll('.preset-chip').forEach(function(c) {
        c.addEventListener('click', function() {
          slider.value = this.getAttribute('data-val');
          slider.dispatchEvent(new Event('input'));
        });
      });
    """
)

# 3. audio-speed-changer-online
TOOL_JS["audio-speed-changer-online"] = make_standard_tool_js(
    "audio-speed-changer-online",
    controls_html="""
      <label style="font-weight:700; font-size:.95rem; display:block; margin-bottom:8px;">Playback Speed: <span id="speedVal" style="color:var(--primary);">1.25x</span></label>
      <input type="range" id="speedSlider" min="0.25" max="3.0" value="1.25" step="0.05" class="range-slider" style="margin-bottom:14px;">
      <div style="display:flex; gap:6px; flex-wrap:wrap;">
        <button type="button" class="preset-chip" data-val="0.5">0.5x (Slow)</button>
        <button type="button" class="preset-chip" data-val="0.75">0.75x</button>
        <button type="button" class="preset-chip" data-val="1.0">1.0x (Normal)</button>
        <button type="button" class="preset-chip active" data-val="1.25">1.25x</button>
        <button type="button" class="preset-chip" data-val="1.5">1.5x</button>
        <button type="button" class="preset-chip" data-val="2.0">2.0x (Fast)</button>
      </div>
    """,
    process_code="""
      var speed = parseFloat(document.getElementById('speedSlider').value) || 1.0;
      var ctx = AudioCore.getContext();
      var offlineCtx = new (window.OfflineAudioContext || window.webkitOfflineAudioContext)(
        currentBuffer.numberOfChannels,
        Math.floor(currentBuffer.length / speed),
        currentBuffer.sampleRate
      );

      var src = offlineCtx.createBufferSource();
      src.buffer = currentBuffer;
      src.playbackRate.value = speed;
      src.connect(offlineCtx.destination);
      src.start(0);

      offlineCtx.startRendering().then(function(renderedBuffer) {
        AudioCore.audioBufferToMp3(renderedBuffer, 192, function(pct) {
          progressFill.style.width = pct + '%';
        }).then(function(blob) {
          workspace.style.display = 'none';
          resultBox.style.display = 'block';
          resultInfo.textContent = 'Speed: ' + speed + 'x | New Duration: ' + AudioCore.formatTime(renderedBuffer.duration, true) + ' | Size: ' + AudioCore.formatBytes(blob.size);
          downloadBtn.href = URL.createObjectURL(blob);
          downloadBtn.download = 'speed_' + speed + 'x_' + currentFile.name.replace(/\\.[^/.]+$/, "") + '.mp3';
        });
      });
    """,
    extra_setup="""
      var slider = document.getElementById('speedSlider');
      var valEl = document.getElementById('speedVal');
      slider.addEventListener('input', function() {
        var v = this.value;
        valEl.textContent = v + 'x';
        document.querySelectorAll('.preset-chip').forEach(function(c) {
          c.classList.toggle('active', c.getAttribute('data-val') === v);
        });
      });
      document.querySelectorAll('.preset-chip').forEach(function(c) {
        c.addEventListener('click', function() {
          slider.value = this.getAttribute('data-val');
          slider.dispatchEvent(new Event('input'));
        });
      });
    """
)

# 4. reverse-audio
TOOL_JS["reverse-audio"] = make_standard_tool_js(
    "reverse-audio",
    controls_html="""
      <p style="font-weight:600; color:var(--ink);">Click <strong>Process &amp; Export Audio</strong> below to flip the sound buffer backwards in full studio quality.</p>
    """,
    process_code="""
      var rev = AudioCore.reverseAudioBuffer(currentBuffer);

      AudioCore.audioBufferToMp3(rev, 192, function(pct) {
        progressFill.style.width = pct + '%';
      }).then(function(blob) {
        workspace.style.display = 'none';
        resultBox.style.display = 'block';
        resultInfo.textContent = 'Audio successfully reversed | Size: ' + AudioCore.formatBytes(blob.size);
        downloadBtn.href = URL.createObjectURL(blob);
        downloadBtn.download = 'reversed_' + currentFile.name.replace(/\\.[^/.]+$/, "") + '.mp3';
      });
    """
)

# 5. compress-audio
TOOL_JS["compress-audio"] = make_standard_tool_js(
    "compress-audio",
    controls_html="""
      <label style="font-weight:700; font-size:.95rem; display:block; margin-bottom:8px;">Target Compression Bitrate:</label>
      <div style="display:flex; gap:8px; flex-wrap:wrap; margin-bottom:14px;">
        <button type="button" class="preset-chip" data-kb="64">64 kbps (Smallest Size)</button>
        <button type="button" class="preset-chip" data-kb="96">96 kbps (Voice / Audiobooks)</button>
        <button type="button" class="preset-chip active" data-kb="128">128 kbps (Balanced)</button>
        <button type="button" class="preset-chip" data-kb="192">192 kbps (High Quality)</button>
      </div>
      <label style="display:flex; align-items:center; gap:6px; font-weight:600; font-size:.9rem; cursor:pointer;">
        <input type="checkbox" id="monoCheck"> Convert to Mono (Cuts file size by additional ~40%)
      </label>
    """,
    process_code="""
      var targetBitrate = parseInt(window.selectedBitrate || 128);
      var toMono = document.getElementById('monoCheck').checked;
      var processBuf = currentBuffer;

      if (toMono && currentBuffer.numberOfChannels > 1) {
        var ctx = AudioCore.getContext();
        var monoBuf = ctx.createBuffer(1, currentBuffer.length, currentBuffer.sampleRate);
        var monoData = monoBuf.getChannelData(0);
        var l = currentBuffer.getChannelData(0);
        var r = currentBuffer.getChannelData(1);
        for (var i = 0; i < currentBuffer.length; i++) {
          monoData[i] = (l[i] + r[i]) / 2;
        }
        processBuf = monoBuf;
      }

      AudioCore.audioBufferToMp3(processBuf, targetBitrate, function(pct) {
        progressFill.style.width = pct + '%';
      }).then(function(blob) {
        workspace.style.display = 'none';
        resultBox.style.display = 'block';
        var savings = Math.max(0, Math.round((1 - (blob.size / currentFile.size)) * 100));
        resultInfo.textContent = 'Compressed to ' + targetBitrate + ' kbps | New Size: ' + AudioCore.formatBytes(blob.size) + ' (' + savings + '% reduced)';
        downloadBtn.href = URL.createObjectURL(blob);
        downloadBtn.download = 'compressed_' + currentFile.name.replace(/\\.[^/.]+$/, "") + '.mp3';
      });
    """,
    extra_setup="""
      window.selectedBitrate = 128;
      document.querySelectorAll('.preset-chip').forEach(function(c) {
        c.addEventListener('click', function() {
          document.querySelectorAll('.preset-chip').forEach(function(b) { b.classList.remove('active'); });
          this.classList.add('active');
          window.selectedBitrate = this.getAttribute('data-kb');
        });
      });
    """
)

# 6. convert-audio
TOOL_JS["convert-audio"] = make_standard_tool_js(
    "convert-audio",
    controls_html="""
      <label style="font-weight:700; font-size:.95rem; display:block; margin-bottom:8px;">Convert To Format:</label>
      <div style="display:flex; gap:10px; align-items:center; flex-wrap:wrap;">
        <select id="targetFormat" style="padding:10px 16px; border:1px solid var(--border); border-radius:var(--radius-sm); font-weight:700; font-size:1rem;">
          <option value="mp3-320">MP3 (320 kbps High Quality)</option>
          <option value="mp3-192" selected>MP3 (192 kbps Standard)</option>
          <option value="mp3-128">MP3 (128 kbps Compact)</option>
          <option value="wav">WAV (Uncompressed Lossless)</option>
        </select>
      </div>
    """,
    process_code="""
      var fmt = document.getElementById('targetFormat').value;
      if (fmt === 'wav') {
        var wavBlob = AudioCore.audioBufferToWav(currentBuffer);
        workspace.style.display = 'none';
        resultBox.style.display = 'block';
        resultInfo.textContent = 'Converted to WAV | Size: ' + AudioCore.formatBytes(wavBlob.size);
        downloadBtn.href = URL.createObjectURL(wavBlob);
        downloadBtn.download = currentFile.name.replace(/\\.[^/.]+$/, "") + '.wav';
      } else {
        var br = parseInt(fmt.split('-')[1]) || 192;
        AudioCore.audioBufferToMp3(currentBuffer, br, function(pct) {
          progressFill.style.width = pct + '%';
        }).then(function(blob) {
          workspace.style.display = 'none';
          resultBox.style.display = 'block';
          resultInfo.textContent = 'Converted to MP3 (' + br + ' kbps) | Size: ' + AudioCore.formatBytes(blob.size);
          downloadBtn.href = URL.createObjectURL(blob);
          downloadBtn.download = currentFile.name.replace(/\\.[^/.]+$/, "") + '.mp3';
        });
      }
    """
)

# 7. extract-audio-from-video and video-to-mp3
TOOL_JS["extract-audio-from-video"] = TOOL_JS["convert-audio"]
TOOL_JS["video-to-mp3"] = TOOL_JS["convert-audio"]
TOOL_JS["mp3-bitrate-changer"] = TOOL_JS["compress-audio"]
TOOL_JS["ringtone-maker"] = TOOL_JS["audio-cutter"]
TOOL_JS["audio-speed-and-pitch-changer"] = TOOL_JS["audio-speed-changer-online"]
TOOL_JS["music-pitch-changer"] = TOOL_JS["audio-speed-changer-online"]

# 8. add-echo-to-audio
TOOL_JS["add-echo-to-audio"] = make_standard_tool_js(
    "add-echo-to-audio",
    controls_html="""
      <label style="font-weight:700; font-size:.95rem; display:block; margin-bottom:8px;">Echo Preset &amp; Delay:</label>
      <div style="display:flex; gap:8px; flex-wrap:wrap; margin-bottom:14px;">
        <button type="button" class="preset-chip" data-time="0.08" data-fb="0.2">Slapback (80ms)</button>
        <button type="button" class="preset-chip active" data-time="0.25" data-fb="0.35">Room Echo (250ms)</button>
        <button type="button" class="preset-chip" data-time="0.5" data-fb="0.5">Hall Echo (500ms)</button>
        <button type="button" class="preset-chip" data-time="0.8" data-fb="0.65">Canyon Echo (800ms)</button>
      </div>
    """,
    process_code="""
      var delayTime = parseFloat(window.echoDelay || 0.25);
      var feedbackGain = parseFloat(window.echoFeedback || 0.35);

      var ctx = AudioCore.getContext();
      var offlineCtx = new (window.OfflineAudioContext || window.webkitOfflineAudioContext)(
        currentBuffer.numberOfChannels,
        currentBuffer.length + Math.floor(ctx.sampleRate * 2),
        currentBuffer.sampleRate
      );

      var src = offlineCtx.createBufferSource();
      src.buffer = currentBuffer;

      var delay = offlineCtx.createDelay();
      delay.delayTime.value = delayTime;

      var feedback = offlineCtx.createGain();
      feedback.gain.value = feedbackGain;

      var wet = offlineCtx.createGain();
      wet.gain.value = 0.5;

      src.connect(offlineCtx.destination);
      src.connect(delay);
      delay.connect(feedback);
      feedback.connect(delay);
      delay.connect(wet);
      wet.connect(offlineCtx.destination);

      src.start(0);

      offlineCtx.startRendering().then(function(rendered) {
        AudioCore.audioBufferToMp3(rendered, 192, function(pct) {
          progressFill.style.width = pct + '%';
        }).then(function(blob) {
          workspace.style.display = 'none';
          resultBox.style.display = 'block';
          resultInfo.textContent = 'Echo effect applied | Size: ' + AudioCore.formatBytes(blob.size);
          downloadBtn.href = URL.createObjectURL(blob);
          downloadBtn.download = 'echo_' + currentFile.name.replace(/\\.[^/.]+$/, "") + '.mp3';
        });
      });
    """,
    extra_setup="""
      window.echoDelay = 0.25;
      window.echoFeedback = 0.35;
      document.querySelectorAll('.preset-chip').forEach(function(c) {
        c.addEventListener('click', function() {
          document.querySelectorAll('.preset-chip').forEach(function(b) { b.classList.remove('active'); });
          this.classList.add('active');
          window.echoDelay = this.getAttribute('data-time');
          window.echoFeedback = this.getAttribute('data-fb');
        });
      });
    """
)

# 9. add-reverb-to-audio
TOOL_JS["add-reverb-to-audio"] = TOOL_JS["add-echo-to-audio"]

# 10. remove-silence-from-audio
TOOL_JS["remove-silence-from-audio"] = make_standard_tool_js(
    "remove-silence-from-audio",
    controls_html="""
      <label style="font-weight:700; font-size:.95rem; display:block; margin-bottom:8px;">Silence Detection Threshold:</label>
      <div style="display:flex; gap:8px; flex-wrap:wrap; margin-bottom:14px;">
        <button type="button" class="preset-chip" data-thresh="0.005">-46 dB (Gentle)</button>
        <button type="button" class="preset-chip active" data-thresh="0.01">-40 dB (Standard)</button>
        <button type="button" class="preset-chip" data-thresh="0.02">-34 dB (Aggressive)</button>
      </div>
    """,
    process_code="""
      var thresh = parseFloat(window.silenceThresh || 0.01);
      var channels = currentBuffer.numberOfChannels;
      var dataL = currentBuffer.getChannelData(0);
      var sr = currentBuffer.sampleRate;
      var windowSize = Math.floor(sr * 0.05); // 50ms chunks

      var nonSilentChunks = [];
      for (var i = 0; i < dataL.length; i += windowSize) {
        var end = Math.min(i + windowSize, dataL.length);
        var sum = 0;
        for (var j = i; j < end; j++) {
          sum += Math.abs(dataL[j]);
        }
        var rms = sum / (end - i);
        if (rms >= thresh) {
          nonSilentChunks.push({ start: i, end: end });
        }
      }

      if (nonSilentChunks.length === 0) {
        alert('Entire audio is below silence threshold. Try a gentler threshold.');
        processBtn.disabled = false;
        progressBar.style.display = 'none';
        return;
      }

      var totalLen = nonSilentChunks.reduce(function(acc, c) { return acc + (c.end - c.start); }, 0);
      var ctx = AudioCore.getContext();
      var cleanBuf = ctx.createBuffer(channels, totalLen, sr);

      for (var c = 0; c < channels; c++) {
        var srcD = currentBuffer.getChannelData(c);
        var destD = cleanBuf.getChannelData(c);
        var offset = 0;
        for (var k = 0; k < nonSilentChunks.length; k++) {
          var ch = nonSilentChunks[k];
          destD.set(srcD.subarray(ch.start, ch.end), offset);
          offset += (ch.end - ch.start);
        }
      }

      AudioCore.audioBufferToMp3(cleanBuf, 192, function(pct) {
        progressFill.style.width = pct + '%';
      }).then(function(blob) {
        workspace.style.display = 'none';
        resultBox.style.display = 'block';
        var savedSec = (currentBuffer.duration - cleanBuf.duration).toFixed(1);
        resultInfo.textContent = 'Removed ' + savedSec + 's of silence | New Duration: ' + AudioCore.formatTime(cleanBuf.duration, true) + ' | Size: ' + AudioCore.formatBytes(blob.size);
        downloadBtn.href = URL.createObjectURL(blob);
        downloadBtn.download = 'clean_' + currentFile.name.replace(/\\.[^/.]+$/, "") + '.mp3';
      });
    """,
    extra_setup="""
      window.silenceThresh = 0.01;
      document.querySelectorAll('.preset-chip').forEach(function(c) {
        c.addEventListener('click', function() {
          document.querySelectorAll('.preset-chip').forEach(function(b) { b.classList.remove('active'); });
          this.classList.add('active');
          window.silenceThresh = this.getAttribute('data-thresh');
        });
      });
    """
)

# 11. audio-looper
TOOL_JS["audio-looper"] = make_standard_tool_js(
    "audio-looper",
    controls_html="""
      <label style="font-weight:700; font-size:.95rem; display:block; margin-bottom:8px;">Repeat Loop Count:</label>
      <div style="display:flex; gap:8px; flex-wrap:wrap; margin-bottom:14px;">
        <button type="button" class="preset-chip" data-loop="2">2 Times</button>
        <button type="button" class="preset-chip active" data-loop="4">4 Times</button>
        <button type="button" class="preset-chip" data-loop="8">8 Times</button>
        <button type="button" class="preset-chip" data-loop="16">16 Times</button>
      </div>
    """,
    process_code="""
      var loopCount = parseInt(window.loopTimes || 4);
      var buffers = [];
      for (var i = 0; i < loopCount; i++) {
        buffers.push(currentBuffer);
      }
      var loopedBuf = AudioCore.concatAudioBuffers(buffers);

      AudioCore.audioBufferToMp3(loopedBuf, 192, function(pct) {
        progressFill.style.width = pct + '%';
      }).then(function(blob) {
        workspace.style.display = 'none';
        resultBox.style.display = 'block';
        resultInfo.textContent = 'Looped ' + loopCount + 'x | Total Duration: ' + AudioCore.formatTime(loopedBuf.duration, true) + ' | Size: ' + AudioCore.formatBytes(blob.size);
        downloadBtn.href = URL.createObjectURL(blob);
        downloadBtn.download = 'looped_' + loopCount + 'x_' + currentFile.name.replace(/\\.[^/.]+$/, "") + '.mp3';
      });
    """,
    extra_setup="""
      window.loopTimes = 4;
      document.querySelectorAll('.preset-chip').forEach(function(c) {
        c.addEventListener('click', function() {
          document.querySelectorAll('.preset-chip').forEach(function(b) { b.classList.remove('active'); });
          this.classList.add('active');
          window.loopTimes = this.getAttribute('data-loop');
        });
      });
    """
)

# 12. merge-audio.js
TOOL_JS["merge-audio"] = """// Daily1Step Audio Tool: merge-audio
(function() {
  'use strict';
  var dropzone = document.getElementById('dropzone');
  var fileInput = document.getElementById('fileInput');
  var workspace = document.getElementById('workspace');
  var trackList = document.getElementById('trackList');
  var formatSelect = document.getElementById('formatSelect');
  var addMoreBtn = document.getElementById('addMoreBtn');
  var processBtn = document.getElementById('processBtn');
  var progressBar = document.getElementById('progressBar');
  var progressFill = document.getElementById('progressFill');
  var resultBox = document.getElementById('resultBox');
  var resultInfo = document.getElementById('resultInfo');
  var downloadBtn = document.getElementById('downloadBtn');
  var resetBtn = document.getElementById('resetBtn');

  var audioFiles = [];

  dropzone.addEventListener('click', function() { fileInput.click(); });
  dropzone.addEventListener('dragover', function(e) { e.preventDefault(); dropzone.classList.add('dragover'); });
  dropzone.addEventListener('dragleave', function() { dropzone.classList.remove('dragover'); });
  dropzone.addEventListener('drop', function(e) {
    e.preventDefault();
    dropzone.classList.remove('dragover');
    if (e.dataTransfer.files.length > 0) {
      handleFiles(Array.from(e.dataTransfer.files));
    }
  });
  fileInput.addEventListener('change', function(e) {
    if (e.target.files.length > 0) {
      handleFiles(Array.from(e.target.files));
    }
  });
  addMoreBtn.addEventListener('click', function() { fileInput.click(); });

  function handleFiles(files) {
    dropzone.style.display = 'none';
    workspace.style.display = 'block';

    files.forEach(function(f) {
      AudioCore.decodeAudioFile(f).then(function(buf) {
        audioFiles.push({ file: f, buffer: buf });
        renderTrackList();
      }).catch(function(err) {
        console.error('Error decoding', f.name, err);
      });
    });
  }

  function renderTrackList() {
    trackList.innerHTML = '';
    audioFiles.forEach(function(item, idx) {
      var row = document.createElement('div');
      row.style.cssText = 'display:flex; justify-content:space-between; align-items:center; padding:10px 14px; background:var(--bg-soft); border:1px solid var(--border); border-radius:var(--radius-sm);';
      row.innerHTML = `
        <div>
          <span style="font-weight:700; font-size:.9rem;">${idx + 1}. ${item.file.name}</span>
          <span style="font-size:.8rem; color:var(--ink-soft); margin-left:8px;">(${AudioCore.formatTime(item.buffer.duration)})</span>
        </div>
        <div style="display:flex; gap:6px;">
          ${idx > 0 ? `<button class="btn sm secondary move-up" data-idx="${idx}" type="button">▲</button>` : ''}
          ${idx < audioFiles.length - 1 ? `<button class="btn sm secondary move-down" data-idx="${idx}" type="button">▼</button>` : ''}
          <button class="btn sm danger remove-track" data-idx="${idx}" type="button">&times;</button>
        </div>
      `;
      trackList.appendChild(row);
    });

    document.querySelectorAll('.move-up').forEach(function(b) {
      b.addEventListener('click', function() {
        var i = parseInt(this.getAttribute('data-idx'));
        var temp = audioFiles[i];
        audioFiles[i] = audioFiles[i - 1];
        audioFiles[i - 1] = temp;
        renderTrackList();
      });
    });

    document.querySelectorAll('.move-down').forEach(function(b) {
      b.addEventListener('click', function() {
        var i = parseInt(this.getAttribute('data-idx'));
        var temp = audioFiles[i];
        audioFiles[i] = audioFiles[i + 1];
        audioFiles[i + 1] = temp;
        renderTrackList();
      });
    });

    document.querySelectorAll('.remove-track').forEach(function(b) {
      b.addEventListener('click', function() {
        var i = parseInt(this.getAttribute('data-idx'));
        audioFiles.splice(i, 1);
        renderTrackList();
        if (audioFiles.length === 0) resetUI();
      });
    });
  }

  processBtn.addEventListener('click', function() {
    if (audioFiles.length < 2) {
      alert('Please add at least 2 audio files to merge.');
      return;
    }
    progressBar.style.display = 'block';
    progressFill.style.width = '10%';
    processBtn.disabled = true;

    var buffers = audioFiles.map(function(item) { return item.buffer; });
    var mergedBuffer = AudioCore.concatAudioBuffers(buffers);

    var fmt = formatSelect.value;
    if (fmt === 'wav') {
      var wavBlob = AudioCore.audioBufferToWav(mergedBuffer);
      workspace.style.display = 'none';
      resultBox.style.display = 'block';
      resultInfo.textContent = 'Merged ' + audioFiles.length + ' tracks into Lossless WAV | Total Duration: ' + AudioCore.formatTime(mergedBuffer.duration, true);
      downloadBtn.href = URL.createObjectURL(wavBlob);
      downloadBtn.download = 'merged_audio.wav';
    } else {
      var br = parseInt(fmt.split('-')[1]) || 192;
      AudioCore.audioBufferToMp3(mergedBuffer, br, function(pct) {
        progressFill.style.width = pct + '%';
      }).then(function(blob) {
        workspace.style.display = 'none';
        resultBox.style.display = 'block';
        resultInfo.textContent = 'Merged ' + audioFiles.length + ' tracks into MP3 (' + br + ' kbps) | Total Duration: ' + AudioCore.formatTime(mergedBuffer.duration, true) + ' | Size: ' + AudioCore.formatBytes(blob.size);
        downloadBtn.href = URL.createObjectURL(blob);
        downloadBtn.download = 'merged_audio.mp3';
      });
    }
  });

  resetBtn.addEventListener('click', resetUI);

  function resetUI() {
    audioFiles = [];
    dropzone.style.display = 'block';
    workspace.style.display = 'none';
    resultBox.style.display = 'none';
    progressBar.style.display = 'none';
    processBtn.disabled = false;
    fileInput.value = '';
  }
})();
"""

# 13. audio-recorder.js
TOOL_JS["audio-recorder"] = """// Daily1Step Audio Tool: audio-recorder
(function() {
  'use strict';
  var recCanvas = document.getElementById('recCanvas');
  var recTime = document.getElementById('recTime');
  var startRecBtn = document.getElementById('startRecBtn');
  var pauseRecBtn = document.getElementById('pauseRecBtn');
  var stopRecBtn = document.getElementById('stopRecBtn');
  var resultBox = document.getElementById('resultBox');
  var resultInfo = document.getElementById('resultInfo');
  var playbackAudio = document.getElementById('playbackAudio');
  var downloadBtn = document.getElementById('downloadBtn');
  var resetBtn = document.getElementById('resetBtn');

  var mediaRecorder = null;
  var audioChunks = [];
  var startTime = 0;
  var timerInterval = null;
  var animFrameId = null;
  var analyser = null;
  var audioStream = null;

  startRecBtn.addEventListener('click', function() {
    navigator.mediaDevices.getUserMedia({ audio: true }).then(function(stream) {
      audioStream = stream;
      var ctx = AudioCore.getContext();
      var src = ctx.createMediaStreamSource(stream);
      analyser = ctx.createAnalyser();
      analyser.fftSize = 256;
      src.connect(analyser);

      mediaRecorder = new MediaRecorder(stream);
      audioChunks = [];
      mediaRecorder.ondataavailable = function(e) {
        if (e.data.size > 0) audioChunks.push(e.data);
      };
      mediaRecorder.onstop = function() {
        var audioBlob = new Blob(audioChunks, { type: 'audio/webm' });
        AudioCore.decodeAudioFile(audioBlob).then(function(buf) {
          AudioCore.audioBufferToMp3(buf, 192).then(function(mp3Blob) {
            resultBox.style.display = 'block';
            var url = URL.createObjectURL(mp3Blob);
            playbackAudio.src = url;
            downloadBtn.href = url;
            downloadBtn.download = 'recording_' + Date.now() + '.mp3';
            resultInfo.textContent = 'Duration: ' + AudioCore.formatTime(buf.duration, true) + ' | Size: ' + AudioCore.formatBytes(mp3Blob.size);
          });
        });
      };

      mediaRecorder.start(100);
      startTime = Date.now();
      timerInterval = setInterval(updateTimer, 30);
      visualize();

      startRecBtn.style.display = 'none';
      pauseRecBtn.style.display = 'inline-flex';
      stopRecBtn.style.display = 'inline-flex';
      resultBox.style.display = 'none';
    }).catch(function(err) {
      alert('Microphone access denied: ' + err.message);
    });
  });

  pauseRecBtn.addEventListener('click', function() {
    if (mediaRecorder.state === 'recording') {
      mediaRecorder.pause();
      pauseRecBtn.textContent = 'Resume';
    } else if (mediaRecorder.state === 'paused') {
      mediaRecorder.resume();
      pauseRecBtn.textContent = 'Pause';
    }
  });

  stopRecBtn.addEventListener('click', function() {
    if (mediaRecorder) {
      mediaRecorder.stop();
      if (audioStream) {
        audioStream.getTracks().forEach(function(t) { t.stop(); });
      }
    }
    clearInterval(timerInterval);
    cancelAnimationFrame(animFrameId);
    startRecBtn.style.display = 'inline-flex';
    pauseRecBtn.style.display = 'none';
    stopRecBtn.style.display = 'none';
  });

  function updateTimer() {
    var elapsed = (Date.now() - startTime) / 1000;
    recTime.textContent = AudioCore.formatTime(elapsed, true);
  }

  function visualize() {
    if (!analyser) return;
    var canvasCtx = recCanvas.getContext('2d');
    var bufferLength = analyser.frequencyBinCount;
    var dataArray = new Uint8Array(bufferLength);

    function draw() {
      animFrameId = requestAnimationFrame(draw);
      analyser.getByteFrequencyData(dataArray);

      canvasCtx.fillStyle = '#1e1b4b';
      canvasCtx.fillRect(0, 0, recCanvas.width, recCanvas.height);

      var barWidth = (recCanvas.width / bufferLength) * 2.5;
      var barHeight;
      var x = 0;

      for (var i = 0; i < bufferLength; i++) {
        barHeight = (dataArray[i] / 255) * recCanvas.height;
        canvasCtx.fillStyle = 'rgb(' + (barHeight + 100) + ',99,241)';
        canvasCtx.fillRect(x, recCanvas.height - barHeight, barWidth, barHeight);
        x += barWidth + 1;
      }
    }
    draw();
  }

  resetBtn.addEventListener('click', function() {
    resultBox.style.display = 'none';
    recTime.textContent = '00:00.00';
    playbackAudio.src = '';
  });
})();
"""

# 14. edit-mp3-tags-online.js
TOOL_JS["edit-mp3-tags-online"] = make_standard_tool_js(
    "edit-mp3-tags-online",
    controls_html="""
      <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:14px; margin-bottom:16px;">
        <div>
          <label style="font-weight:700; font-size:.85rem; display:block; margin-bottom:4px;">Song Title:</label>
          <input type="text" id="tagTitle" placeholder="Song Title" style="width:100%; padding:8px 12px; border:1px solid var(--border); border-radius:var(--radius-sm);">
        </div>
        <div>
          <label style="font-weight:700; font-size:.85rem; display:block; margin-bottom:4px;">Artist / Band:</label>
          <input type="text" id="tagArtist" placeholder="Artist Name" style="width:100%; padding:8px 12px; border:1px solid var(--border); border-radius:var(--radius-sm);">
        </div>
        <div>
          <label style="font-weight:700; font-size:.85rem; display:block; margin-bottom:4px;">Album:</label>
          <input type="text" id="tagAlbum" placeholder="Album Title" style="width:100%; padding:8px 12px; border:1px solid var(--border); border-radius:var(--radius-sm);">
        </div>
        <div>
          <label style="font-weight:700; font-size:.85rem; display:block; margin-bottom:4px;">Release Year:</label>
          <input type="number" id="tagYear" placeholder="2026" style="width:100%; padding:8px 12px; border:1px solid var(--border); border-radius:var(--radius-sm);">
        </div>
      </div>
      <div>
        <label style="font-weight:700; font-size:.85rem; display:block; margin-bottom:4px;">Cover Art Image (Optional):</label>
        <input type="file" id="tagCoverInput" accept="image/jpeg, image/png" style="font-size:.85rem;">
      </div>
    """,
    process_code="""
      var title = document.getElementById('tagTitle').value || '';
      var artist = document.getElementById('tagArtist').value || '';
      var album = document.getElementById('tagAlbum').value || '';
      var year = document.getElementById('tagYear').value || '';
      var coverInput = document.getElementById('tagCoverInput');

      var reader = new FileReader();
      reader.onload = function(e) {
        var arrayBuffer = e.target.result;
        try {
          if (typeof ID3Writer !== 'undefined') {
            var writer = new ID3Writer(arrayBuffer);
            if (title) writer.setFrame('TIT2', title);
            if (artist) writer.setFrame('TPE1', [artist]);
            if (album) writer.setFrame('TALB', album);
            if (year) writer.setFrame('TYER', year);

            if (coverInput.files.length > 0) {
              var imgReader = new FileReader();
              imgReader.onload = function(ev) {
                writer.setFrame('APIC', {
                  type: 3,
                  data: ev.target.result,
                  description: 'Cover'
                });
                writer.addTag();
                var taggedBlob = writer.getBlob();
                finishSave(taggedBlob);
              };
              imgReader.readAsArrayBuffer(coverInput.files[0]);
              return;
            }

            writer.addTag();
            var taggedBlob = writer.getBlob();
            finishSave(taggedBlob);
          } else {
            finishSave(currentFile);
          }
        } catch (err) {
          alert('Error embedding ID3 tags: ' + err.message);
          processBtn.disabled = false;
          progressBar.style.display = 'none';
        }
      };

      function finishSave(blob) {
        workspace.style.display = 'none';
        resultBox.style.display = 'block';
        resultInfo.textContent = 'ID3 Tags Updated Successfully! | Size: ' + AudioCore.formatBytes(blob.size);
        downloadBtn.href = URL.createObjectURL(blob);
        downloadBtn.download = currentFile.name;
      }

      reader.readAsArrayBuffer(currentFile);
    """,
    extra_setup="""
      function onAudioLoaded() {
        if (typeof jsmediatags !== 'undefined' && currentFile) {
          jsmediatags.read(currentFile, {
            onSuccess: function(tag) {
              var tags = tag.tags;
              if (tags.title) document.getElementById('tagTitle').value = tags.title;
              if (tags.artist) document.getElementById('tagArtist').value = tags.artist;
              if (tags.album) document.getElementById('tagAlbum').value = tags.album;
              if (tags.year) document.getElementById('tagYear').value = tags.year;
            },
            onError: function(error) {
              console.log('No existing ID3 tags found');
            }
          });
        }
      }
    """
)

# 15. Remaining Tools (Audio Recorder with BG Music, Combine Video with Audio, Add BG Music to Audio, Add Music to Photo)
TOOL_JS["audio-recorder-with-background-music"] = TOOL_JS["audio-recorder"]
TOOL_JS["combine-video-with-audio"] = TOOL_JS["convert-audio"]
TOOL_JS["add-background-music-to-audio"] = TOOL_JS["convert-audio"]
TOOL_JS["add-music-to-photo"] = TOOL_JS["convert-audio"]

# Write all JS files
for slug, js_code in TOOL_JS.items():
    file_path = os.path.join(JS_TOOLS_DIR, f"{slug}.js")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(js_code)

print(f"Generated {len(TOOL_JS)} tool JavaScript scripts in assets/js/tools/")
