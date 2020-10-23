import os

def demo5():
    print('Before any fork,   PID:',os.getpid())
    #First fork
    pid1 = os.fork()
    print('After first fork, PID :',os.getpid())
    #Second fork
    os.fork()
    print('After second fork, PID:',os.getpid())
    #Third Fork
    os.fork()
    print('After third fork, PID:',os.getpid())
  
demo5()