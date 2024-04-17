from Olimp import Olimp_parser
from VSHE import VSHE_parser
from time import time


t = time()
while True:
    currentTime = time()
    if int(currentTime - t) % 15 == 0:
        Olimp_parser()
        VSHE_parser()