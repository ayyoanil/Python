import threading

class MsgThread(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())


sender = MsgThread(name='Sending messages')
receiver = MsgThread(name ='Recieving messages')

receiver.start()
sender.start()


