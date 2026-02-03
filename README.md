🗞️ News Teller Using Pywin32 (Python)

A command-line based News Teller built using Python and Pywin32 that reads out Latest News, Crypto News, and Market News using text-to-speech functionality.
The program fetches real-time news from newsdata.io API and narrates the news titles and descriptions aloud.

📖 Description

The News Teller Using Pywin32 is a Python application designed to provide users with spoken news updates.

The software uses:

newsdata.io API to fetch real-time news

requests module to retrieve API responses

Pywin32 (SAPI.SpVoice) to convert text into speech

The user can choose from three categories of news, and the program will read aloud up to 10 news headlines and descriptions, one by one.

✨ Features

🎙️ Text-to-Speech using Pywin32

📰 Reads Latest News

💰 Reads Crypto News

📈 Reads Market News

🔄 Fetches real-time data via API

📦 JSON response handling

⏹️ User can stop listening anytime

🖥️ Simple command-line interface

🗂 Supported News Categories

Latest News

Crypto News

Market News

🧠 Concepts Used

win32com.client.Dispatch for speech synthesis

REST APIs

requests module for HTTP requests

JSON data parsing (response.json())

Python functions

Loops and conditional statements

User input handling

🛠 Dependencies

Python 3.10 or later

Windows OS (required for Pywin32 SAPI)

External Modules Required

pywin32

requests

Install dependencies using:
pip install pywin32 requests

🔑 API Used

newsdata.io

API key required to fetch news

Endpoints used:

Latest News

Crypto News

Market News

⚠️ Make sure to replace the API key with your own key for production use.

⚙️ How the Software Works

The user runs the program.

A menu is displayed with 3 news options.

The user selects a news category (1–3).

The program sends a request to the API.

The API returns data in JSON format.

Titles and descriptions are extracted.

Pywin32 speaks the news aloud.

The user can stop listening at any time.

📥 Installation

Clone the repository:

git clone https://github.com/your-username/news-teller-using-pywin32.git


Navigate to the project directory:

cd news-teller-using-pywin32


Install required modules:

pip install pywin32 requests

▶️ Executing the Program

Open Command Prompt or Terminal.

Navigate to the project folder.

Run the program:

python news_teller.py

❓ Help / Troubleshooting

If the program does not work:

Ensure you are using Windows OS

Verify Python installation:

python --version


Ensure pywin32 is installed correctly

Check your API key validity

Make sure you have an active internet connection

👨‍💻 Author

Aeshan Chowdhury

GitHub: https://github.com/Immortal-code-creator
