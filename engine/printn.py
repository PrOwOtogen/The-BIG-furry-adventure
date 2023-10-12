##Typewriter Effect

import sys
import time

def printn(c,t=0.01):
    for _ in c:
        sys.stdout.write(_)
        sys.stdout.flush()
        time.sleep(t)
    
