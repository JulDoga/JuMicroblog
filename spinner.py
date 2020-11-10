import time
from yaspin import yaspin
from yaspin.spinners import Spinners

with yaspin(Spinners.moon, text="Please wait") as sp:
    time.sleep(2)