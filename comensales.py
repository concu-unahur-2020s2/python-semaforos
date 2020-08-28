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
    for i in range(3):
      platosDisponibles += 1
    for i in range(3):
      semaforoComensal.release()

class Comensal(threading.Thread):
  def __init__(self, numero):
    super().__init__()
    self.name = f'Comensal {numero}'

  def run(self):
    global platosDisponibles
    platosDisponibles -= 1
    semaforoComensal.acquire()
    logging.info(f'¡Qué rico! Quedan {platosDisponibles} platos')

platosDisponibles = 3
semaforoComensal = threading.Semaphore(3)

for i in range(5):
  Comensal(i).start()
  if platosDisponibles == 0:
    Cocinero().start()
