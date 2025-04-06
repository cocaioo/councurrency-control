import threading
import queue
import time
import random

BUFFER_SIZE = 5
buffer = queue.Queue(BUFFER_SIZE)

num_produtores = 1
num_consumidores = 1

intercalar = (num_produtores == num_consumidores)

sem_produtor = threading.Semaphore(1)
sem_consumidor = threading.Semaphore(0)

sem_espacos = threading.Semaphore(BUFFER_SIZE)
sem_itens = threading.Semaphore(0)
mutex = threading.Lock()

class Produtor(threading.Thread):
    def __init__(self, nome):
        super().__init__()
        self.nome = nome

    def run(self):
        for _ in range(10):
            item = random.randint(1, 100)
            if intercalar:
                sem_produtor.acquire()
                buffer.put(item)
                print(f"{self.nome} produziu {item}")
                sem_consumidor.release()
            else:
                sem_espacos.acquire()
                with mutex:
                    buffer.put(item)
                    print(f"{self.nome} produziu {item}")
                sem_itens.release()
            time.sleep(random.uniform(0.5, 1.5))

class Consumidor(threading.Thread):
    def __init__(self, nome):
        super().__init__()
        self.nome = nome

    def run(self):
        for _ in range(10):
            if intercalar:
                sem_consumidor.acquire()
                item = buffer.get()
                print(f"{self.nome} consumiu {item}")
                buffer.task_done()
                sem_produtor.release()
            else:
                sem_itens.acquire()
                with mutex:
                    item = buffer.get()
                    print(f"{self.nome} consumiu {item}")
                    buffer.task_done()
                sem_espacos.release()
            time.sleep(random.uniform(1, 2))

produtores = [Produtor(f"Produtor{i+1}") for i in range(num_produtores)]
consumidores = [Consumidor(f"Consumidor{j+1}") for j in range(num_consumidores)]

threads = produtores + consumidores

for t in threads:
    t.start()

for t in threads:
    t.join()

print("Processo finalizado!")
