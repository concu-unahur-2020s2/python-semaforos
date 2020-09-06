import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

comensales = []
ctdComensales = 5
platosDisponibles = 3
semaforos = threading.Semaphore(platosDisponibles)

class Cocinero(threading.Thread):
  def __init__(self):
    super().__init__()
    self.name = 'Cocinero'

  def run(self):
    global platosDisponibles
    global semaforos
    while(ctdComensales > 0):
      if(platosDisponibles==0):
        logging.info('Reponiendo los platos...')
        for x in range(3):
          platosDisponibles += 1
          semaforos.release()


class Comensal(threading.Thread):
  def __init__(self, numero):
    super().__init__()
    self.name = f'Comensal {numero}'

  def run(self):
    global platosDisponibles
    global ctdComensales
    global semaforos
    semaforos.acquire()
    platosDisponibles -= 1
    logging.info(f'¡Qué rico! Quedan {platosDisponibles} platos')
    ctdComensales -= 1

Cocinero().start()

for i in range(ctdComensales):
  Comensal(i).start()