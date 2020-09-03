import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

semaphoreComensal = threading.Semaphore(3)
semaphoreComida = threading.Semaphore(0)

class Cocinero(threading.Thread):
  def __init__(self):
    super().__init__()
    self.name = 'Cocinero'

  def run(self):
    global platosDisponibles
    while (True):
      semaphoreComensal.acquire()
      #El semaforo comida hace que el cocinero no cocine hasta que el comensal lo llame.
      semaphoreComida.acquire()
      logging.info('Reponiendo los platos...')
      platosDisponibles = 3
      semaphoreComensal.release()
      
      
class Comensal(threading.Thread):
  def __init__(self, numero):
    super().__init__()
    self.name = f'Comensal {numero}'

  def run(self):
    global platosDisponibles
    #Si los platos disponibles son 0 se bloquea el semaforo comensal.
    if platosDisponibles == 0:
      semaphoreComensal.acquire()
    platosDisponibles -= 1
    semaphoreComensal.release()
    #Cuando no halla mas platos despierto al cocinero
    if platosDisponibles == 0:
      semaphoreComida.release()
    

    logging.info(f'¡Qué rico! Quedan {platosDisponibles} platos')

platosDisponibles = 3

Cocinero().start()

for i in range(5):
  Comensal(i).start()
 
  Cocinero().start()

