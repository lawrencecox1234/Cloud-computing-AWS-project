#!/usr/bin/python3

import os
import html
import cgi
import cgitb
import random

#the code below contain modified code obtained from Lee Gillam from lab 5 page 10 from the Cloud Computing module
cgitb.enable()

print("Content-type: text/html\r\n\r\n")
form = cgi.FieldStorage()

shots2 = form.getvalue("shots", "(no shots)")
q_value2 = form.getvalue("q_value", "(no q_value)")

shots2 = int(shots2)
q_value2 = int(q_value2)

list1 = []
incircle = 0

number = shots2/q_value2
number = int(number)

for j in range(0,number):
    for i in range(1,q_value2+1):
        random1 = random.uniform(-1.0, 1.0)
        random2 = random.uniform(-1.0, 1.0)
        if((random1*random1 + random2*random2) < 1):
            incircle += 1
    list1.append(incircle)
    list1.append(q_value2)
    incircle = 0
    
print(list1)
