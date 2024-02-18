import os
import time


def mainLoop(): 
    while True:
        print(getInput())
        
    
    
def draw():
    pass

def getInput():
    
    inputDictionary = {'w':'top' , 'a':'left' , 's':'bottom' , 'd':'right'}
    input = input()
    
    while True:
        try:
            char = inputDictionary[input]
            return char
        except IndexError:
            pass

def endGame():
    pass

main()