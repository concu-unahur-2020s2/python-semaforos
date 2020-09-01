import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

semaphone = threading.Semaphore(2)
semaphoneCocinero = threading.Semaphore(0)


class Cocinero(threading.Thread):
  def __init__(self):
    super().__init__()
    self.name = 'Cocinero'

  def run(self):
    global platosDisponibles

    semaphone.acquire()
    while (True):
      semaphone.acquire()
      logging.info('Reponiendo los platos...')
      platosDisponibles = 3
    

class Comensal(threading.Thread):
  def __init__(self, numero):
    super().__init__()
    self.name = f'Comensal {numero}'

  def run(self):
    global platosDisponibles

    platosDisponibles -= 1
    logging.info(f'¡Qué rico! Quedan {platosDisponibles} platos')
    semaphoneCocinero.release()


platosDisponibles = 3

Cocinero().start()

for i in range(5):
  Comensal(i).start()

