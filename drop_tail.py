import sys
import nfqueue
from socket import AF_INET

dropped = False
drop_count = 0
count = 0
drop_range = []
is_last = False


def callback(handle, new_handle=None):
    """
        This function causes Tail Drop
    """
    global payload_length
    global dropped
    global drop_count
    global count
    global is_last

    if new_handle is not None:
        handle = new_handle
    if handle.get_length() == 1500:
        count = count + 1
        if drop_count > 0:
            if count in drop_range:
                drop_count = drop_count - 1
                if drop_count == 0:
                    is_last = True
                handle.set_verdict(nfqueue.NF_DROP)
            else:
                handle.set_verdict(nfqueue.NF_ACCEPT)
        else:
            handle.set_verdict(nfqueue.NF_ACCEPT)
    elif is_last is True:
        is_last = False
        handle.set_verdict(nfqueue.NF_DROP)
    else:
        handle.set_verdict(nfqueue.NF_ACCEPT)


def buildDropRange(drop_count, payload_length):
    """
        This Function builds a list of packets
        to be dropped
    """
    global drop_range

    while drop_count > 0:
        toDrop = payload_length/1448
        drop_count = drop_count - 1
        payload_length = payload_length - 1448
        drop_range.append(toDrop)


if __name__ == "__main__":
    payload_length = int(sys.argv[2])
    drop_count = int(sys.argv[1])
    print("Started")
    buildDropRange(drop_count, payload_length)
    q = nfqueue.queue()
    family = AF_INET
    q.set_callback(callback)
    q.fast_open(0, family)
    q.try_run()
