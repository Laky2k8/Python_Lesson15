import pyfiglet as pyfiglet




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
print(Toldi, "\n \n")

#Calculating the volume of a cone.
task2 = pyfiglet.figlet_format("TASK  2")
print(task2 , "\n")

radius = int(input("Radius (units): "))
print("\n")
height = int(input("Height (units): "))
print("\n \n")
volume = (radius ** 2 * 3.14) * height / 3

print("The volume of this cone is ", volume, " units.")

