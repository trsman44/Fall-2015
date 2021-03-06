'''
Created on Sep 19, 2015

@author: Tyler
'''

from math import *


#------LISTS-----
roomNumber = []
roomTypes = []
roomAreas = []
#----------------


numRooms = int(input("How many rooms do you want to have? "))

#Used to define what the Square room area is
def squareRoom(base, height):
    roomArea = float(base * height)
    return roomArea
    
#Used to define what the SemiCircle room area is   
def semicircleRoom(radius):
    roomArea = (pi*(radius)**2) / 4
    return roomArea
    
#Used to define what the Triangle room area is 
def triangleRoom(base, height):
    roomArea = (base * height) / 2
    return roomArea
    




    
    
#--------------------USER INPUT--------------------


def room():
    while True:
        print("What shape do you want this room to be?\n")  #Asks what room you want
        room = str(input("Response: "))
        if room.lower() in ('square', 'semicircle', 'triangle'):    #If room is in set then do the following
            if room.lower() == 'square':                            #If square do:
                roomTypes.append('Square')    #Used to make the room type
                base = float(input("Base: "))
                height = float(input("Height: "))
                roomArea = squareRoom(base, height)
                roomAreas.append(roomArea)
                
                
            elif room.lower() == 'semicircle':                     #If SemiCircle do:
                roomTypes.append('SemiCircle')
                radius = float(input("Radius: "))
                roomArea = semicircleRoom(radius)
                roomAreas.append(roomArea)
                
                
            elif room.lower() == 'triangle':                       #If Triangle do:
                roomTypes.append('Triangle')
                base = float(input("Base: "))
                height = float(input("Height: "))
                roomArea = triangleRoom(base, height)
                roomAreas.append(roomArea)
                
            break
        else:
            print('Input was Wrong. Try Again.')            #Not a correct input, go back through

        
        
#--------------------------------------------------

def runProgram():       #Def to run program as many times as needed
    for i in range(numRooms):
        room()
        
runProgram()    #Runs program

#----------OUTPUT----------
print("The total area in each room is as follows: ")
x = 1
for i in range(numRooms):
    print("Room %d is:" % x, roomAreas[i])
    x = x + 1
print("The total room area is: ", sum(roomAreas))
#---------------------------