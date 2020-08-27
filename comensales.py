import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

semaphore = threading.Semaphore(2)
mutex = threading.Lock()

class Cocinero(threading.Thread):
  def __init__(self):
    super().__init__()
    self.name = 'Cocinero'

  def run(self):
    global platosDisponibles
    while (platosDisponibles < 3):
      mutex.acquire()
      #logging.info('Reponiendo los platos...')
      platosDisponibles += 1
      logging.info(f'reponiendo {platosDisponibles} platos')
      mutex.release()


class Comensal(threading.Thread):
  def __init__(self, numero):
    super().__init__()
    self.name = f'Comensal {numero}'

  def run(self):
    global platosDisponibles
    semaphore.acquire()
    if platosDisponibles < 1 :
        self.llamarCocinero()
    mutex.acquire()
    platosDisponibles -= 1
    mutex.release()
    logging.info(f'¡Qué rico! Quedan {platosDisponibles} platos')
    semaphore.release()

    
  def llamarCocinero(self):
      Cocinero().start()

platosDisponibles = 3

Cocinero().start()


for i in range(5):
    Comensal(i).start()

    

logging.info(f'platos sobrantes {platosDisponibles} ')