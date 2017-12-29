# dogecoin_altar
34C3 fun project to burn dogecoin on a raspberry pi "altar"

https://events.ccc.de/congress/2017/wiki/index.php/Projects:Dogecoin_Altar

Contributors:

https://github.com/rootzoll/dogecoin-altar
https://github.com/johncoffee/doge-altar

Purpose:

The script is checking the balance of the burn-address of Dogecoin frequently and triggers a LED-Light on the Raspi
if new Dogecoins came in to get burned

Steps:

- Use a "burn" dogecoin address: DDogepartyxxxxxxxxxxxxxxxxxxw1dfzr

    -> check it out: https://dogechain.info/chain/Dogecoin/q/addressbalance/DDogepartyxxxxxxxxxxxxxxxxxxw1dfzr

- Create python scripts to scan the address frequently and trigger actions to announce incoming funds</br>
    -> a) get latest block from dogecoin-chain</br>
    -> extract all transactions from the block</br>
    -> check transactions if directed to burn-address</br>
    -> if yes: trigger action: LED-Fire & Sound</br>
    -> if no: goto a)
    
- Action 1: LED-Fire: Attach LED to Raspberry 3 Model B</br>
    (see pin wiring http://raspberrypiguide.de/howtos/raspberry-pi-gpio-how-to/)</br>
    -> PIN 9 (Ground)</br>
    -> PIN 11 (3.3V)
    
- Action 2: Sound: tbd.

- Enable python script to auto run</br>
    -> Option 1) Init.d: https://www.raspberrypi.org/forums/viewtopic.php?f=31&t=20462</br>
    -> Option 2) Autorun:</br>
        -> sudo raspi-config -> Select “Boot Options” then “Desktop/CLI” then “Console Autologin”
        -> sudo nano /etc/profile -> add path to python script at the bottom:
            -> sudo python /path/to/script/myscript.py & (& to run in background)
            
How to deploy:

- put the file dogealtar_at_pi.py under /home/pi
- put the script startup.sh under /home/pi

