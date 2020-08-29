import requests
import tiempo
import logging
import threading



logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)


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

def bajar_imagen(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img_name = f'{img_name}.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        # print(f'{img_name} fue bajada...')


tiempo = Contador()

tiempo.iniciar()

# una por una
#for url in img_urls:
#    bajar_imagen(url)

#tiempo.finalizar()
#tiempo.imprimir()



# Pero ahora con threads


lista =[]

for url in img_urls:
    #Generamos un hilo por cada imagen
    t = threading.Thread(target=bajar_imagen, args=[url])
    #Lo lanzamos
    t.start()
    lista.append(t)


#Esperamos cada hilo y lo imprimimos.
for thread in lista:
    thread.join()
    tiempo.finalizar()
    tiempo.imprimir()


#Tarda 153 segundos secuencial y 15 segundos con hilos.
#Para limitar a 3 hilos pondria un semaforo que limite la generacion de hilos
#A tres y que liberen luego del join para que el resto siga. De todas formas
#creo que el codigo como está no se podria. porque una vez finalizado el 
#primer for creo... no lo se, voy a probarlo.









