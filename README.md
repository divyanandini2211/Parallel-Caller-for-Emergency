Parallel Emergency Caller

A multi-threaded emergency response tool that initiates simultaneous voice calls and SMS alerts to multiple caregivers using the Twilio API. Fast, reliable, and suitable for health emergencies when every second counts.

Key Features:
- Parallel Voice Calling: Calls all emergency contacts concurrently using multithreading.
- Instant SMS Alerts: Sends predefined text messages alongside calls.
- Configurable Contacts: Easily customize contact list and alert text in config.txt.
- Reliable Execution: Detects and retries failed calls or messages automatically.

Use Cases:
- Health emergencies for bedridden or elderly individuals
- Home or rural safety alert systems
- Backup alert tool for caregivers and hospitals

Tech Stack:
- Language: Python
- API: Twilio Voice & SMS
- Architecture: Python threading for parallel dispatch
- OS Support: Windows, macOS, Linux

Installation & Setup:
1. Clone the repository:
   git clone https://github.com/divyanandini2211/Parallel-Caller-for-Emergency.git
   cd Parallel-Caller-for-Emergency

2. Create a virtual environment:
   python -m venv venv
   venv\Scripts\activate    # Windows
   # source venv/bin/activate  # macOS/Linux

3. Install dependencies:
   pip install -r requirements.txt

4. Configure credentials and contacts in config.txt:
   TWILIO_SID=<your_sid>
   TWILIO_AUTH_TOKEN=<your_token>
   TWILIO_PHONE_NUMBER=<your_twilio_number>
   CONTACTS=+91xxxxxxx,+91yyyyyyy

How to Run:
   python emergency_caller.py

Logs and notifications display in the terminal.

Project Structure:
- emergency_caller.py     # Main application logic
- config.txt              # Settings for credentials and contacts
- requirements.txt        # Dependencies
- README.txt              # Project documentation

Future Improvements:
- Add GUI interface
- Voice-trigger support (e.g. "help")
- Integration with wearable health devices
- Local logging and dashboard display

Author:
Divya Nandhini R
Sai Karthi Balaji.G
SuryaPrakash.B
Nivashini.N
Latshana.P


