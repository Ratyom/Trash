#function factorial

x=input('type your number for factorial ')

def factorial(x):
	result=1
	for i in range(1,x+1):
		result=result*i
	return result

print (factorial(int(x)))

#function fibonacci

n=input('type your number for fibonacci ')

def fibonacci(n):
	if n==0 or n==1:
		result=[0]	
	else:
		result=[0,1]
		for i in range(n-2):
			result.append(result[i]+result[i+1])
	return result

print (fibonacci(int(n)))

#function bubble_sort

a=input('type your list of numbers ')
string=''
array=[]

for element in a:
	if element.isdigit():
		string+=element
	else:
		string+=' '

string=string.split()

for element in string:
	array.append(int(element))

def bubble_sort(array):
	counter=len(array)
	while counter>0:	
		for i in range(len(array)-1):
			if array[i]>array[i+1]:
				array[i],array[i+1]=array[i+1],array[i]
		counter-=1
	return array	

print (bubble_sort(array))

#function insert_sort

b=input('type your list of numbers ')
string=''
array=[]

for element in b:
	if element.isdigit():
		string+=element
	else:
		string+=' '

string=string.split()

for element in string:
	array.append(int(element))

def insert_sort(array):
	for j in range(2,len(array)):
		key=array[j]
		i=j-1
		while i>=0 and array[i]>key:
			array[i+1]=array[i]
			i-=1
		array[i+1]=key
	return array	

print (insert_sort(array))
