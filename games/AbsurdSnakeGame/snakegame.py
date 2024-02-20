import os
import random as rd

def mainLoop(): 
    snakeX = 2
    snakeY = 3
    gameX = 10
    gameY = 5
    grid = Grid(gameX, gameY)
    
    while True:
     
        grid.print()
        
        movement = getInput()
        os.system('clear')
        
        grid.replace('#', snakeX, snakeY)
        match movement:
            case 'up':
                snakeY += 1 if gameY >snakeY >0
            case 'down':
                snakeY -= 1 if gameY >snakeY >0
            case 'right':
                snakeX += 1 if gameX >snakeX >0
            case 'left':
                snakeX -= 1 if gameX >snakeX >0

                
        
        
class Grid:
    grid =[]    
    def __init__(self, gridX, gridY):
        
        grid = []
        row = []
        
        for y in range(gridY):
            for x in range(gridX):
                row.append('·')
            grid.append(row)
            row = []
            
        self.grid = grid
        
    def replace(self, char, X , Y): #bool, return true if succesful
        try:
            self.grid[(len(self.grid)-Y)][X-1]= char   #grid[row (from top to bottom)[column]]
            return True
        except IndexError:
            return False



    def print(self):   #only accepts a x · y grid 
        X = len(self.grid[0])
        Y = len(self.grid)
        
        for row in self.grid:
            for x in row:
                print(x, end='  ')
            print('')
    
    

def getInput():
    
    inputDictionary = {'w':'up' , 'a':'left' , 's':'down' , 'd':'right'}
   
    while True:
        userInput = input()

        try:
            char = inputDictionary[userInput]
            print('lololo')
            return char
        except KeyError:
            print('error')
            char = ''

def endGame():
    pass

mainLoop()