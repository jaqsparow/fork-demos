import os

def demo3():
    print('Before calling fork(),PID: ', os.getpid())
    rc = os.fork()
    if rc == 0:
        print('I am child, PID: ', os.getpid())
        os._exit(0)
    elif rc > 0:
        print('I am parent,PID:',os.getpid())
    else:
        print('Child process creation failed!!')
    
demo3()