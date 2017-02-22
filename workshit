import random

A1 = [random.randint(-1000, 1000) for i in range(1000)]
A2 = []
A3 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
A4 = [-5,-4,-3,-2,-1,0,1,2,3,4,5,78,123,435]

reference=(sorted(A1),sorted(A2),sorted(A3),sorted(A4))

#check func

def check(x,y):
    if not x==y:
        return 'You failed'
    return 'You win'

#function bubble_sort

def bubble_sort(array):
	counter=len(array)
	while counter>0:
		for i in range(len(array)-1):
			if array[i]>array[i+1]:
				array[i],array[i+1]=array[i+1],array[i]
		counter-=1
	return array

#function insert_sort

def insert_sort(array):
	for j in range(2,len(array)):
		key=array[j]
		i=j-1
		while i>=0 and array[i]>key:
			array[i+1]=array[i]
			i-=1
		array[i+1]=key
	return array

#handle sort
B=(insert_sort(A1),insert_sort(A2),insert_sort(A3),insert_sort(A4))
C=(bubble_sort(A1),bubble_sort(A2),bubble_sort(A3),bubble_sort(A4))

#check
print (check(reference,B))
print (check(reference,C))
