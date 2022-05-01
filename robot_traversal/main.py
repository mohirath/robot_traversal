#!/usr/bin/python3
# initialise global variables
# amount of rovers that you want to traverse
from ast import Or


rover_count = 1
# direction list
direction = ['N', 'E', 'S', 'W']
# movement of rovers, 1 grid point
move = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
# commands sent to rovers
instructions = {'L': 'tleft', 'R': 'tright', 'M': 'move'}
class Rover:
    """
    calculate and return position of rovers based on input paramters
    """

    def __init__(self, x, y, xmax, ymax, bearing, intersection):
        """
        initialise parameters
        """
        self.x = x
        self.y = y
        self.xmax = xmax
        self.ymax = ymax
        self.bearing = bearing
        self.intersection = set(intersection)

    def tright(self):
        """
        turning right method
        """
        self.bearing = direction[(direction.index(self.bearing) + 1) % len(direction)]

    def tleft(self):
        """
        turning left method
        """
        self.bearing = direction[(direction.index(self.bearing) - 1) % len(direction)]

    def move(self):
        """
        moving forward 1 grid point method
        """

        xmod = self.x + move[self.bearing][0]
        ymod = self.y + move[self.bearing][1]
        #print(self.intersection)
        # check intersection to see if nrover is not the same position as mrover
        #if (xmod, ymod) not in self.intersection:     
        if (xmod, ymod) in self.intersection:
            print("Rover will stop at this postion as rover has traveled earlier on this path", (xmod,ymod))
            print("Final coordinates of rover is", (self.x, self.y))
            exit()
        elif (xmod, ymod) not in self.intersection:
            
            if xmod <= self.xmax and xmod >= 0 and ymod <= self.ymax and ymod >= 0:
                self.x = xmod
                self.y = ymod
                self.intersection.add((xmod,ymod))
                #print(xmod,ymod)
            else:
                print('Out of bounds try again!!')
                exit()
        else:
            print('Rovers are on the same spot, try again!!')
            exit()


if __name__ == '__main__':
   
    # get grid size from input
    xmax, ymax = map(int, input('grid:').split())
    # initialise intersection rovers soon to be positions
    intersection = set([])
    check_coords = []
    results = []
    # count_a for rover_count for loop
    count_a = 1
    # count_b for instructions for loop
    count_b = 1
    # iterate over rover count
    for _ in range(rover_count):
        # get rover coordinates and NESW bearing
        x, y, bearing = input('coordinates for rover %d:' % count_a).split()
        intersection.add((int(x), int(y)))
        count_a += 1
        # check to see that you havent deployed rovers with the same coordinates
        if [x, y, bearing] not in check_coords:
            check_coords.append([x, y, bearing])
            rover = Rover(int(x), int(y), xmax, ymax, bearing, intersection)
            # iterate over instructions string
            for i in input('instructions for rover %d:' % count_b):
                if i not in 'MRL':
                    # exit if not valid instruction
                    print('Invalid Instruction "%s": use M or R or L - please try again' % i)
                    exit()
                else:
                    # store and run instructions
                    getattr(rover, instructions[i])()
            count_b += 1
            # add nrovers coords to intersection
            intersection.add((rover.x, rover.y))
            results.append((rover.x, rover.y, rover.bearing))
        else:
            print('2 or more of your rovers can not share the same spot, please try again')
            exit()
    # print results
    for x, y, z in results:
        print("Final coordinates of rover is", x, y, z)
