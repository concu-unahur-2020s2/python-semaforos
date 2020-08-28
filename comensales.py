import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)


class Cocinero(threading.Thread):
  def __init__(self):
    super().__init__()
    self.name = 'Cocinero'

  def run(self):
    global platosDisponibles
    logging.info('Reponiendo los platos...')
    while (True):
      platosDisponibles = 3
      semaforo.release()

class Comensal(threading.Thread):
  def __init__(self, numero):
    super().__init__()
    self.name = f'Comensal {numero}'

  def run(self):
    global platosDisponibles
    platosDisponibles -= 1
    semaforo.acquire()
    logging.info(f'¡Qué rico! Quedan {platosDisponibles} platos')

platosDisponibles = 3

semaforo = threading.Semaphore(3)

#Cocinero().start()

for i in range(5):
  Comensal(i).start()
  if(platosDisponibles == 0):
    Cocinero().start()
