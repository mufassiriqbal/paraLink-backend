AI-Powered Communication and Smart Home Control System
----------------

 Project Purpose:
This system is designed to assist paralyzed individuals by combining
AI-based communication and smart home control features. Users can
select emotions or commands through a simple web interface, or by
eye-blink detection, and the system will automatically speak the
selected message or control connected IoT appliances.


  → Project documentation

-1
 Technologies Used:
- HTML5, CSS3, JavaScript (Frontend)
- Web Speech API (Text-to-Speech)
- OpenCV / Mediapipe (Blink & Eye Tracking)
- Python (optional, for AI integration)
- Arduino / ESP32 (optional IoT control)
- Urdu and English voice output support

--------------2----------------
 How It Works:
1. User opens the web interface (`index.html`).
2. Icons represent different emotions or actions.
3. User blinks or clicks to select an icon.
4. The system automatically:
   - Generates an AI-enhanced response.
   - Translates it (if enabled).
   - Speaks it aloud using speech synthesis.
5. The message also appears in the on-screen history list.

-----------3-----------------
 Features:
- Eye-blink and click-based interaction.
- AI-powered communication.
- Urdu text-to-speech support.
- Smart home appliance control simulation.
- Fully responsive and browser-based interface.

---------4---------------------------
 How to Run:
1. Open the `AI-Assistive-System` folder.
2. Double-click **index.html** to open it in your browser.
3. Allow microphone and camera permissions if prompted.
4. Select or blink on an icon to hear the voice output.

----------5------------
 Optional Extensions:
- Connect IoT devices via Arduino/ESP32 relays.
- Add emotion prediction using machine learning.
- Expand language support beyond Urdu and English.
- Deploy the web version to GitHub Pages or a local server.

