import requests
import time
import logging
import threading

from tiempo import Contador

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)


img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719'
    
]

def bajar_imagen(img_url):
    
        img_bytes = requests.get(img_url).content
        img_name = img_url.split('/')[3]
        img_name = f'{img_name}.jpg'
        with open(img_name, 'wb') as img_file:
            img_file.write(img_bytes)
        # print(f'{img_name} fue bajada...')




#tiempo.iniciar()

# una por una
#for url in img_urls:
 #   bajar_imagen(url)

#tiempo.finalizar()
#tiempo.imprimir()



# Pero ahora con threads
def run():
    dato=img_urls.pop()
    bajar_imagen(dato)

tiempo = Contador()

tiempo.iniciar()

lista = [] #crea una lista vacía

for i in range(2):
    #crear un thead
    imag = threading.Thread(target=run)
    #lanzarlo
    lista.append(imag)
    imag.start()
    
   
for thread in lista:
    thread.join()

tiempo.finalizar()
tiempo.imprimir()