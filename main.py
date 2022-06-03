import mojang
from directKeys import *
import requests
from mojang import MojangAPI

requestlink = str("https://api.hypixel.net/skyblock/bazaar?key=a9408d41-2710-4a17-a642-ccb92f831da6")
hydata = requests.get(requestlink).json()

def getPearlPrice():
    ep = float(hydata["products"]["ENDER_PEARL"]["buy_summary"][0]['pricePerUnit'])
    print(ep)
    return ep
