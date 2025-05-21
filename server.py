# -*- coding: utf-8 -*-
import urllib2
import json
import time
from naoqi import ALProxy

ip = "192.168.1.116"
# Connect to proxies
motion = ALProxy("ALMotion", ip, 9559)
tts = ALProxy("ALTextToSpeech", ip, 9559)

# Set English language and voice
tts.setLanguage("English")
tts.setVoice("naomnc")

while True:
    try:
        response = urllib2.urlopen("http://192.168.1.115:8090/controle")
        data = response.read()
        json_data = json.loads(data)
        
        if json_data != {}:
            button = json_data.get('id')

            if button == 'up':
                print("Moving forward")
                motion.move(1.0, 0.0, 0.0)
                #tts.say("Moving forward")

            elif button == 'down':
                print("Moving backward")
                motion.move(-1.0, 0.0, 0.0)
                #tts.say("Moving backward")

            elif button == 'left':
                print("Moving left")
                motion.move(0.0, 1.0, 0.0)
                #tts.say("Turning left")

            elif button == 'right':
                print("Moving right")
                motion.move(0.0, -1.0, 0.0)
                #tts.say("Turning right")

            elif button == 'a':
                print("Moving head right")
                motion.setAngles("HeadYaw", 0.5, 0.1)
                #tts.say("Looking right")

            elif button == 'b':
                print("Moving head left")
                motion.setAngles("HeadYaw", -0.5, 0.1)
                #tts.say("Looking left")

            elif button == 'start':
                print("Waking up NAO")
                motion.wakeUp()
                #tts.say("I'm waking up")

            elif button == 'stop':
                print("Stopping NAO")
                #tts.say("Going to rest")
                motion.rest()

            else:
                print("Unknown button")
                tts.say("Unknown command")
        
        time.sleep(0.1)

    except Exception as e:
        print("Connection or processing error:", str(e))
        tts.say("I encountered an error")
        time.sleep(1)
