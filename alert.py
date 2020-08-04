from bs4 import BeautifulSoup
import requests
from pygame import mixer

def playSound():
    mixer.init()
    mixer.music.load('alert.mp3')
    mixer.music.set_volume(1)
    mixer.music.play()


def getBitCoinValue():
    url = "https://markets.businessinsider.com/currencies/btc-usd"
    response = requests.get(url)
    data = response.content
    soup = BeautifulSoup(data, 'html.parser')
    input_tag = soup.find_all('span')
    value = input_tag[35].contents[0]
    value = str(value)
    value = value.replace(',','')
    value_f = float(value)
    return value_f

def roundOff(value_f):
    #valueRound = int(value_f/100)*100
    valueRound = int(value_f)
    return valueRound
    
currentVal = 0

while True:
    oldVal = currentVal
    currentVal = roundOff(getBitCoinValue())  
    if currentVal != oldVal:
        print('Current Value: USD',currentVal,', Previous Value: USD',oldVal)
        playSound()
