A team of young engineers have built a robot
The robot can travel on a rectangular plane :
1. The rectangular plane is represented by a X-Y plane with bottom left as (0,0) and top right as
(M,N)
2. The rectangular plane contains multiple particles. A particle's position is represented by x and
y coordinates

The robot's movement :
1. Its position is represented by x and y coordinates and a letter representing one of the four
directions (N/S/E/W)
2. It takes in commands in the form of single letters. The possible letters are 'L', 'R' and 'M'.
   2.1 'L' and 'R' makes the robot turn 90 degrees left or right respectively, without moving from its current position.
   2.2 'M' means move forward one position and maintain the same direction.
3. It stops walking
   3.1 If it finds any particle on its way
   3.2 If it encounters any coordinate on its path which it had travelled earlier
   3.3 If the next command leads to a position outside rectangular plane

**INPUT**
1. The first line of input is the top-right coordinates of the rectangular plan (M, N),
2. Next two lines of input are about the robot
   2.1 first line gives the robot's starting position, X,Y coordinates and a letter, all 3 separated by
   spaces
   2.2 second line is a series of commands for the robot


The first line of input is the upper-right coordinates of the plateau, the lower-left coordinates are assumed to be 0,0.

The rest of the input is information pertaining to the rovers that have been deployed. Each rover has two lines of input. The first line gives the rover's position, and the second line is a series of instructions telling the rover how to explore the plateau. The position is made up of two integers and a letter separated by spaces, corresponding to the x and y co-ordinates and the rover's orientation.

Each rover will be finished sequentially, which means that the second rover won't start to move until the first one has finished moving.

**OUTPUT**

The output for each rover should be its final co-ordinates and heading.

1. Test Input
   4 4
   0 0 N
   MMMRMMLM

   Test Output

   2 4 N

2. Test Input
   4 4
   0 0 N
   MMRMRMRMR

   Test Output

   Rover will stop at this postion as rover has traveled earlier on this path (0, 1)

   Final coordinates of rover is 1 1 N




## Installing

Requirements : Python3

## How to run

python3 main.py

1. write size of grid
2. write coordinates for robot
3. write instruction for robot
