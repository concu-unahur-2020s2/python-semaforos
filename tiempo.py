import time
import logging

class Contador:
  def iniciar(self):
    self.inicio = time.perf_counter()

  def finalizar(self):
    self.fin = time.perf_counter()

  def imprimir(self):
    logging.info(f'Pasaron {round(self.fin - self.inicio, 2)} segundos')
