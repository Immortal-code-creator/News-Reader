# 🗞️ NEWS TELLER USING PYWIN32 (PYTHON)

A command-line based News Teller built using Python and Pywin32 that reads out Latest News, Crypto News, and Market News using text-to-speech functionality.
The program fetches real-time news from newsdata.io API and narrates the news titles and descriptions aloud.

# 📖 DESCRIPTION

The News Teller Using Pywin32 is a Python application designed to provide users with spoken news updates.

The software uses:

newsdata.io API to fetch real-time news

requests module to retrieve API responses

Pywin32 (SAPI.SpVoice) to convert text into speech

The user can choose from three categories of news, and the program will read aloud up to 10 news headlines and descriptions, one by one.

## ✨ FEATURES

-Text-to-Speech using Pywin32

-Reads Latest News

-Reads Crypto News

-Reads Market News

-Fetches real-time data via API

-JSON response handling

-User-controlled stop option

-Simple command-line interface

## 🗂 SUPPORTED NEWS CATEGORIES

-Latest News

-Crypto News

-Market News

## 🧠 CONCEPTS USED

-win32com.client.Dispatch for speech synthesis

-REST APIs

-requests module for HTTP requests

-JSON parsing using response.json()

-Functions and loops

-Conditional statements

-User input handling

## 🛠 DEPENDENCIES

-Python 3.10 or later

-Windows OS (required for Pywin32)

## 📦 EXTERNAL MODULES REQUIRED

-pywin32

-requests

## 📥 INSTALL DEPENDENCIES
pip install pywin32 requests

## 🔑 API USED

-newsdata.io

-API key required for fetching news

-API ENDPOINTS

-Latest News

-Crypto News

-Market News

⚠️ Replace the API key with your own key for production use.

## ⚙️ HOW THE SOFTWARE WORKS

-User runs the program

-A menu with 3 news options is displayed

-User selects a news category

-API request is sent

-Response is received in JSON format

-News titles and descriptions are extracted

-Pywin32 reads the news aloud

-User can stop listening anytime

## 📥 INSTALLATION

Clone the repository:

### git clone https://github.com/your-username/news-teller-using-pywin32.git


Navigate to the project directory:

-cd news-teller-using-pywin32


Install required modules:

pip install pywin32 requests

## ▶️ EXECUTING THE PROGRAM
python news_teller.py

## ❓ HELP / TROUBLESHOOTING

If the program does not work:

-Ensure you are using Windows OS

-Verify Python installation:

### python --version


Ensure pywin32 is installed correctly

Verify API key validity

Check internet connectivity

## 👨‍💻 AUTHOR

Aeshan Chowdhury

### GitHub: https://github.com/Immortal-code-creator
