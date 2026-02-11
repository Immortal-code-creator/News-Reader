#News Teller Using Pywin32
#Create a News Teller Using Pywin32 that will tell the user current/Latest,crypto and market news
#It uses dispatch and speak function from pywin32
#It uses API key from newsadata.io website
#It uses API key endpoints to retrieve the response of latest,crypto and market news consecutively using requests module
#The data recieved is in JSON format which is converted to python Structure using response.json()
#From the formatted data we taok the results which is a list of Dictionaries and pywin32 tell the title and description(total 10 ) of news

def speak(str):
    """Speak Function Of Pywin32 that will read the news"""
    from win32com.client import Dispatch

    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(str)
import requests

def latest_news():
    """ It helps in retrieving latest news"""
    r=requests.get("https://newsdata.io/api/1/latest?apikey=write API-KEY")
    url="https://newsdata.io/api/1/latest"
    params={
        "apikey":"write API-KEY",
        "language":"en",
    }
    response=requests.get(url,params=params)#Retrieve the news
    data=response.json()#converts the retrieved news in JSON format to python structure
    title=data["results"]#contain list of dictionaries
    news_order = [
        "First", "Second", "Third", "Fourth", "Fifth",
        "Sixth", "Seventh", "Eighth", "Ninth", "Tenth"
    ]
    for j,i in enumerate(title[:10]):
        t=i.get("title","no title available")
        descrip=i.get("description","No available news")
        speak(f"{news_order[j]} News Title")
        speak(t)
        speak(f"{news_order[j]} News Description")
        speak(descrip)
        k = str(input("Do You Want To Stop Listening News(y/n):-"))
        if (k == "y"):
            speak.Speak(" ", 1)#stops the voice from speaking



def crypto_news():
    """ It helps in retrieving crypto news"""
    r=requests.get("https://newsdata.io/api/1/latest?apikey=write API-KEY")
    url="https://newsdata.io/api/1/crypto"
    params={
        "apikey":"write API-KEY",
        "language":"en",
    }
    response=requests.get(url,params=params)
    data=response.json()
    title=data["results"]#contain list of dictionaries
    news_order = [
        "First", "Second", "Third", "Fourth", "Fifth",
        "Sixth", "Seventh", "Eighth", "Ninth", "Tenth"
    ]
    for j, i in enumerate(title[:10]):
        t = i.get("title", "no title available")
        descrip = i.get("description", "No available news")
        speak(f"{news_order[j]} News Title")
        speak(t)
        speak(f"{news_order[j]} News Description")
        speak(descrip)
        k = str(input("Do You Want To Stop Listening News(y/n):-"))
        if (k == "y"):
            speak.Speak(" ", 1)


def market_news():
    """ It helps in retrieving market news"""
    r=requests.get("https://newsdata.io/api/1/latest?apikey=write API-KEY")
    url="https://newsdata.io/api/1/market"
    params={
        "apikey":"write API-KEY",
        "language":"en",
    }
    response=requests.get(url,params=params)
    data=response.json()
    title=data["results"]#contain list of dictionaries
    news_order = [
        "First", "Second", "Third", "Fourth", "Fifth",
        "Sixth", "Seventh", "Eighth", "Ninth", "Tenth"
    ]
    for j, i in enumerate(title[:10]):
        t = i.get("title", "no title available")
        descrip = i.get("description", "No available news")
        speak(f"{news_order[j]} News Title")
        speak(t)
        speak(f"{news_order[j]} News Description")
        speak(descrip)
        k = str(input("Do You Want To Stop Listening News(y/n):-"))
        if (k == "y"):
            speak.Speak(" ", 1)


def User_Input():
    """ This function made for User Interface(UI) and deals with the choice of news user will enter"""
    print("                                     Welcome To News Reader                                              ")
    print("                             This Program Offers 3 Options For News                                      ")
    print("                    Press 1 For Latest News , 2 For Crypto News , 3 For Market News                      ")
    print("The Three News Options are:-")
    list=["Latest_News","Crypto_News","Market_News"]
    for i in range(len(list)):
        print(f"{i+1}.{list[i]}")
    n=int(input("Which News You Want To Listen:-"))
    try:
        if(n==1):
            print("Great Choice,Latest News Will Begin Shortly")
            latest_news()
        elif(n==2):
            print("Amazing Choice,Crypto News Will Begin Shortly")
            market_news()
        else:
            print("Fabulous Choice,Market News Will Begin Shortly")
            market_news()
    except Exception as e:
        print("Enter 1 or 2 or 3")
if __name__ == '__main__':

    User_Input()
