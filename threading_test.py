import threading
import thread

class BuckyMessenger(threading.Thread):
    def run(self):
        for _ in range(10):
            threading._sleep(0.5)
            print(threading.current_thread().getName())

x = BuckyMessenger(name="send out message")
y = BuckyMessenger(name="recieve messages")
x.start()
y.start()

var = threading.Thread

print var