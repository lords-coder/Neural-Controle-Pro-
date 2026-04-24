import os
import subprocess
import time
import threading
import webbrowser
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import pyautogui
import webbrowser
import google.generativeai as genai

GOOGLE_API_KEY = "AIzaSyD2QePJHqQUParbDAlYnT_RKoCRPfP934c"

try:
    genai.configure(api_key=GOOGLE_API_KEY)
    # Using the fast, efficient flash model
    ai_model = genai.GenerativeModel('gemini-2.5-flash') 
    AI_ENABLED = True
    print("[SUCCESS] Gemini AI initialized!")
except Exception as e:
    AI_ENABLED = False
    print(f"[WARNING] Gemini AI failed to load. Check API Key. Error: {e}")

app = Flask(__name__, static_folder='.')
CORS(app)

# Dictionary mapping voice phrases to actual Windows executables
APPS = {
    'notepad': 'notepad.exe',
    'calculator': 'calc.exe',
    'chrome': 'chrome.exe',
    'edge': 'msedge.exe',
    'explorer': 'explorer.exe',
    'file explorer': 'explorer.exe',
    'settings': 'ms-settings:',
    'store': 'ms-windows-store:',
    'microsoft store': 'ms-windows-store:',
    'cmd': 'cmd.exe',
    'whatsapp': 'whatsapp.exe',
    'tor': 'tor.exe'
}

@app.route('/')
def index():
    # Serve the HTML file
    return send_from_directory('.', 'index.html')

# NEW ROUTE: AI Chat Endpoint
@app.route('/api/chat', methods=['POST'])
def chat():
    if not AI_ENABLED:
        return jsonify({'success': False, 'result': 'AI is not configured. Check API key in app.py.'})
    
    data = request.json or {}
    user_message = data.get('message', '').strip()
    
    if not user_message:
        return jsonify({'success': False, 'result': 'No message received.'})
    
    print(f"[USER -> GEMINI] {user_message}")
    
    try:
        # System Prompt
        prompt = f"""You are 'Neural Control', an advanced AI voice assistant built into the user's computer. 
        Keep your answers concise, conversational, and helpful. Do not use formatting like markdown asterisks, 
        because your text will be read aloud by text-to-speech.
        
        User says: {user_message}"""
        
        response = ai_model.generate_content(prompt)
        print(f"[GEMINI -> USER] {response.text}")
        
        return jsonify({'success': True, 'result': response.text})
    except Exception as e:
        print(f"[AI ERROR] {e}")
        return jsonify({'success': False, 'result': 'My neural network is currently offline. Check the server console.'})

@app.route('/api/command', methods=['POST'])
def command():
    data = request.json or {}
    cmd = data.get('command', '').strip().lower()
    
    print(f"[VOICE COMMAND RECEIVED] {cmd}")
    
    # 1. Handle App Opening
    if cmd.startswith('open ') or cmd.startswith('launch '):
        app_name = cmd.split(' ', 1)[1]
        
        # Fuzzy matching for app names
        exe = APPS.get(app_name)
        if not exe:
            for key in APPS:
                if app_name in key or key in app_name:
                    exe = APPS[key]
                    break
        
        if exe:
            try:
                if exe.startswith('ms-'):
                    os.startfile(exe)
                else:
                    subprocess.Popen(exe)
                return jsonify({'success': True, 'result': f'Opening {app_name}'})
            except Exception as e:
                return jsonify({'success': False, 'result': str(e)})
        else:
            return jsonify({'success': False, 'result': f'App "{app_name}" not found in registry'})

    # 2. Handle Scrolling
    if 'scroll up' in cmd:
        pyautogui.scroll(500)
        return jsonify({'success': True, 'result': 'Scrolled up'})
    if 'scroll down' in cmd:
        pyautogui.scroll(-500)
        return jsonify({'success': True, 'result': 'Scrolled down'})

    # 3. Handle Volume
    if 'volume up' in cmd:
        pyautogui.press('volumeup', presses=3)
        return jsonify({'success': True, 'result': 'Volume increased'})
    if 'volume down' in cmd:
        pyautogui.press('volumedown', presses=3)
        return jsonify({'success': True, 'result': 'Volume decreased'})

    return jsonify({'success': False, 'result': f'Command "{cmd}" not recognized'})


def open_browser():
    """Waits 1.5 seconds for the server to boot up, then opens the web browser."""
    time.sleep(1.5)
    webbrowser.open('http://localhost:5000')

if __name__ == '__main__':
    print("\n" + "="*50)
    print(" NEURAL CONTROL SERVER RUNNING")
    print(" Your browser will open automatically...")
    print("="*50 + "\n")
    
    # Start the browser-opening function in the background
    threading.Thread(target=open_browser).start()
    
    # Start the Flask server
    app.run(host='0.0.0.0', port=5000, debug=False)