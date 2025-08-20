👓 Smart Glasses to Assist the Visually Impaired

<img width="642" height="340" style="margin-bottom: 20px;" alt="Screenshot 2025-08-20 222839" src="https://github.com/user-attachments/assets/5b3bf466-d1f3-4d61-9b1b-167c133b733a" />

    An AI-powered assistive device designed to help blind and visually impaired people by describing the world around them using a camera, AI (Gemini API), and text‑to‑speech narration.

📌 Project Vision

    Provide independence to visually impaired people.

    Enable users to understand their surroundings in real time.

    Build an affordable & portable solution with simple hardware.

    Demonstrate how AI + hardware + voice technology can solve real-life problems.

🛠️ Hardware Requirements

    Raspberry Pi (mini-computer, main controller)

    Pi Camera Module (mounted on eyeglasses frame)

    Eyeglasses Frame (base to hold camera & Pi)

    Speaker / Earphones (for audio output)

    Power Source (power bank or Pi-compatible battery)

💻 Software & Libraries

    OS: Raspberry Pi OS (Bullseye) / Ubuntu-based Linux

    Language: Python 3

Python Libraries Used:

    pyttsx3 – Offline Text to Speech

    gTTS – Google Text to Speech

    speech_recognition – Voice command recognition

    pydub, playsound – For audio playback

    Gemini API – AI for image description

⚙️ How It Works

    Image Capture → Camera captures an image using Raspberry Pi.

    AI Processing → Image sent to Gemini API → Generates a text description.

    Text-to-Speech → Description converted into speech using pyttsx3 / gTTS.

    Narration → Description played via speaker/earphones for the user.

📂 Project Structure

text
smart-glasses/
│── main.py              # Main Python script
│── requirements.txt     # Python dependencies
│── README.md            # Project documentation
│── /modules/            # Additional helper scripts
│── /samples/            # Sample images & outputs

🚀 Setup & Installation

    Clone this repo:

bash
git clone https://github.com/yourusername/smart-glasses-ai.git
cd smart-glasses-ai

Install dependencies:

bash
pip install -r requirements.txt

Run the project:

    bash
    python3 main.py

🎯 Skills Learned

    Raspberry Pi setup & camera integration

    Python development for IoT & AI integration

    Using Linux commands for hardware projects

    Text-to-speech & speech recognition module handling

    AI API (Gemini) integration for real-world applications

🏆 Achievements

    Successfully demonstrated in school exhibition

    Received guidance and support from teachers

    Learned how AI + IoT technology can impact real lives

🌍 Impact

This project demonstrates how technology can empower visually impaired individuals by providing greater independence and awareness of their surroundings.
It serves as an innovative example of combining AI + hardware + voice technology in the field of assistive technology.
📸 Demo Screenshot / Flow

(Add an image or flowchart here if you have one)
![Project Demo 🤝 Contributing
Contributions are welcome! Feel free to fork this repository and submit PRs.
