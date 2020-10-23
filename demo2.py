import os

def demo2():
    print('Before calling fork(),PID: ', os.getpid())
    rc = os.fork()
    print('After calling fork(), PID: ', os.getpid())
    
demo2()