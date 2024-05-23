import ntptime
import time

class GetTime:
    def __init__(self):
        time.localtime()
        #ntptime.settime()
    
        self.getTime = True

        while self.getTime is True:
            time.sleep(1)
            self.clkTime = time.localtime()
            self.dispTime = "{}:{}:{}".format(self.clkTime[3],self.clkTime[4],self.clkTime[4])
            self.dispDate = "{}/{}/{}".format(self.clkTime[1],self.clkTime[2],self.clkTime[0])
            return (self.dispTime, self.dispDate)
    