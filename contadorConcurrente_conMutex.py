import threading
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

THREADS = 2
MAX_COUNT = 1000000

counter = 0

mutex = threading.Lock()
# mutex = threading.Semaphore(1) hubiera sido lo mismo que el Lock()

def cuenta():
    global counter

    for i in range(int(MAX_COUNT/THREADS)):
        #forma 1
        # mutex.acquire()
        # counter += 1
        # mutex.release()
        
        #forma 2
        # mutex.acquire()
        # try:
        #     counter += 1
        # finally:
        #     mutex.release()

        # forma 3: abreviatura de forma 2
        with mutex:
            counter += 1
        
threads = []

for i in range(THREADS):
    t = threading.Thread(target=cuenta)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# print(f"Valor del contador: {counter}")
logging.info(f"Valor del contador: {counter}")

