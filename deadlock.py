#!/usr/bin/env python2.7
import threading
import time
import inspect

a = 5
b = 5

alock = threading.Lock()
block = threading.Lock()

def calc_add_five():
  global a
  global b
  print inspect.stack()[0][3] + " acquires lock a"
  alock.acquire()
  time.sleep(1)
  a = a + 5
  print inspect.stack()[0][3] + " acquires lock b"
  block.acquire()
  time.sleep(1)
  b = b + 5 + a
  print inspect.stack()[0][3] + " releases lock b"
  block.release()
  print inspect.stack()[0][3] + " releases lock a"
  alock.release()

def calc_add_ten():
  global a
  global b
  print inspect.stack()[0][3] + " acquires lock b"
  block.acquire()
  time.sleep(1)
  b = b + 10
  print inspect.stack()[0][3] + " acquires lock a"
  alock.acquire()
  time.sleep(1)
  a = a + 10 + b
  print inspect.stack()[0][3] + " releases lock b"
  block.release()
  print inspect.stack()[0][3] + " releases lock a"
  alock.release()
t1 = threading.Thread(target = calc_add_five)
t2 = threading.Thread(target = calc_add_ten)
t1.start()
t2.start()
t1.join()
t2.join()
print "a = " + str(a)
print "b = " + str(b)
