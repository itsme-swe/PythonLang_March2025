from threading import *


def display():
    for i in range(65, 91):
        print(chr(i))


t = Thread(target=display, name="Alphabets")

t.start()

for i in range(65, 91):
    print(i)

t.join()

"""
🔸 Here we are creating thread and two threads are running simultaneously, that is the reason we are getting mix results 
"""
