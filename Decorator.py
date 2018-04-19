import time
def decorator(f):
    def decorator():
        startTime = time.time()
        f()
        stopTime = time.time()
        print(stopTime-startTime)
    return decorator
    
# @decorator
def foo():
    time.sleep(2)
    print('sleeping')
# foo()
foo = decorator(foo)
foo()