"""Sends daily price alerts of Cryptocurrencies via text message"""

from time import sleep
import requests
import schedule
from twilio.rest import Client #for text messaging

#cryptocurrencies APIs, can change to cryptocurrencies of choice
bitcoin_api_url = 'https://api.coinmarketcap.com/v1/ticker/bitcoin/' 
ethereum_api_url = 'https://api.coinmarketcap.com/v1/ticker/ethereum/'
litecoin_api_url = 'https://api.coinmarketcap.com/v1/ticker/litecoin/'
stellar_api_url = 'https://api.coinmarketcap.com/v1/ticker/stellar/'
xrp_api_url = 'https://api.coinmarketcap.com/v1/ticker/ripple/'

#Twilio account info
account_sid = '' #put your own account sid number
auth_token = '' #put your own auth token
client = Client(account_sid, auth_token)


#functions to get crypto prices from api
def get_bitcoin_price():
    response = requests.get(bitcoin_api_url)
    response_json = response.json()
    return float(response_json[0]['price_usd'])

def get_ethereum_price():
    response = requests.get(ether_api_url)
    response_json = response.json()
    return float(response_json[0]['price_usd'])

def get_litecoin_price():
    response = requests.get(litecoin_api_url)
    response_json = response.json()
    return float(response_json[0]['price_usd'])

def get_stellar_price():
    response = requests.get(stellar_api_url)
    response_json = response.json()
    return float(response_json[0]['price_usd'])

def get_xrp_price():
    response = requests.get(xrp_api_url)
    response_json = response.json()
    return float(response_json[0]['price_usd'])

def send_text(): #sends text message alert
    bitcoin_price = get_bitcoin_price()
    ethereum_price = get_ethereum_price()
    litecoin_price = get_litecoin_price()
    stellar_price = get_stellar_price()
    xrp_price = get_xrp_price()
    message = client.messages \
                .create(
                     body=f'Bitcoin is currently priced at ${bitcoin_price}!\n' 
                          f'Ethereum is currently priced at ${ether_price}!\n'
                          f'Litecoin is currently priced at ${litecoin_price}!\n'
                          f'Stellar is currently priced at ${stellar_price}!\n'
                          f'XRP is currently priced at ${xrp_price}!',
                     from_='',#put phone number selected from Twilio account
                     to='' #put your own cell phone number
                 )
    print(message.sid)

if __name__ == '__main__':
    schedule.every().day.at(15:00).do(send_text)
    """sends text price alert at 3pm everyday, can change to different time or even
       send every few minutes using
       schedule.every(60).minutes.do(send_text)
       can change number to different number of minutes"""
    
    

    while True:
        schedule.run_pending()
        sleep(1)

    
