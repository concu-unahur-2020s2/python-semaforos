import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)
mutex = threading.Semaphore(2)
mutex2 = threading.Lock()
class Cocinero(threading.Thread):
  def __init__(self):
    super().__init__()
    self.name = 'Cocinero'

  def run(self):
    global platosDisponibles
    with mutex2:
      while (True):
        logging.info('Reponiendo los platos...')
        platosDisponibles = 3
        time.sleep(2)

class Comensal(threading.Thread):
  def __init__(self, numero):
    super().__init__()
    self.name = f'Comensal {numero}'

  def run(self):
    global platosDisponibles
    with mutex:
      platosDisponibles -= 1
      logging.info(f'¡Qué rico! Quedan {platosDisponibles} platos')
      time.sleep(2)

platosDisponibles = 3

Cocinero().start()

for i in range(5):
  Comensal(i).start()

