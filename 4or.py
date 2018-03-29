import pixelvloer

player = 1
spelbord = [[3 for x in range(9)] for y in range(8)]
positie = 0

breedte = 9
hoogte = 8

def pixel(x,y,r,g,b):
     pixelvloer.zet((int(y*11)+int(x)),r,g,b)

def tekenbord():
     for i in range (0,11):
        for j in [0,10]:
            pixel(j,i,0,0,200)
            pixel(i,j,0,0,200)

def clear():
     for i in range (0,11):
        for j in range (0,11):
            pixel(i,j,0,0,0)

def zet(kolom,speler):
    for i in range(0,hoogte):
        if spelbord[i][kolom] == 3:
            gezet = 1
            if speler == 1:
                spelbord[i][kolom] = 0
                pixel(kolom+1,9-i,255,0,0)
            else:
                spelbord[i][kolom] = 1
                pixel(kolom+1,9-i,0,255,0)
            break
clear()
tekenbord()


import paho.mqtt.client as mqtt
import config


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(config.mqtttopic)

def on_message(client, userdata, msg):
    global positie, breedte, player
    consolenr = 0
    try: #kijken of het wel echt een nummer is
        consolenr = int(msg.topic.split("/")[-1])
    except:
        pass

    if consolenr == player:
        if msg.payload.decode() == "left":
            if (positie > 0):
                positie -= 1
        if msg.payload.decode() == "right":
            if (positie < (breedte-1)):
                positie += 1
        if msg.payload.decode() == "down":
            zet(positie,player)
            player += 1
            if player >2 : player=1

    for i in range(0,9):
        if i == positie:
            if player == 1:
                pixel(i+1,1,255,0,0)
            else:
                pixel(i+1,1,0,255,0)
        else:
            pixel(i+1,1,0,0,0)

client = mqtt.Client()
client.username_pw_set(config.mqttuser, config.mqttpass)
client.connect(config.mqttaddr,1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
