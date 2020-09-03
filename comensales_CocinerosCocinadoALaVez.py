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
    platosDisponibles += 1
    logging.info(f'reponiendo {platosDisponibles} platos')


class Comensal(threading.Thread):
  def __init__(self, numero):
    super().__init__()
    self.name = f'Comensal {numero}'

  def run(self):
    global platosDisponibles
    semaphore.acquire()
    if platosDisponibles == 0 :
        self.llamarCocineros()
    mutex.acquire()
    platosDisponibles -= 1
    mutex.release()
    logging.info(f'¡Qué rico! Quedan {platosDisponibles} platos')
    semaphore.release()
      
  def llamarCocineros(self):
      global platosDisponibles
      while (platosDisponibles < 3):
              Cocinero(random.randint(0,1)).start()


platosDisponibles = 3

#Cocinero(1).start()

for i in range(5):
    Comensal(i).start()

logging.info(f'platos sobrantes {platosDisponibles} ')