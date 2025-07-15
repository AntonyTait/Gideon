# Gideon: LineageOS Home Assistant (Samsung S8+)

## Vision
Gideon is a home assistant running on a Samsung S8+ with LineageOS, inspired by Google Home and Alexa. It will listen for the trigger word "Hey Gideon," maintain conversational context (resetting after 20 minutes of inactivity), search the web, set reminders and alarms, control volume, and play music via YouTube Music. The S8+ provides a built-in microphone, speaker, touchscreen, and WiFi, making it an ideal all-in-one device. The assistant will feature a minimal black and white touchscreen UI with clock, weather, reminders, and interactive elements.

---

## 1. Core Assistant Features
- **Constant Mic Input:** Always-on listening, toggleable via UI.
- **Wake Word Detection:** "Hey Gideon".
- **Speech-to-Text (STT):** Convert spoken commands to text.
- **Conversational AI:** DeepSeek via OpenRouter API (with tool support, up-to-date knowledge via API, not hardcoded logic).
- **Web Search:** Use tools via OpenRouter/DeepSeek.
- **Reminders/Alarms:** Set, manage, and notify.
- **Set Volume:** Control device volume via voice or UI.
- **Text-to-Speech (TTS):** Speak responses aloud, highlight text as read.
- **Music Playback:** Play music via YouTube Music (preferably ad-free via Piped, Electron, or similar solution).
- **Context Management:** Save context per conversation, delete after 20 minutes of inactivity.

---

## 2. Touchscreen Features
- **Minimal Black and White Theme:** Clean, modern, and easy on the eyes.
- **Clock and Weather:** Prominently displayed.
- **Mic Toggle Button:** Easily enable/disable listening.
- **Reminders Today Section:** Displayed on the right side.
- **Listening Animation:** Visual feedback when listening.
- **TTS Highlighting:** Show response text and highlight as it's read aloud.
- **Now Playing:** Show currently playing music info.

---

## 3. Tech Stack Suggestions (LineageOS, Android-based)
- **Language:** Python (via Termux or Pydroid), or Kotlin/Java for native Android integration. Consider Kivy or React Native for cross-platform UI.
- **Wake Word:** Porcupine, Vosk, or open-source alternatives (ARM/Android compatible).
- **STT:** Vosk, OpenAI Whisper, or Android's built-in STT.
- **TTS:** Android TTS, Coqui TTS, or espeak (if using Python).
- **AI API:** DeepSeek via OpenRouter (HTTP requests, tool support).
- **Web Search:** Via DeepSeek tools.
- **Reminders/Alarms:** Local scheduling (Python’s sched/APScheduler, or Android alarms).
- **Music:** yt-dlp + VLC/mpv, or Piped API for ad-free YouTube Music.
- **UI:** Kivy (Python), React Native, or native Android (Kotlin/Java). Minimal black and white theme.
- **Audio I/O:** Android APIs, or Python’s sounddevice/pyaudio if supported.
- **Weather:** OpenWeatherMap API or similar.

---

## 4. Project Structure Example
```
gideon/
├── main.py
├── audio/
│   ├── wake_word.py
│   ├── stt.py
│   └── tts.py
├── ai/
│   └── deepseek.py
├── tools/
│   ├── web_search.py
│   ├── reminders.py
│   ├── alarms.py
│   └── music.py
├── ui/
│   ├── touchscreen.py
│   ├── animation.py
│   ├── clock.py
│   ├── weather.py
│   └── now_playing.py
├── utils/
│   ├── context_manager.py
│   └── volume.py
├── requirements.txt
└── README.md
```

---

## 5. First Steps
- Decide on Python (Termux/Pydroid) or native Android (Kotlin/Java) for core logic.
- Scaffold the project structure for modularity and future features.
- Test audio input/output and basic UI on LineageOS.
- Implement a minimal always-listening wake word + STT + TTS loop with UI toggle.
- Integrate DeepSeek via OpenRouter for basic Q&A.

Let this plan guide the development of Gideon, your custom home assistant for LineageOS! 