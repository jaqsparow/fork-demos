import os

def demo4():
    #No fork, only one process
    print('Before any fork,  PID:',os.getpid())
    #First fork
    os.fork()
    print('After first fork, PID:',os.getpid())
    #Second fork
    os.fork()
    print('After second fork,PID:',os.getpid())

demo4()