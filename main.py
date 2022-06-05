import time
from keyboard import *
import mojang
from directKeys import *
import requests
from mojang import MojangAPI
from random import *
from time import *
import json

requestlink = str("https://api.hypixel.net/skyblock/bazaar?key=a9408d41-2710-4a17-a642-ccb92f831da6")
hydata = requests.get(requestlink).json()
randoapi = requests.get(str("https://sky.shiiyu.moe/api/v2/bazaar")).json()

def getPearlPrice():
    ep = float(hydata["products"]["ENDER_PEARL"]["buy_summary"][0]['pricePerUnit'])
    rp = float(randoapi["ENDER_PEARL"]["buyPrice"])
    print("skyblock: {} rando {}".format(ep, rp))
    return ep


def dropItem():
    PressKey(CTRL)
    PressKey(Q)
    sleep(float("0.{}".format(randint(10, 20))))
    ReleaseKey(CTRL)
    ReleaseKey(Q)
#read_key() == 'f'

def openBazaar(sec=0):
    sleep(sec)
    PressKey(SLASH)
    ReleaseKey(SLASH)
    sleep(uniform(0.100, 0.299))
    PressKey(B)
    ReleaseKey(B)
    sleep(uniform(0.100, 0.299))
    PressKey(H)
    ReleaseKey(H)
    sleep(uniform(0.100, 0.299))
    PressKey(ENTER)
    ReleaseKey(ENTER)


def getMousePos():
    pos = {}
    num = 1
    while read_key() != "r":
        if read_key() == "f":
            mospos = queryMousePosition()
            pos.update({"x{}".format(num): mospos.x, "y{}".format(num): mospos.y})
            num += 1
    json_object = json.dumps(pos, indent=0)
    with open("invpos.json", "w") as outfile:
        outfile.write(json_object)

def dropInventory():
    coords = json.load(open("invpos.json", "r"))['inv_position']
    PressKey(E)
    ReleaseKey(E)
    sleep(uniform(0.2, 0.4))
    moveMouseTo(1000, 465)
    for x in range(1, 36):
        moveMouseTo(coords["x{}".format(x)], coords["y{}".format(x)])
        sleep(uniform(0.15, 0.2))
        dropItem()
    PressKey(E)
    ReleaseKey(E)


while True:
    if read_key() == "f":
        dropInventory()



