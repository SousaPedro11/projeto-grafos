import threading


class MinhaThread(threading.Thread):
    def __init__(self, meuId, cont, mutex):
        self.meuId = meuId
        self.cont = cont
        self.mutex = mutex
        threading.Thread.__init__(self)

    def run(self):
        for i in range(self.cont):
            with self.mutex:
                print('[%s] => %s' % (self.meuId, i))
