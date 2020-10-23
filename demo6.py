import os

def demo5():
    num = 0
    rc = os.fork()
    if rc > 0:
        num = os.getpid()
    print ('num: ',num)    
demo5()