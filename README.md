## Maze Solver


Original | Searching... | Solved
-------- | ------------ | ------
<img src="https://raw.github.com/scharissis/maze-solver-python/master/mazes/maze_000.jpg" width="250px"> | <img src="https://raw.github.com/scharissis/maze-solver-python/master/out/maze_000.gif" width="250px"> | <img src="https://raw.github.com/scharissis/maze-solver-python/master/out/maze_000.jpg" width="250px">



## Usage

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
 * Package 'imagemagick' for the `convert` command.
 * Package 'libav' for the `avconv` command.
  
 * Ubuntu:
 
   ```
   sudo apt-get install imagemagick libav-tools
   ```
 * Mac:
 
   ```
   brew install imagemagick libav
   ```

### Packages
```
virtualenv venv
. ./venv/bin/activate
pip3 install -r requirements.txt
```
