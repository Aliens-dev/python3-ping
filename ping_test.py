
import sys
#import ping_fns
from ping import do_one

destination=sys.argv[1]

class MyStats:
    thisIP   = "0.0.0.0"
    pktsSent = 0
    pktsRcvd = 0
    minTime  = 999999999
    maxTime  = 0
    totTime  = 0
    avrgTime = 0
    fracLoss = 1.0

myStats = MyStats # NOT Used globally anymore.

do_one(myStats, destination, destination, timeout=1, mySeqNumber=1, packet_size=1, quiet = False)



