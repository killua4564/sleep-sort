# !/usr/bin/env python3
from time import sleep
from random import randint
from threading import Thread

def target(n, value):
	global sorted_list
	sleep(n)
	sorted_list.append(value)

unsort_list, sorted_list = [randint(-100, 100) for _ in range(randint(10, 20))], []
max_value, min_value = unsort_list[0], unsort_list[0]
print(unsort_list)

for item in unsort_list[1:]:
	if max_value < item: max_value = item
	elif min_value > item: min_value = item

for item in unsort_list: Thread(target=target, args=((item - min_value) / (max_value - min_value), item)).start()

sleep(1)
print(sorted_list)