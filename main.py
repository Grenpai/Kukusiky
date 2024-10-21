import random

#1  Использование random.randint()
rand_list=[]
n=10
for i in range(n):
	rand_list.append(random.randint(3,9))
print(rand_list)

#2  Использование random.sample()
res = random.sample(range(1, 50), 7)

# printing result
print("Random number list is : " + str(res))

#3  Использование списочного понимания + randrange()
res = [random.randrange(1, 50, 1) for i in range(7)]

# printing result
print("Random number list is : " + str(res))

#4 Использование цикла + randint()
lis = []
for _ in range(10):
	lis.append(random.randint(0, 51))
print(lis)


#Случайное число с использованием Numpy!!

#5-1 Генерация списка случайных целых чисел с помощью функции numpy.random.randin
import numpy as np

print(list(np.random.randint(low = 3,high=8,size=10)))

print(list(np.random.randint(low = 3,size=5)))

#5-2 Генерация списка случайных плавающих значений с помощью функции numpy.random.random_sample

print(np.random.random_sample(size=4))

print(np.random.random_sample(size=(4, 4)))
