#!/usr/bin/python3

import random
import time
import sys
import threading

if len(sys.argv) == 2:
    n_threads = int(sys.argv[1])
else:
    n_threads = 10

sem = threading.Semaphore()

values = 5

def calc_random(v):
    a = []
    b = []
    c = []
    i=0
    while(i<=v):
        a.append(random.randint(0,9))
        b.append(random.randint(0,9))
        c.append(a[i] + b[i])

        time.sleep(0.5)

        print( threading.current_thread().getName() + ": " + str(a[i]) + " + " + str(b[i]) + " = " + str(c[i]) + "\n", file=sys.stderr)

        i+=1

    sem.acquire()
    
    print("Hello my name is: " + threading.current_thread().getName())

    i = 0
    while(i<=v):
        
        print(threading.current_thread().getName() + ":c[" + str(i) + "]= " + str(c[i]))

        i+=1

    sem.release()


threads = []

for n in list(range(0, n_threads, 1)):
    thread = threading.Thread(target=calc_random, args=(values,))
    threads.append(thread)
    thread.start()

#print(a)
