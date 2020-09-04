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

    while(True):
      semaforoCocinero.acquire()
      try:
        logging.info('Reponiendo los platos...')
        platosDisponibles = platosDisponibles
      finally:
        semaforoPlato.release()

    

class Comensal(threading.Thread):
  def __init__(self, numero):
    super().__init__()
    self.name = f'Comensal {numero}'

  def run(self):
    global platosDisponibles

    semaforoPlato.acquire()
    try:
      while platosDisponibles == 0:   #probar con if

        semaforoCocinero.release()
        semaforoPlato.acquire()
      platosDisponibles -= 1
      logging.info(f'¡Qué rico! Quedan {platosDisponibles} platos')
    finally:
      semaforoPlato.release()


semaforoCocinero = threading.Semaphore(0)
semaforoPlato = threading.Semaphore(1) # un solo thead que modificque la variable
platosDisponibles = 5


Cocinero().start()

for i in range(50):
  Comensal(i).start()

