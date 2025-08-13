# Phishing Champion 🛡️

A phishing simulation tool to test employee awareness and deliver instant training.

## Features
- Sends realistic phishing emails
- Tracks clicks, credential entries, and reports
- Provides instant feedback and training
- Analytics dashboard for risk profiling

## Setup
Run the Tool on a New Laptop
🧰 Step 1: Clone the Repo
bash
git clone https://github.com/yourusername/phishing-champion.git
cd phishing-champion
🧪 Step 2: Create Virtual Environment
bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
📦 Step 3: Install Dependencies
bash
pip install -r requirements.txt
🔐 Step 4: Add .env File
Create a .env file with your SMTP credentials:

env
SMTP_USER=your_email@example.com
SMTP_PASS=your_password
▶️ Step 5: Run the App
bash
python app.py
Visit http://localhost:5000/send_phish/<email> to trigger a phishing simulation.
```bash
git clone https://github.com/yourusername/phishing-champion.git
cd phishing-champion
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
