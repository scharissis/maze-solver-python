Maze Solver
===

Usage example:
======
```
stefano@stefano-laptop:~/code/src/maze-solver$ ./solve_maze.sh mazes/maze_000.jpg
INFO: Loaded image 'mazes/maze_000.jpg' ((800, 1002) pixels).
INFO: Solving...
INFO: Found a path after 457955 iterations.
INFO: Solution saved as 'out/maze_000.jpg'.
Generating AVI...	out/maze_000.avi
Generating GIF...	out/maze_000.gif
```


Dependencies:
======
  * Package 'imagemagick' for the `convert` command:
  
  ```
  sudo apt-get install imagemagick
  ```
