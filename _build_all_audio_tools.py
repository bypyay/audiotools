import os
import json

BASE_DIR = r"D:\Codding\Claude Cowork code\Audio Tools"
TOOLS_DIR = os.path.join(BASE_DIR, "tools")
JS_TOOLS_DIR = os.path.join(BASE_DIR, "assets", "js", "tools")

os.makedirs(TOOLS_DIR, exist_ok=True)
os.makedirs(JS_TOOLS_DIR, exist_ok=True)

# List of all 23 Audio Tools with full metadata, categories, icons, and SEO configuration
AUDIO_TOOLS = [
    # 1. Cut & Trim
    {
        "slug": "audio-cutter",
        "name": "Audio Cutter & Trimmer",
        "short_name": "Audio Cutter",
        "category": "cut",
        "color": "#6366f1",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><line x1="20" y1="4" x2="8.12" y2="15.88"/><line x1="14.47" y1="14.48" x2="20" y2="20"/><line x1="8.12" y1="8.12" x2="12" y2="12"/></svg>',
        "title": "Audio Cutter Online Free — Cut MP3 & Trim Music Tracks",
        "desc": "Cut, trim, and split MP3, WAV, AAC, and audio files online for free. Drag interactive waveform handles, preview in real-time, and download instant high-quality audio.",
        "h1": "Free Online Audio Cutter & MP3 Trimmer",
        "tagline": "Trim, cut, and crop songs or recordings with millisecond precision directly in your web browser.",
        "faqs": [
            ("How do I cut an audio file online?", "Simply drag and drop your MP3, WAV, or audio file into the dropzone. Use the interactive waveform visualizer to drag the start and end markers to your desired section, listen to the preview, and click 'Download Cut Audio'."),
            ("Is this audio cutter safe and private?", "Yes, 100%! Daily1Step Audio Cutter processes your audio completely in your browser using the HTML5 Web Audio API. Your files are never uploaded to any cloud server."),
            ("What audio formats are supported?", "We support MP3, WAV, AAC, M4A, OGG, FLAC, WMA, and WebM audio files."),
            ("Can I create smartphone ringtones with this tool?", "Yes! You can trim your favorite 30-second chorus and save it directly as an MP3 or WAV ringtone.")
        ]
    },
    {
        "slug": "merge-audio",
        "name": "Merge Audio Files",
        "short_name": "Merge Audio",
        "category": "cut",
        "color": "#8b5cf6",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M8 3v3a2 2 0 0 1-2 2H3"/><path d="M21 8h-3a2 2 0 0 1-2-2V3"/><path d="M3 16h3a2 2 0 0 1 2 2v3"/><path d="M16 21v-3a2 2 0 0 1 2-2h3"/><line x1="12" y1="8" x2="12" y2="16"/></svg>',
        "title": "Merge Audio Files Online Free — Join Multiple Songs into One MP3",
        "desc": "Combine and merge multiple audio files into a single song or podcast track online. Drag to reorder tracks, add smooth crossfades, and export high-quality MP3.",
        "h1": "Merge Audio Files Online for Free",
        "tagline": "Combine multiple songs, voice recordings, and sound clips into one seamless audio track with zero quality loss.",
        "faqs": [
            ("How many audio files can I merge together?", "You can merge unlimited audio tracks simultaneously. Simply select multiple files and reorder them as needed."),
            ("Can I merge different audio formats together (e.g. MP3 + WAV)?", "Yes! Our audio engine automatically converts and normalizes sample rates across all uploaded files to create a unified audio output."),
            ("Does it support crossfading between tracks?", "Yes, you can enable smooth transition crossfades to blend consecutive songs seamlessly.")
        ]
    },
    {
        "slug": "ringtone-maker",
        "name": "Ringtone Maker",
        "short_name": "Ringtone Maker",
        "category": "cut",
        "color": "#ec4899",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 0 1-3.46 0"/></svg>',
        "title": "Online Ringtone Maker — Create Free Custom Ringtones for iPhone & Android",
        "desc": "Turn any song into a custom ringtone online. Select a 30-second chorus, add smooth fade-in and fade-out effects, and download for iPhone (M4R) or Android (MP3).",
        "h1": "Free Online Ringtone Maker",
        "tagline": "Create custom ringtones, alarm tones, and notification alerts from your favorite MP3 music in seconds.",
        "faqs": [
            ("How long should a custom ringtone be?", "Smartphone ringtones typically range between 20 to 30 seconds for optimal looping during incoming calls."),
            ("How do I make a ringtone for my iPhone?", "Trim your desired audio section, enable fade-in and fade-out effects, and export the file. You can then set it as your ringtone via iTunes or GarageBand on iOS."),
            ("What are fade-in and fade-out effects?", "Fade-in gradually raises the volume from zero at the beginning so the ringtone doesn't start abruptly, while fade-out gently lowers the volume at the end.")
        ]
    },
    {
        "slug": "remove-silence-from-audio",
        "name": "Remove Silence from Audio",
        "short_name": "Remove Silence",
        "category": "cut",
        "color": "#06b6d4",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="1" y1="1" x2="23" y2="23"/><path d="M9 9v3a3 3 0 0 0 5.12 2.12M15 9.34V4a3 3 0 0 0-5.94-.6"/></svg>',
        "title": "Remove Silence from Audio Online — Auto-Detect & Strip Silent Gaps",
        "desc": "Automatically detect and remove dead pauses and quiet silence gaps from podcasts, voice-overs, and audio recordings. Speed up listening and clean up takes instantly.",
        "h1": "Remove Silence & Dead Air from Audio",
        "tagline": "Clean up voice recordings, lectures, and podcast tracks by automatically stripping silent gaps with smart decibel thresholding.",
        "faqs": [
            ("How does automatic silence detection work?", "The tool scans the audio's PCM waveform and identifies any consecutive samples that stay below your selected decibel threshold (e.g. -40dB), trimming them out automatically."),
            ("Can I customize the silence sensitivity?", "Yes! You can adjust both the silence decibel threshold and the minimum silence duration (e.g. 0.3s) to prevent clipping natural breathing pauses.")
        ]
    },
    {
        "slug": "reverse-audio",
        "name": "Reverse Audio",
        "short_name": "Reverse Audio",
        "category": "cut",
        "color": "#f59e0b",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="11 17 6 12 11 7"/><polyline points="18 17 13 12 18 7"/></svg>',
        "title": "Reverse Audio Online Free — Play Audio & MP3 Backwards",
        "desc": "Play any song or voice clip backwards online. Invert audio waveforms to create mysterious reverse sound effects, backwards music, and backward vocal tracks.",
        "h1": "Reverse Audio & Play Songs Backwards",
        "tagline": "Flip your audio backwards in 1 click to create eerie sound effects, backward vocals, and creative music transitions.",
        "faqs": [
            ("What does reversing audio do?", "It mirrors the audio buffer from the last sample to the first sample, creating the classic 'backwards playback' effect used in movies and creative music production."),
            ("Does it change the audio pitch or quality?", "No, reversing audio preserves the exact pitch, sample rate, and audio fidelity.")
        ]
    },

    # 2. Effects & Speed
    {
        "slug": "mp3-volume-booster",
        "name": "Increase Audio Volume (MP3 Booster)",
        "short_name": "Volume Booster",
        "category": "effects",
        "color": "#10b981",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>',
        "title": "Increase Audio Volume Online — MP3 Volume Booster up to 500%",
        "desc": "Boost low audio volume and amplify quiet MP3, WAV, and audio files online. Increase loudness up to 500% (+20dB) with built-in soft-clipping limiter to prevent distortion.",
        "h1": "Free Online MP3 Volume Booster",
        "tagline": "Make quiet music, voice memos, and recorded lectures louder with smart distortion-free volume amplification.",
        "faqs": [
            ("How much can I boost the volume?", "You can boost your audio volume from 100% up to 500% (or up to +20dB)."),
            ("Will boosting audio volume cause distortion or buzzing?", "Our volume booster utilizes an intelligent soft-clipping limiter to minimize harsh clipping distortion when amplifying quiet recordings.")
        ]
    },
    {
        "slug": "audio-speed-changer-online",
        "name": "Change Audio Speed",
        "short_name": "Audio Speed",
        "category": "effects",
        "color": "#3b82f6",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>',
        "title": "Change Audio Speed Online Free — Speed Up or Slow Down MP3",
        "desc": "Speed up or slow down songs, podcasts, and voice recordings online. Adjust tempo from 0.25x (slow motion) to 3.0x (fast forward) with optional pitch preservation.",
        "h1": "Change Audio Speed Online",
        "tagline": "Speed up audio for fast learning or slow down complex musical passages for easy ear training and transcription.",
        "faqs": [
            ("Can I speed up audio without changing pitch?", "Yes! You can adjust the playback rate with pitch lock enabled so voices don't sound like chipmunks when sped up."),
            ("What speed presets are available?", "You can choose popular presets like 0.5x, 0.75x, 1.25x, 1.5x, 2.0x, or customize the exact speed multiplier slider.")
        ]
    },
    {
        "slug": "music-pitch-changer",
        "name": "Change Audio Pitch (Key Transposer)",
        "short_name": "Pitch Changer",
        "category": "effects",
        "color": "#8b5cf6",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/></svg>',
        "title": "Change Audio Pitch Online — Transpose Music Key & Pitch Shifter",
        "desc": "Change audio pitch and transpose musical keys online for free. Shift pitch by semitones (-12 to +12) or fine-tune cents without altering the song speed or tempo.",
        "h1": "Online Audio Pitch Shifter & Key Transposer",
        "tagline": "Transpose backing tracks to match your vocal range or fine-tune instrument pitch without changing tempo.",
        "faqs": [
            ("What is a semitone in pitch shifting?", "One semitone represents a half-step on a musical scale (e.g. from C to C#). Shifting by +12 semitones raises the song by an entire octave."),
            ("Why use a pitch changer?", "Singers use pitch changers to transpose karaoke and backing tracks to fit their comfortable vocal range without having to sing off-key.")
        ]
    },
    {
        "slug": "audio-speed-and-pitch-changer",
        "name": "Speed & Pitch Changer",
        "short_name": "Speed & Pitch",
        "category": "effects",
        "color": "#a855f7",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 8v8"/><path d="m8 12 4-4 4 4"/></svg>',
        "title": "Audio Speed & Pitch Changer Online — Dual Tempo & Key Editor",
        "desc": "Simultaneously adjust audio speed and musical pitch online. Modify playback tempo and pitch key independently with real-time waveform preview and instant download.",
        "h1": "Change Audio Speed & Pitch Simultaneously",
        "tagline": "The ultimate dual audio modifier for dancers, musicians, language learners, and video editors.",
        "faqs": [
            ("How do speed and pitch interact?", "Our tool allows you to adjust both sliders independently—you can speed up a track while lowering its pitch, or slow it down while transposing the key up.")
        ]
    },
    {
        "slug": "add-echo-to-audio",
        "name": "Add Echo to Audio",
        "short_name": "Add Echo",
        "category": "effects",
        "color": "#d97706",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 12h2a8 8 0 0 1 8 8v2"/><path d="M2 7h2a13 13 0 0 1 13 13v2"/><path d="M2 2h2a18 18 0 0 1 18 18v2"/></svg>',
        "title": "Add Echo Effect to Audio Online — Delay & Feedback FX",
        "desc": "Add rich echo and delay effects to vocal tracks and music online. Choose slapback, room delay, canyon echo, and adjust delay time and feedback decay in real time.",
        "h1": "Add Echo & Delay Effect to Audio",
        "tagline": "Infuse your voice recordings, vocal hooks, and instruments with lush slapback, canyon echo, and rhythmic delay effects.",
        "faqs": [
            ("What is slapback echo?", "Slapback is a short delay (usually 70ms to 120ms) with low feedback, famously used in vintage rock, rockabilly, and podcast voice presence.")
        ]
    },
    {
        "slug": "add-reverb-to-audio",
        "name": "Add Reverb to Audio",
        "short_name": "Add Reverb",
        "category": "effects",
        "color": "#4f46e5",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"/><line x1="4" y1="22" x2="4" y2="15"/></svg>',
        "title": "Add Reverb to Audio Online — Studio, Chamber, Hall & Cave Spaces",
        "desc": "Add realistic acoustic space and convolution reverb to dry vocals and instruments. Choose from Studio Booth, Warm Room, Concert Hall, Cathedral, and Deep Cave presets.",
        "h1": "Add Reverb & Acoustic Space to Audio",
        "tagline": "Transform flat, dry bedroom recordings into professional studio, concert hall, and cathedral master tracks.",
        "faqs": [
            ("What is the difference between Echo and Reverb?", "Echo creates distinct, audible repetitions of a sound delayed over time, while Reverb simulates thousands of microscopic acoustic reflections inside a physical room.")
        ]
    },
    {
        "slug": "audio-looper",
        "name": "Audio Looper",
        "short_name": "Audio Looper",
        "category": "effects",
        "color": "#059669",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="17 1 21 5 17 9"/><path d="M3 11V9a4 4 0 0 1 4-4h14"/><polyline points="7 23 3 19 7 15"/><path d="M21 13v2a4 4 0 0 1-4 4H3"/></svg>',
        "title": "Audio Looper Online — Loop Audio & Music Seamlessly",
        "desc": "Loop music loops, drum beats, nature sounds, and meditation tracks online. Set repeat counts (2x to 50x) with seamless crossfade looping to eliminate clicks.",
        "h1": "Free Online Audio & Music Looper",
        "tagline": "Repeat drum patterns, ambient sounds, and backing tracks seamlessly with automatic zero-crossing crossfade.",
        "faqs": [
            ("How does seamless looping work?", "Our audio looper applies a subtle crossfade curve between the end of each iteration and the start of the next, preventing annoying clicks or popping sounds.")
        ]
    },

    # 3. Record & Mix
    {
        "slug": "audio-recorder",
        "name": "Online Voice Recorder",
        "short_name": "Voice Recorder",
        "category": "record",
        "color": "#e11d48",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" y1="19" x2="12" y2="23"/><line x1="8" y1="23" x2="16" y2="23"/></svg>',
        "title": "Online Voice Recorder — Record High-Quality Audio from Mic to MP3",
        "desc": "Record clear voice memos, podcast interviews, and vocal takes directly from your microphone online. Live audio waveform monitor, pause/resume, and instant MP3/WAV download.",
        "h1": "Free Online Voice & Audio Recorder",
        "tagline": "Studio-quality microphone recording in your browser with real-time waveform visualization and zero file limits.",
        "faqs": [
            ("Is there any recording time limit?", "No! You can record for as long as your device memory allows—from quick 5-second voice memos to 2-hour podcast episodes."),
            ("Does the recorder send my voice to a server?", "Never. The audio is captured via HTML5 MediaStream and encoded into MP3 locally in your browser.")
        ]
    },
    {
        "slug": "audio-recorder-with-background-music",
        "name": "Voice Recorder with Background Music",
        "short_name": "Recorder + Music",
        "category": "record",
        "color": "#c026d3",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><path d="M9 18V5l12-2v13"/></svg>',
        "title": "Record Voice with Background Music Online — Podcast & Meditation",
        "desc": "Record your voice live while hearing and mixing background music. Pick from lo-fi, acoustic, ambient, or upload your own track. Export mixed high-res MP3.",
        "h1": "Record Voice with Background Music",
        "tagline": "Record professional podcasts, spoken word, guided meditations, and stories with live backing music beds.",
        "faqs": [
            ("Can I upload my own background music track?", "Yes! You can choose from our built-in ambient presets or upload any custom MP3/WAV backing track.")
        ]
    },
    {
        "slug": "add-background-music-to-audio",
        "name": "Add Background Music to Audio",
        "short_name": "Add BG Music",
        "category": "record",
        "color": "#0284c7",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="5.5" cy="17.5" r="2.5"/><circle cx="17.5" cy="15.5" r="2.5"/><path d="M8 17V5l12-2v12"/></svg>',
        "title": "Add Background Music to Audio Online — Voice & Music Mixer",
        "desc": "Mix an existing voice recording with a background music track online. Adjust the volume ratio (ducking) to ensure speech stays clear and download unified MP3.",
        "h1": "Add Background Music to Voice Recordings",
        "tagline": "Elevate audiobooks, video voiceovers, and presentations by blending relaxing background music behind speech.",
        "faqs": [
            ("How do I make sure the music isn't too loud?", "Our dual volume sliders allow you to lower the music track volume (e.g. to 20-30%) while keeping your voice track loud and punchy (100%).")
        ]
    },

    # 4. Video & Music
    {
        "slug": "extract-audio-from-video",
        "name": "Extract Audio from Video",
        "short_name": "Extract Audio",
        "category": "video",
        "color": "#e5322d",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="2.18" ry="2.18"/><line x1="7" y1="2" x2="7" y2="22"/><line x1="17" y1="2" x2="17" y2="22"/><line x1="2" y1="12" x2="22" y2="12"/></svg>',
        "title": "Extract Audio from Video Online Free — Video to Audio Converter",
        "desc": "Extract sound and music tracks from MP4, WebM, MKV, MOV, and AVI videos online for free. Fast browser-based extraction with MP3 and WAV export.",
        "h1": "Extract Audio from Video Files Online",
        "tagline": "Rip background music, dialogues, and sound effects from any video file without uploading gigabytes to a server.",
        "faqs": [
            ("What video formats can I extract audio from?", "We support MP4, WebM, MKV, MOV, AVI, FLV, and 3GP video files."),
            ("Will the extracted audio lose quality?", "No, the audio is decoded directly from the video stream into uncompressed PCM and exported at up to 320 kbps MP3 or lossless WAV.")
        ]
    },
    {
        "slug": "video-to-mp3",
        "name": "Video to MP3 Converter",
        "short_name": "Video to MP3",
        "category": "video",
        "color": "#ea580c",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2" ry="2"/></svg>',
        "title": "Video to MP3 Converter Online Free — Fast MP4 to MP3 Audio",
        "desc": "Convert video clips to high-bitrate MP3 audio online. Drop MP4, MOV, or WebM files and download clean 320 kbps, 192 kbps, or 128 kbps MP3 files in seconds.",
        "h1": "Fast Online Video to MP3 Converter",
        "tagline": "Turn music videos, webinars, and lectures into standalone MP3 audio files for offline listening on any device.",
        "faqs": [
            ("How fast is the video to MP3 conversion?", "Because all processing occurs directly on your computer via Web Audio decoding, conversion takes only a few seconds even for large videos.")
        ]
    },
    {
        "slug": "combine-video-with-audio",
        "name": "Combine Video with Audio",
        "short_name": "Combine Video + Audio",
        "category": "video",
        "color": "#7c3aed",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="2"/><path d="m10 15 5-3-5-3v6z"/></svg>',
        "title": "Combine Video with Audio Online — Replace or Add Audio to Video",
        "desc": "Merge any audio track with any video file online. Replace bad video sound or layer background music on top of existing video audio and export MP4.",
        "h1": "Combine Video with Audio Online",
        "tagline": "Add background scores, replace muted video audio, or dub voiceovers over your video clips effortlessly.",
        "faqs": [
            ("Can I replace the original video audio?", "Yes! You can either mute the original video audio completely or blend the new audio track alongside it.")
        ]
    },
    {
        "slug": "add-music-to-photo",
        "name": "Add Music to Photo",
        "short_name": "Music to Photo",
        "category": "video",
        "color": "#db2777",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><path d="M21 15l-5-5L5 21"/></svg>',
        "title": "Add Music to Photo Online — Turn Picture + Song into MP4 Video",
        "desc": "Combine a photo and audio song into an MP4 video clip online. Choose 1:1 Square (Instagram), 9:16 (TikTok/Reels/Shorts), or 16:9 (YouTube) format.",
        "h1": "Add Music to Photo & Create MP4 Video",
        "tagline": "Turn still album art, photography, and quote pictures into shareable video clips with your favorite soundtrack.",
        "faqs": [
            ("What formats can I export the photo video as?", "The output is exported as standard WebM/MP4 video, compatible with Instagram Stories, YouTube Shorts, and TikTok.")
        ]
    },

    # 5. Convert, Compress & Tags
    {
        "slug": "compress-audio",
        "name": "Compress Audio",
        "short_name": "Compress Audio",
        "category": "convert",
        "color": "#e5322d",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 14.899A7 7 0 1 1 15.71 8h1.79a4.5 4.5 0 0 1 2.5 8.242"/><path d="M12 12v9"/><path d="m8 17 4 4 4-4"/></svg>',
        "title": "Compress Audio Online Free — Reduce MP3 & Audio File Size",
        "desc": "Reduce audio file size online without noticeable quality loss. Downsample bitrates (64k, 96k, 128k, 192k) and sample rates to make audio lightweight for sharing.",
        "h1": "Compress Audio & Reduce File Size Online",
        "tagline": "Shrink bulky audio recordings, voice notes, and songs to fit email attachments, web upload limits, and mobile storage.",
        "faqs": [
            ("How much file size can I save?", "You can typically reduce file size by 50% to 80% by selecting a 128 kbps or 96 kbps bitrate while maintaining high speech clarity.")
        ]
    },
    {
        "slug": "convert-audio",
        "name": "Audio Converter",
        "short_name": "Audio Converter",
        "category": "convert",
        "color": "#16a34a",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12a9 9 0 0 0-9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/><path d="M3 12a9 9 0 0 0 9 9 9.75 9.75 0 0 0 6.74-2.74L21 16"/><path d="M21 21v-5h-5"/></svg>',
        "title": "Online Audio Converter — Convert MP3, WAV, AAC, M4A, OGG, FLAC",
        "desc": "Convert audio files between all popular formats online for free. Convert WAV to MP3, M4A to MP3, AAC to WAV, and OGG to MP3 in your web browser.",
        "h1": "Free Online Audio Format Converter",
        "tagline": "Universal client-side audio transcoder supporting all major modern audio containers with custom bitrate selection.",
        "faqs": [
            ("What formats can I convert between?", "You can convert between MP3, WAV, AAC, M4A, OGG, WebM, and FLAC.")
        ]
    },
    {
        "slug": "mp3-bitrate-changer",
        "name": "MP3 Bitrate Changer",
        "short_name": "Bitrate Changer",
        "category": "convert",
        "color": "#d97706",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="6" width="20" height="12" rx="2"/><line x1="6" y1="6" x2="6" y2="10"/><line x1="10" y1="6" x2="10" y2="8"/><line x1="14" y1="6" x2="14" y2="10"/><line x1="18" y1="6" x2="18" y2="8"/></svg>',
        "title": "MP3 Bitrate Changer Online — Change Bitrate (64k to 320k kbps)",
        "desc": "Change MP3 audio bitrate online to optimize audio fidelity or reduce size. Re-encode MP3s to 64, 96, 128, 160, 192, 256, or 320 kbps instantly.",
        "h1": "Online MP3 Bitrate Changer",
        "tagline": "Re-encode MP3 files to your exact target bitrate for radio broadcast, podcast feeds, or archival storage.",
        "faqs": [
            ("What is the best MP3 bitrate for music vs speech?", "For music, 320 kbps or 256 kbps offers near-lossless clarity. For spoken word and podcasts, 128 kbps or 96 kbps provides the ideal balance between quality and compact file size.")
        ]
    },
    {
        "slug": "edit-mp3-tags-online",
        "name": "Edit MP3 Tags Online (ID3 Editor)",
        "short_name": "Edit MP3 Tags",
        "category": "convert",
        "color": "#4f46e5",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.59 13.41l-7.17 7.17a2 2 0 0 1-2.83 0L2 12V2h10l8.59 8.59a2 2 0 0 1 0 2.82z"/><line x1="7" y1="7" x2="7.01" y2="7"/></svg>',
        "title": "Edit MP3 Tags Online Free — ID3v2 Tag & Album Cover Editor",
        "desc": "Edit MP3 metadata tags online. Modify Song Title, Artist, Album, Year, Genre, Track Number, and embed custom Album Cover Art directly into your MP3 files.",
        "h1": "Free Online ID3 MP3 Tag Editor",
        "tagline": "Organize your music library with accurate metadata, song information, and embedded high-resolution album artwork.",
        "faqs": [
            ("What ID3 metadata fields can I edit?", "You can edit Song Title, Artist / Band Name, Album Title, Release Year, Genre, Track Number, and attach an Album Cover image (JPG/PNG)."),
            ("Will my car stereo and music player display the new album art?", "Yes! Our ID3 editor embeds standardized ID3v2.3 tags and APIC frames, fully recognized by Apple Music, Spotify, Android, and car infotainment systems.")
        ]
    }
]

CATEGORIES = [
    ("all", "All Audio Tools", "🌟", len(AUDIO_TOOLS)),
    ("cut", "Cut & Trim", "✂️", 5),
    ("effects", "Effects & Speed", "🎚️", 7),
    ("record", "Record & Mix", "🎙️", 3),
    ("video", "Video & Music", "🎬", 4),
    ("convert", "Convert & Tags", "🗜️", 4),
]

print(f"Total tools defined: {len(AUDIO_TOOLS)}")
