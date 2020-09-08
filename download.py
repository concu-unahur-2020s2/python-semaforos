import requests
import time
import logging
import threading

from tiempo import Contador

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

tiempo = Contador()
ctdThreads = 10
threads = []

img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]

def descargaSecuencial(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img_name = f'{img_name}.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)

def sinThreads():
    tiempo.iniciar()

    for url in img_urls:
        descargaSecuencial(url)

    tiempo.finalizar()
    print("Sin thread: ") 
    tiempo.imprimir()

# Pero ahora con threads

def descargaConcurrente(semaforos):
    while(img_urls): # Mientras no este vacia
        semaforos.acquire()
        try:
            # saco la url de la lista para que no lo vuelva a descargar otro thread
            url = img_urls.pop()
            #logging.info(f'Descargando imagen...')
            descargaSecuencial(url)
            #logging.info(f'Imagen descargada {url}...')
        except IndexError:
            pass
        finally:
            semaforos.release()

def semaforo(cantidad):
    semaforos = threading.Semaphore(cantidad)
    backup = [] 
    backup.extend(img_urls)
    tiempo.iniciar()

    for thread in range( ctdThreads ):
        thread = threading.Thread(target = descargaConcurrente, args=(semaforos,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        # Espero que terminen todos los threads
        thread.join()
    
    tiempo.finalizar()
    print("Threads con " + str(cantidad) + " semaforos: ") 
    tiempo.imprimir()
    img_urls.extend(backup)

# Primer intento sin usar threads
sinThreads()

# Tercer intento con 10 threads y mutex (semaforo = 1)
semaforo(1)

# Segundo intento con 10 threads y 3 semaforos
semaforo(3)
