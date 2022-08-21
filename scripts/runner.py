from StegPix.scripts.decrypt import run_decryption
from StegPix.scripts.encrypt import run_encryption
import time
import random

from StegPix.scripts.utils.utils import hacky_string


def start():
    cryp = input("Would you like to perform Encryption or Decryption?\n>>")
    if "encrypt" in cryp:
        run_encryption()
    elif "decrypt" in cryp:
        run_decryption()
    else:
        print("You have not provided a valid input. I will now hack into your system as a punishment.\n")
        time.sleep(3)
        for i in range(50):
            time.sleep(0.1)
            hacky_string()
        print("You have been hacked and your bank accounts have been emptied.")


start()

