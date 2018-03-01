#!/usr/bin/python3

#Assignment 01 - Big-O Notation of few famous algorithms

import time as time
import random as random
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation
from datetime import datetime

#**********Algorithms to test speed**********

def BubbleSort(data): 
  for i in range(0, len(data)-1, 1):
    for j in range(0, i, 1):
      if data[j] > data[j+1]:
        temp = data[j]
        data[j] = data[j+1]
        data[j+1] = temp

def SelectionSort(data):
  for i in range(0, len(data)-1, 1):
    for j in range(i+1, len(data), 1):
      if data[i] > data[j]:
        temp = data[i]
        data[i] = data[j]
        data[j] = temp

def SequentialSearch(data, item):
  for i in range(0, len(data)-1, 1):
    if data[i] == item:
      return '{item} is found.'.format(item=item)

def BinarySearch(data, item):
  head = 0 
  tail = len(data) - 1
  while True:
    if tail > head:
      return -1
    m = (head + tail) // 2
    if data[m] < item:
      min = m + 1
    elif data[m] > item:
      max = m - 1
    else:
      return '{item} is found.'.format(item=item)

#*******************Calculate****************

#generate a random array of # len elements b/w 1 to 10000, not unique
def gen_ran_arr(len): 
  temp = list(random.sample(range(1, 10000), len))
  return temp

def choose_ran_item(array):
  #a = array[len(array)-1] change it to view worst case scenario
  a = random.choice(array)
  return a

#returns the run time of the function
#option: 1 - sorting 2 - search 3 - maze
def runtime(option, i, function_to_run):
  import timeit
  data = gen_ran_arr(i)
  if option >=4 and option <=6:
    data.sort()
    item = choose_ran_item(data)

  if option <= 3:
    start = timeit.default_timer()
    function_to_run(data)
    end = timeit.default_timer()

  elif option >=4 and option <= 6:
    start = timeit.default_timer()
    function_to_run(data, item)
    end = timeit.default_timer()

  return (end - start)

#******************Matplotlib****************

t = []

for i in range()

  y = runtime(4, i, BinarySearch)

#**************************User**************

print("---------------------------------------------")
print("Enter Option:")
print("1. Bubble, 2. Selection 3.Bubble+Selection")
print("4. Sequential 5. Binary 6. Sequential+Binary")
print("7. Stack 8. Queue 9. Stack+Queue")
print("---------------------------------------------")

option = int(input())
#**************************User**************



 #t.append(runtime(4, i, SequentialSearch))


#plt.plot(range(1, 1001), time)
#plt.show()
