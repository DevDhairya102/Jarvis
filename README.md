## JARVIS - Python Voice Assistant

This is a simple desktop-based JARVIS-like virtual assistant built using Python. It can recognize voice commands, respond with speech, and perform tasks like playing YouTube videos, telling the time, searching Wikipedia, telling jokes, and listening to your words and more.


---
###  Project Structure

```bash
JARVIS
├── main.py
├── requirements.txt
├── commands
│   ├── open_apps.py
│   ├── search_web.py
│   ├── play_music.py
│   └── system_tasks.py
├── assets
│   ├── jarvis_logo.png
│   └── sounds
├── screenshots
└── README.md
```




### Features

- Voice Recognition (Speech-to-Text)
- Text-to-Speech using `pyttsx3`
- 📺 Play YouTube videos using voice
- 📚 Get quick Wikipedia summaries
- 🕒 Tell current time
-  Crack jokes
- 🔁 Voice-based control loop ("Do you want me to continue?")
- 🛑 Say "stop" or "exit" to shut down

---
## Future Improvements
-Face Recognition Login
-GUI Interface
-ChatGPT Integration
-Home Automation
-WhatsApp Automation
-AI Memory System
-Mobile App Version
-Wake Word Detection (“Hey Jarvis”)

---

Example Commands
Command	Action
“Open Chrome”	Opens Google Chrome
“Play music”	Plays music
“What is the time?”	Speaks current time
“Search Python”	Searches on Google
“Take screenshot”	Captures screenshot


## 🛠️ Built With

- Python 3.11
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [PyAudio](https://pypi.org/project/PyAudio/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [pywhatkit](https://pypi.org/project/pywhatkit/)
- [wikipedia](https://pypi.org/project/wikipedia/)
- [pyjokes](https://pypi.org/project/pyjokes/)

---

## 💻 How to Run

1. **Install dependencies** (create `venv` if preferred):

   ```bash
   pip install -r requirements.txt


   Disclaimer

This project is developed for educational and learning purposes only.
JARVIS is inspired by Marvel’s fictional AI assistant.

👨‍💻 Author

Dhairya Shah
Computer Engineering Student | AI & ML Enthusiast

Support

If you like this project:

Give it a ⭐ on GitHub
Fork the repository
Contribute improvements
