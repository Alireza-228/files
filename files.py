# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 14:02:20 2026

@author: GostarNetwork
"""

# files 

file = open("data.txt" , "w")

file.write("name ; alireza ,/ family :akbari ,/ age :22")

file.close()

print(file)

print('------------------------------------')

file = open("data.txt" , "r")

content = file.read()

print(content)

file.close()

print("------------------------------------------")


file = open("data.txt" , "a")

file.write("/n mohammad")

file.close()

print("------------------------------------")


file1 = open("newdata.txt" , "w")

file1.write("my first file")

file1.close()

print("----------------------------------")


with open("data2.txt" , "w") as file2:
    content = file2.write("salam")
    
print(content)
    
print("--------------------------------")


with open("data2.txt" , "r") as file2:
    content = file2.read()
    
print(content)

print("---------------------------------")


name = input("Enter your name: ")

score = input("Enter your score: ")

with open("students.txt", "a") as file:

    file.write(name + " : " + score + "\n")

print("Information saved!")


print("------------------------------------------")

file = open("test83.text","w")

file.write("hello alireza")
file.write("/n hi alireza")

file.close()

print("------------------------------------")

file = open("test83.text" , "r")

file82 = file .read()

print(file82)

file.close()

print("--------------------------------------")

file = open("test83.text", "a")

file.write("/n age = 22 , city = shahrebabak")

file.close()

print("----------------------------------------")

with open("test81.text","w") as file80 :
    file80.write("hello alireza akbari")
    
    
name = input(" enter your name: ")
famili = input("enter your famili : ")
age = input("enter your age : ")



with open("test28.text" , "w") as file28:
    file28.write(name)
    file28.write(famili)
    file28.write(age)
    
    
    



























