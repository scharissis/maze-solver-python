## Maze Solver


Original | Searching... | Solved
-------- | ------------ | ------
<img src="https://raw.github.com/scharissis/maze-solver-python/master/mazes/maze_000.jpg" width="250px"> | <img src="https://raw.github.com/scharissis/maze-solver-python/master/out/maze_000.gif" width="250px"> | <img src="https://raw.github.com/scharissis/maze-solver-python/master/out/maze_000.jpg" width="250px">



## Usage
There is a python script which solves the input image and outputs a solution image with the path it found.
Additionally, if you'd like to generate a GIF or MP4 of the process, you use the shell script.

### Solve and output image
```
$ python3 solve.py mazes/maze_63423.jpg
```

### Solve and output gif & avi
```
$ ./solve_maze.sh mazes/maze_000.jpg
```

### Installation

### Dependencies:

### System
OPTIONAL: package `ffmpeg` for generating mp4 and gif.
If you just want to output an image, these are not needed.

### Packages
```
virtualenv venv
. ./venv/bin/activate
pip3 install -r requirements.txt
```
