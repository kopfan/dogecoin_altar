# dogecoin_altar
34C3 fun project to burn dogecoin on a raspberry pi "altar"

https://events.ccc.de/congress/2017/wiki/index.php/Projects:Dogecoin_Altar

Contributors:

https://github.com/rootzoll/dogecoin-altar
https://github.com/johncoffee/doge-altar

Steps:

- Use a "burn" dogecoin address: DDogepartyxxxxxxxxxxxxxxxxxxw1dfzr

    -> check it out: https://dogechain.info/chain/Dogecoin/q/addressbalance/DDogepartyxxxxxxxxxxxxxxxxxxw1dfzr

- Create python scripts to scan the address frequently and trigger actions to announce incoming funds
    -> a) get latest block from dogecoin-chain
    -> extract all transactions from the block
    -> check transactions if directed to burn-address
    -> if yes: trigger action: LED-Fire & Sound
    -> if no: goto a)
    
- Action 1: LED-Fire: Attach LED to Raspberry 3 Model B
    -> PIN 11 (3.3V)
    
- Action 2: Sound: tbd.

- Enable python script to auto run
    -> Option 1) Init.d: https://www.raspberrypi.org/forums/viewtopic.php?f=31&t=20462
    -> Option 2) Autorun:
        -> sudo raspi-config -> Select “Boot Options” then “Desktop/CLI” then “Console Autologin”
        -> sudo nano /etc/profile -> add path to python script at the bottom:
            -> sudo python /path/to/script/myscript.py & (& to run in background)

