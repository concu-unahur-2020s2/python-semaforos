import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

semaphore = threading.Semaphore(3)

class Cocinero(threading.Thread):
  def __init__(self):
    super().__init__()
    self.name = 'Cocinero'

  def run(self):
    global platosDisponibles
    while (True and platosDisponibles == 0):
      logging.info('Reponiendo los platos...')
      platosDisponibles = 3
      for i in range(3):
          semaphore.release()

class Comensal(threading.Thread):
  def __init__(self, numero):
    super().__init__()
    self.name = f'Comensal {numero + 1}'

  def run(self):
    global platosDisponibles
    semaphore.acquire()
    platosDisponibles -= 1
    logging.info(f'¡Qué rico! Quedan {platosDisponibles} platos')
    if platosDisponibles == 0:
      Cocinero().start()
      

platosDisponibles = 3
Cocinero().start()


for i in range(5):
  Comensal(i).start()
