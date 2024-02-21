import os
import random as rd

def mainLoop(): 
    snakeX = 2
    snakeY = 3
    gameX = 20
    gameY = 20
    
    grid = Grid(gameX, gameY)
    grid.replace('#', snakeX, snakeY)
    while True:
     
        grid.print()
        
        movement = getInput()
        os.system('clear')
        

        match movement:
            case 'up':
                snakeY += 1 
            case 'down':
                snakeY -= 1 
            case 'right':
                snakeX += 1 
            case 'left':
                snakeX -= 1 
        grid.replace('#', snakeX, snakeY)
    
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
            char = ''

def endGame():
    pass

mainLoop()