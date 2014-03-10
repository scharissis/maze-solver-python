## Maze Solver


Original | Searching... | Solved
-------- | ------------ | ------
<img src="https://raw.github.com/scharissis/maze-solver-python/master/mazes/maze_000.jpg" width="250px"> | <img src="https://raw.github.com/scharissis/maze-solver-python/master/out/maze_000.gif" width="250px"> | <img src="https://raw.github.com/scharissis/maze-solver-python/master/out/maze_000.jpg" width="250px">



#### Usage example:

```
stefano@stefano-laptop:~/code/src/maze-solver$ ./solve_maze.sh mazes/maze_000.jpg
INFO: Loaded image 'mazes/maze_000.jpg' ((800, 1002) pixels).
INFO: Solving...
INFO: Found a path after 457955 iterations.
INFO: Solution saved as 'out/maze_000.jpg'.
Generating AVI...	out/maze_000.avi
Generating GIF...	out/maze_000.gif
```



#### Dependencies:
  * Package 'imagemagick' for the `convert` command:
  
  ```
  sudo apt-get install imagemagick
  ```

  * for Mac using brew for the `convert`command:

  ```
  brew install imagemagick
  ```
  * for Mac using brew for the `avconv` command:

  ```
  brew install libav
  ```