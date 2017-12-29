#!/usr/bin/env python
import urllib2, urllib
import time
import sys
import RPi.GPIO as GPIO


##########################################
# DOGE ALTAR Control Script
##########################################
# my first python in a very loooong time
# feel free to improve :D
##########################################

# init balance
balance = 0.0

# init GPIO
GPIO.setmode(GPIO.BOARD)

# Pin 11 (GPIO 17) as Output
GPIO.setup(11, GPIO.OUT)

##################
# BURNING DOGE
##################

def processBurnedDoge( burnAmount ):
   # TODO --> play holy sound with speech of wisdom
   print "Switch on burn fire and make sound for " + str(tipToTheDOGE) + "DOGE"
   letItBurn(10)
   return

def letItBurn( timeToBurn ):
    print "Let it Burn"
    start = time.time()
    time.clock()    
    elapsed = 0
    while elapsed < timeToBurn:
        elapsed = time.time() - start
        print "loop cycle time: %f, seconds count: %02d" % (time.clock() , elapsed) 
        # LED on
        GPIO.output(11, GPIO.HIGH)
        # wait a second
        time.sleep(0.1)
        # LED off
        GPIO.output(11, GPIO.LOW)
    return

##################
# MAIN LOOP
##################

while True:
    try:
        print "Get fresh balance of burn address ..."
        data = urllib.urlopen('https://dogechain.info/chain/Dogecoin/q/addressbalance/DDogepartyxxxxxxxxxxxxxxxxxxw1dfzr')
        print
        freshBanalceStr = data.read()
        freshBalance = float(freshBanalceStr)
        if freshBalance>balance:
            tipToTheDOGE = freshBalance - balance
            balance = freshBalance
            print "SUCH BURN - MUCH WOW: " + str(tipToTheDOGE)
            processBurnedDoge( tipToTheDOGE )
        time.sleep(20)
    except:
        e = sys.exc_info()[0]
        print "SUCH ERROR: %s" % e
        # TODO play error sound
        print "take a nap doge altar - your drunk (30 secs)"
        time.sleep(60)
pass
