import threading
import time
import logging
import random

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

semaphore = threading.Semaphore(2)
mutex = threading.Lock()

class Cocinero(threading.Thread):
  def __init__(self, numero):
    super().__init__()
    self.name = f'Cocinero {numero}'

  def run(self):
    global platosDisponibles
    while (platosDisponibles < 3):
            platosDisponibles += 1
            logging.info(f'reponiendo {platosDisponibles} platos')


class Comensal(threading.Thread):
  def __init__(self, numero):
    super().__init__()
    self.name = f'Comensal {numero}'

  def run(self):
    global platosDisponibles
    semaphore.acquire()
    if platosDisponibles < 1 :
        self.llamarCocineros()
    mutex.acquire()
    platosDisponibles -= 1
    logging.info(f'¡Qué rico! Quedan {platosDisponibles} platos')
    mutex.release()
    semaphore.release()

    
  def llamarCocinero(self):
      Cocinero().start()
      
  def llamarCocineros(self):
      Cocinero(random.randint(0,2)).start()

platosDisponibles = 3

Cocinero(1).start()


for i in range(10):
    Comensal(i).start()

    

logging.info(f'platos sobrantes {platosDisponibles} ')