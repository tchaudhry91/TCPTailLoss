import sys
import nfqueue
from socket import AF_INET

payload_length = 0
drop_count = 0

def callback(i, payload):
    """
        This function causes Tail Drop
    """
    payload.set_verdict(nfqueue.NF_ACCEPT)
    

if __name__=="__main__":
    global payload_length
    global drop_count
    payload_length = sys.argv[0]
    drop_count = sys.argv[1]

    q = nfqueue.queue()
    family = AF_INET
    q.set_callback(callback)
    q.fast_open(0, family)
    q.try_run()
