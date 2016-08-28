#login and password
import time

file=open('dictionary.txt', 'w+')
file.write('admin:admin\ntyom:12345\nneo:follothewhiterabbit')
file.close()

file=open('dictionary.txt', 'r+')
string=file.read()
file.close()

string=string.split('\n')
for i in range(len(string)):
    string+=string[i].split(':')
string=string[i+1:]

dictionary={}

for i in range(0,len(string),2):
    dictionary[string[i]]=string[i+1]

login=input('Enter your login please: ')

def login_check(login):
    while login not in dictionary:
        login=input('This login doesn''t exist please enter again: ')
    password=input('Enter your password please: ')
    counter = 1
    time.sleep(3)
    return login, password, counter

login, password, counter = login_check(login)

while password!=dictionary.get(login):
    if counter==3:
        login=input('What the hell are you doing, now enter your login again: ')
        login, password, counter = login_check(login)
    password=input('Wrong password please enter it again:')
    time.sleep(3)
    counter+=1

print('You logged in, welcome dear,',login)