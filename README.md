# Neural-Controle-Pro-
Voice / Gesture / Sign Language Interface v3.2
# Neural Control Pro v3.2

![Neural Control Pro](https://img.shields.io/badge/Status-Active-brightgreen) ![Version](https://img.shields.io/badge/Version-3.2-blue) ![License](https://img.shields.io/badge/License-MIT-purple)

Neural Control Pro is an advanced, multimodal Human-Computer Interface (HCI) that replaces traditional peripherals with computer vision, natural language processing, and Generative AI. It allows you to navigate your PC, execute system commands, type in sign language, and consult an AI assistant—all from a single, unified web dashboard.

---

## 🌟 Key Features

### ✋ Vision System (Virtual Mouse)
Powered by **Google MediaPipe**, the vision system tracks hand landmarks in real-time through your webcam.
* **Cursor Movement:** Tracked via the tip of your index finger. Includes customizable smoothing algorithms.
* **Pinch-to-Click:** Bring your thumb and index finger together to execute left clicks.
* **Right-Click:** Bring your thumb and middle finger together.
* **Drag-and-Drop:** Hold your thumb and ring finger together to drag elements.
* **Scroll:** Thumbs-up to scroll up, thumbs-down to scroll down.

### 🗣️ Audio System (Voice Commands)
Utilizes the **Web Speech API** to listen for system-level commands and route them through the Python backend.
* **Launch Apps:** "Open Notepad", "Launch Calculator", "Open Chrome", etc.
* **System Controls:** "Volume up", "Volume down", "Scroll down", "Go back".

### 🧠 Gemini AI Agent
A built-in AI assistant powered by **Google's Gemini 2.5 Flash** model. 
* Triggered seamlessly via voice by starting your sentence with **"Ask AI..."** (e.g., *"Ask AI how to write a binary search tree"*).
* Bypasses OS controls and fetches intelligent, conversational responses.
* Reads answers out loud using Text-to-Speech synthesis.
* Includes a manual chat interface for text-based interactions.

### 🤟 Sign Language Typing
A dedicated mode that translates static finger-spelling (ASL-inspired) directly into typed text.
* Detects letter formations dynamically.
* Includes a confidence-scoring visualizer.
* Type out words entirely hands-free.

---

## 🛠️ Tech Stack

**Frontend (The Face):**
* HTML5, JavaScript, CSS3
* Tailwind CSS (Styling)
* Google MediaPipe Hands (Client-side Computer Vision via CDN)
* Web Speech API (Speech Recognition & Synthesis)

**Backend (The Brain):**
* Python 3.x
* Flask & Flask-CORS (Local API Server)
* PyAutoGUI (System-level OS Control)
* Google Generative AI SDK (Gemini API Integration)

---

## 🚀 Installation & Setup

### 1. Prerequisites
* **Python 3.8+** installed on your system.
* A working **Webcam** and **Microphone**.
* **Google Chrome** or **Microsoft Edge** (Required for the Web Speech API).
* A free **Gemini API Key** from [Google AI Studio](https://aistudio.google.com/).

### 2. Install Dependencies
Open your terminal or command prompt and install the required Python packages:
```bash
pip install flask flask-cors pyautogui google-generativeai
