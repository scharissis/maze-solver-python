#!/bin/bash

# Produces animations (avi & gif) of the search process.
# Usage example: ./solve_maze.sh mazes/maze_000.jpg

TMP_DIR=tmp
MAZE=$1
MAZE_NAME=$(basename "$MAZE")
OUT_GIF="out/${MAZE_NAME%.*}.gif"
OUT_VID="out/${MAZE_NAME%.*}.avi"

if [ -z "$MAZE" ]; then
	echo "Usage: $0 maze.jpg"; exit 1;
fi

SORT="sort -V"
if   ! find "$TMP_DIR" -maxdepth 1 -name *.jpg | "$SORT" >/dev/null 2>&1; then
	SORT="sort -k1"
fi

# Clean up old output files.
{
	rm "$TMP_DIR/*"
	rm "$OUT_GIF"
	rm "$OUT_VID"
} 2> /dev/null

# Solve.
if ! python3 solve.py "$MAZE"; then exit 1; fi

echo -n 'Generating video...'
ffmpeg -r 10 -pattern_type glob -i "$TMP_DIR/*.jpg" "$OUT_VID" -hide_banner -loglevel panic
echo -e "\t$OUT_VID"

echo -n 'Generating GIF...'
ffmpeg -i "$OUT_VID" -loop 0 "$OUT_GIF" -hide_banner -loglevel panic

echo -e "\t$OUT_GIF"