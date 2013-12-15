import sys
import nfqueue

payload_length = 0 
drop_count = 0

def callback(handle, new_handle=None):
    """
        This function causes Tail Drop
    """
    if handle_new is not None:
        handle = handle_new
    print(handle)

if __name__=="__main__":
    global payload_length
    global drop_count
    payload_length = sys.argv[0]
    drop_count = sys.argv[1]
    
    q = nfqueue.queue()
    q.bind(0,callback)
    q.run()
