import time

def getMillis() -> int:
    milli = int(round(time.time() * 1000))
    return milli