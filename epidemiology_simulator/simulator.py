#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import math
from matplotlib import pyplot as plt

def normpdf(x, mean, sd):
    var = float(sd)**2
    denom = (2*math.pi*var)**.5
    num = math.exp(-(float(x)-float(mean))**2/(2*var))
    return num/denom
    
recover_time = 4
virality = 0.5
mortality_mean = 3
mortality_sd = 1

class Cell(object):

    def __init__(self,x, y):
        self.x = x
        self.y = y
        self.state = "S" 
        self.time = 0

    def process(self, adjacent_cells):
        if self.state == "I":
            if random.random() < normpdf(self.time, mortality_mean, \
                                         mortality_sd):
                self.state = "R"
            elif self.time >= recover_time: 
                self.state = "S"                
            else: 
                for cell in adjacent_cells:
                    if cell.state == "S":                                        
                        if random.random() < virality:
                            cell.infect()    
            self.time += 1
                                        
    def infect(self):
        self.state = "I"
        self.time = 0
    
class Map(object):
    
    def __init__(self, height, width):
        self.cells = {}
    
    def add_cell(self, lot):
        self.cells[lot.x, lot.y] = lot
 
    def adjacent_cells(self, x,y):

        test_cells = []
        if x > 0: #left 
            test_cells.append((x-1,y))
        if x < 149: #right
            test_cells.append((x+1,y))
        if y > 0: # up
            test_cells.append((x,y-1))
        if y < 149: # down
            test_cells.append((x,y+1))
        
        return [self.cells[x] for x in test_cells if x in self.cells]
           
    def time_step(self):
        for (x,y) in self.cells: 
            cell = self.cells[(x,y)]
            cell.process(self.adjacent_cells(x,y))
        self.display()

    def display(self):
        simu_map = []
        for i in range(150):
            simu_map.append(150*[(0,0,0)])
        for x,y in self.cells: 
            if self.cells[x,y].state == "I":
                simu_map[x][y] = (1,0,0)
            elif self.cells[x,y].state == "R":
                simu_map[x][y] = (0.5,0.5,0.5)
            else: 
                simu_map[x][y] = (0,1,0)
                
        plt.imshow(simu_map)
            
            
def read_map(filename):

    try: 
        result = Map(150,150)
        f = open(filename,'r')
        for line in f: 
            line = line.strip()
            x, y = line.split(',')
            if x and y:
                lot = Cell(int(x), int(y))
            result.add_cell(lot)
        return result    
        
    except FileNotFoundError:
        print('Could not find file {}'.format(filename))
        
        