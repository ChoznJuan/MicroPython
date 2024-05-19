import ntptime
import utime

def getTime():
    ntptime.settime()

    getTime = True

    while getTime is True:
        utime.localtime()
        utime.sleep(1)
        clkTime = utime.localtime()
        return clkTime
    