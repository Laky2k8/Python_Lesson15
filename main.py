import pyfiglet as pyfiglet
import random



#Printing out a sequence from a famouse Hungarian poem.
task1 = pyfiglet.figlet_format("TASK  1")

Toldi = """TOLDI \n
ELSŐ ÉNEK. \n \n Ég a napmelegtől a kopár szík sarja,
Tikkadt szöcskenyájak legelésznek rajta;
Nincs egy árva fűszál a tors közt kelőben,
Nincs tenyérnyi zöld hely nagy határ mezőben.
Boglyák hűvösében tíz-tizenkét szolga
Hortyog, mintha legjobb rendin menne dolga;
Hej, pedig üresen, vagy félig rakottan,
Nagy szénás szekerek álldogálnak ottan."""

print(task1 , "\n")
print(Toldi, "\n \n \n")

#Calculating the volume of a cone.
task2 = pyfiglet.figlet_format("TASK  2")
print(task2 , "\n")

radius = int(input("Radius (units): "))
print("\n")
height = int(input("Height (units): "))
print("\n \n")
volume = (radius ** 2 * 3.14) * height / 3

print("The volume of this cone is ", volume, " units. \n \n \n")

#Swapping two variables with two methods.
task3 = pyfiglet.figlet_format("TASK  3")
print(task3 , "\n")

a = random.randint(0,10000)
b = random.randint(-10000,0)

print("We have two random varables. Those are A: ", a, " and B: ", b, ". \n")
print("We're gonna spaw these in two ways. \n \n")

print("1. THE LAZY METHOD")
print("a,b = b,a  \n")
a, b = b, a

print("A now is: ", a, " while B now is: ", b, "\n \n")

print("2. THE LOOOONG METHOD")
print("Using a temporary variable to swap these variables. Why would you do that though? \n")

temp = a
a = b
b = temp

print("A now is: ", a, " while B now is: ", b, "\n \n \n")

#Getting a list of numbers and then converting each of them into integers.
task4 = pyfiglet.figlet_format("TASK  4")
print(task4 , "\n")

superList = input("Please input a list of numbers seperated with columns: ")

x = superList.split(", ")

print("\n \n \n")

#We'll split a list by the even and odd numbers.
task5 = pyfiglet.figlet_format("TASK  5")
print(task5 , "\n")

numList = [1,2,5,6,8,9,12,25,32,48,56,99,134,357,179,12,78,34567, 7654332]
even = []
odd = []

i = 0

print("We have a list: ", numList)
print("We'll now split this list by the even and odd numbers. \n \n")

while i < len(numList):
    if i % 2 == 0:
        even.append(numList[i])
    else:
        odd.append(numList[i])
    i += 1

print("Our list's even numbers: ", even)
print("Our list's odd numbers: ", odd, "\n \n \n")

thx = pyfiglet.figlet_format("THANKS FOR USING THIS PROGRAM!")
print(thx , "\n")