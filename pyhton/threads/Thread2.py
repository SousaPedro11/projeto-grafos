import _thread as thread
import time


def contador(meuId, cont):
    for i in range(cont):
        time.sleep(1)
        print('[%s] => %s' % (meuId, i))


for i in range(5):
    thread.start_new_thread(contador, (i, 5))

time.sleep(6)
print('Saindo da thread principal')
