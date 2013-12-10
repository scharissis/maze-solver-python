#!/usr/bin/env python

"""
    Maze Solver
    
    Usage:
        python solve.py <maze-image-in>
    
    Output:
        An image of the original maze with the solution path drawn in.
    
    Note:
        This program relies on colors.
        For example, assumes explorable space is WHITE and the maze is BLACK.
"""

import os
import sys
import logging
from PIL import Image
from Queue import Queue

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')


class Solver:
    """
    file_in = Input maze image filename.
    image   = Maze image object.
    pixels  = Maze image pixel array.
    """
    def __init__(self, maze):
        # Colors.
        self.COLOR_RED = (255,0,0)
        self.COLOR_GREEN = (0,255,0)
        self.COLOR_BLUE = (0,0,255)
        self.COLOR_WHITE = (255,255,255)
        self.COLOR_BLACK = (0,0,0)
        self.START_COLOR = self.COLOR_RED
        self.END_COLOR = self.COLOR_BLUE
        self.FRONTIER_COLOR = self.COLOR_GREEN
        
        # TODO: START/END is currently hardcoded for 'maze_000.jpeg'.
        self.START = (400,984)
        self.END = (398,25)    
    
        # Output file.
        self.DIR_OUT = 'out'
        self.file_in = maze
        ext = maze.split('.')[-1]
        self.file_out = os.path.join(self.DIR_OUT, os.path.basename(maze).split('.')[0] + '.' + ext)
        
        # Output parameters.
        self.SNAPSHOT_FREQ = 10000 # Save an image every SNAPSHOT_FREQ steps.
        
        # Load image.
        self.image = Image.open(self.file_in)
        self.image = self.image.convert('RGB')
        self.pixels = self.image.load()
        self._cleanImage() 
        logging.info("Loaded image '{0}' ({1} pixels).".format(self.file_in, self.image.size))

    """
    Purify pixels to either pure black or white.
    """
    def _cleanImage(self):
        th = 256/2
        x,y = self.image.size
        for i in range(x):
            for j in range(y):
                r,g,b = self.pixels[i,j]
                if r > th and g > th and b > th:
                    self.pixels[i,j] = self.COLOR_WHITE
                else:
                    self.pixels[i,j] = self.COLOR_BLACK
                
    def solve(self):
        logging.info('Solving...')
        path = self._BFS(self.START, self.END)
        if path is None:
            logging.error('No path found.')
            self._drawX(base_pixels, self.START)
            self._drawX(base_pixels, self.END)
            self.image.save(self.file_out)
            sys.exit(1)
        
        # Draw solution path.
        for position in path:
            x,y = position
            self.pixels[x,y] = self.COLOR_RED   
        
        self.image.save(self.file_out)
        logging.info("Solution saved as '{0}'.".format(self.file_out))
        #self.image.show()

    def _drawX(self, pos, color=(255,0,0)):
        x,y = pos
        d = 10

        for i in range(-d,d):
            self.pixels[x+i,y] = color
        for j in range(-d,d):
            self.pixels[x,y+j] = color

    def _inBounds(self, dim, x, y):
        mx, my = dim
        if x < 0 or y < 0 or x >= mx or y >= my:
            return False
        return True

    def _isWhite(self, value):
        r,g,b = value
        th = 240
        if value == self.COLOR_WHITE or value == 0 or (r>th and g>th and b>th):
            return True

    # Left, Down, Right, Up
    def _getNeighbours(self, pos):
        x,y = pos
        return [(x-1,y),(x,y-1),(x+1,y),(x,y+1)]

    """
    Breadth-first search.
    """
    def _BFS(self, start, end):
        # Copy of maze to hold temporary search state.
        image = self.image.copy()
        pixels = image.load()
        
        self.iterations = 0
        Q = [[start]]
        img = 0
        
        while len(Q) != 0:
            path = Q.pop(0)
            pos = path[-1]
            
            if pos == end:
                # Draw solution path.
                for position in path:
                    x,y = position
                    pixels[x,y] = self.COLOR_RED
                image.save('tmp/{0:05d}.jpg'.format(img))
                logging.info('Found a path after {0} iterations.'.format(self.iterations))
                return path
            
            for neighbour in self._getNeighbours(pos):
                x,y = neighbour
                if self._inBounds(image.size, x, y) and self._isWhite(pixels[x,y]):
                    pixels[x,y] = self.FRONTIER_COLOR
                    new_path = list(path)
                    new_path.append(neighbour)
                    Q += [new_path]

            if self.iterations%self.SNAPSHOT_FREQ == 0:
                image.save('tmp/{0:05d}.jpg'.format(img))
                img += 1
            self.iterations += 1

        return None



if __name__ == '__main__':
    solver = Solver(sys.argv[1])
    solver.solve()
