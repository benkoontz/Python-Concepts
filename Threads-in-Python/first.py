# Threading is a way to make a program do multiple things at the same time

import threading

class BuckysMessenger(threading.Thread):
    def run(self):
        for _ in range(10): # you can use an underscore for not caring about the variable
            print(threading.currentThread().getName()) # give every thread a name

x = BuckysMessenger(name = 'Send out messages')
y = BuckysMessenger(name = 'Receive messages')
x.start() # creates a thread called send out message, goes to class and looks for function called run
y.start()
