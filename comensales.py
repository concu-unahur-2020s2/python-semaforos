import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)
#luego de la clase repense el ejercicio e hice algunas modificaciones.

#el despertador comienza en cero para que el cocinero espere a que el comensal lo llame.
#lo mismo con el semaforo de comida.
semaforoDespertador = threading.Semaphore(0)
semaforoDeComida = threading.Semaphore(0)

class Cocinero(threading.Thread):
  def __init__(self):
    super().__init__()
    self.name = 'Cocinero'

  def run(self):
    global platosDisponibles
    while (True):
      #en la primera vuelta del while no corre porque inicializó en cero.
      #tomo el semaforo despertador asi el cocinero no cocina hasta que el comensal lo llame.
      semaforoDespertador.acquire()
      logging.info('Reponiendo los platos...')
      platosDisponibles = 3
      #una vez que esten los platos libero el semaforo de comida.
      semaforoDeComida.release()



class Comensal(threading.Thread):
  def __init__(self, numero):
    super().__init__()
    self.name = f'Comensal {numero}'

  def run(self):
    global platosDisponibles

    #si la cantidad de platos disponible es cero bloqueo el semaforo de comida
    if platosDisponibles == 0:
      semaforoDeComida.acquire()

    platosDisponibles -= 1

    #cuando no quedan platos despierto al cocinero
    if platosDisponibles == 0:
      semaforoDespertador.release()

    logging.info(f'¡Qué rico! Quedan {platosDisponibles} platos')


platosDisponibles = 3

Cocinero().start()

for i in range(5):
  Comensal(i).start()