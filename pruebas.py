from threading import Thread, Event, Lock
import time

lock = Lock()

salir = Event()
#salir.clear()

r = 1

def func1(n):
    global salir
    contador = 0
    while contador < 20:
        if contador % n == 0:
            print(contador)
        contador += 1
        time.sleep(1)
    salir.set()

def func2():
    global r
    global salir
    while not salir.is_set():
        lock.acquire()
        r = r*2+1
        print(f"-> {r}")
        lock.release()
        time.sleep(1)

def func3():
    global r
    global salir
    while not salir.is_set():
        if int(time.time()) % 3 == 0:
            lock.acquire()
            r = -r
            lock.release()

# args[], indicamos los parametros de la funcion
# daemon si muere el hilo principal, muere el hilo secundario
h1 = Thread(target=func1, args=[5])#, daemon=True)
h2 = Thread(target=func2)
h3 = Thread(target=func3)

h1.start()
h2.start()
h3.start()

h1.join() # nos incorporamos al hilo principal

# Una hebra que este pendiente del microfono


