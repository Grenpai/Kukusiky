import random
import numpy as np

#1  Использование random.randint()
def my_rand1():
	rand_list=[]
	n=10
	for i in range(n):
		rand_list.append(random.randint(3,9))
	return (rand_list)

#2  Использование random.sample()
def my_rand2 ():
	res = random.sample(range(1, 50), 7)
		# printing result
	return ("Random number list is : " + str(res))

#3  Использование списочного понимания + randrange()
def my_rand3():
	res = [random.randrange(1, 50, 1) for i in range(7)]

	# printing result
	return ("Random number list is : " + str(res))

#4 Использование цикла + randint()
def my_rand4():
	lis = []
	for _ in range(10):
		lis.append(random.randint(0, 51))
	return (lis)

#Случайное число с использованием Numpy!!

#5-1 Генерация списка случайных целых чисел с помощью функции numpy.random.randin
def my_rand5_1():
	return (list(np.random.randint(low = 3,high=8,size=10)))

	return (list(np.random.randint(low = 3,size=5)))

#5-2 Генерация списка случайных плавающих значений с помощью функции numpy.random.random_sample
def my_rand5_2():
	return (np.random.random_sample(size=4))

	return (np.random.random_sample(size=(4, 4)))

#print(str((my_rand1(),my_rand2(),my_rand3(),my_rand4(),my_rand5_1(),my_rand5_2())).split(","))
print(my_rand1())
print(my_rand2())
print(my_rand3())
print(my_rand4())
print(my_rand5_1())
print(my_rand5_2())
