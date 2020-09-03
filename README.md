# Mutex / Semáforos

## Precalentando
En `dowload.py` hay código que se baja secuencialmete imágenes, desde urls determinadas.
- Correlo y fijate aprox. cuánto tarda.
  Entre 102 y 110 seg. 
- Ahora codealo concurrente usando threads. Por ahora, lanzá un thread por cada imagen que querés bajar. Para más adelante: si querés usar solamente 3 threads, ¿cómo hacés?
  Se me ocurrio poner en el for una llamada para que cada iteracion tenga un threads:
  
  for url in img_urls:
    t = threading.Thread(target=bajar_imagen, args=[url]) 
    threads.append(t)
    t.start()
    comenzoDescarga(url)
  
  Agregue una pequeña funcion, que me diga cuando el hilo ejecuto, me haga un print de pantalla con una leyenda a modo de ver que todos los hilos iniciaron con el for.
  Para que solo haya tres threads corriendo, defini como area critica, la funcion que descarga la imgagen. Alli agregue una acquire() para que antes de comenzar a descargar y  luego que termine, suelte el bloqueo.
  Lo que si, no logre esta vez poder representarlo en pantalla.
  
  mutex = threading.Semaphore(3)

def bajar_imagen(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img_name = f'{img_name}.jpg'
    mutex.acquire()
    print(f'{img_name} comenzo a bajar...')
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} fue bajada...')
    mutex.release()
  
  

## Mutex
En `contadorConcurrente_conMutex.py` está resuelto el problema del contador, sincronizado usando un `Lock` (mutex), para que lo uses de ejemplo.

## Semáforos básico

En `semaforos.py` está el funcionamiento básico de un semáforo.

## Computadoras e impresoras

En `impresoras.py` vamos a simular que tenemos una serie de `Computadoras` que necesitan imprimir cosas en `Impresoras`. Dentro de la red podemos tener cualquier número de impresoras y computadoras; aunque obviamente en este ejemplo habrá más computadoras que impresoras.

A la implementación que ya está hecha, agregale semáforos para que las computadoras se queden esperando si no hay impresoras disponibles. Como está ahora, arroja un error al intentar sacar un elemento cuando la lista está vacía. 

## Cocinero, comensales y platos

En `comensales.py` esta una simulación donde tenemos `Comensales`, un `Cocinero` y una determinada cantidad de platos disponibles.

Si un comensal quiere comer y no hay más platos, debería:
1. despertar al `Cocinero` para que los reponga;
1. esperar a que este termine;
1. comer.

Agregar la sincronización necesaria para que el programa dado funcione así. No importa el orden en que comen los comensales, sí importa que no coman cuando no hay más platos. Una vez sincronizado probar de agregar más comensales, debería funcionar igual.

La salida debería verse más o menos así:

```
19:22:57.349 [Comensal 0] - ¡Qué rico! Quedan 2 platos
19:22:57.349 [Comensal 1] - ¡Qué rico! Quedan 1 platos
19:22:57.350 [Comensal 2] - ¡Qué rico! Quedan 0 platos
19:22:57.350 [Cocinero] - Reponiendo los platos...
19:22:57.350 [Comensal 4] - ¡Qué rico! Quedan 2 platos
19:22:57.350 [Comensal 3] - ¡Qué rico! Quedan 1 platos
```
### Comentario

No se puede asegurar que el thread que llamó al cocinero y se queda esperando, sea el primero en recibir un plato cuando el cocinero termina de cocinar. Esto es algo inherente a la concurrencia. Se puede leer de [acá](https://docs.python.org/3.8/library/threading.html#semaphore-objects) del `acquire()`.

### Bonus: variantes

Ahora podés probar algunas variantes. Por ejemplo

* Que haya más de un cocinero, compiten por quién cocina primero y solamente uno puede cocinar.
* Que haya más de un cocinero, y pueden cocinar dos a la vez.
* Que el cocinero *agregue* platos antes de que se terminen. (Ahora nunca se va a dar el caso de que un comensal tenga que esperar al cocinero porque no hay más platos).
* La cantidad de comensales que pueden pedir platos al mismo tiempo son 2.
