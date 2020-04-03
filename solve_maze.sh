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

exit 0

echo -n 'Generating GIF...'
# Resize images.
(
    cd "$TMP_DIR" || exit
    for img in $(ls *.jpg)
    do
	    convert "$img" -resize 40% "tmp.jpg"
	    mv "tmp.jpg" "$img"
    done
)

video2gif() {
  ffmpeg -y -i "${1}" -vf fps="${3:-10}",scale="${2:-320}":-1:flags=lanczos,palettegen "${1}.png"
  ffmpeg -i "${1}" -i "${1}.png" -filter_complex "fps=${3:-10},scale='bitand(oh*dar,65534)':'min(720,ih)':-1:flags=lanczos[x];[x][1:v]paletteuse" "${1}".gif
  rm "${1}.png"
}
video2gif "$OUT_VID"

#convert -delay 10 -loop 0 -layers optimize $( ls "$TMP_DIR/*.jpg" | $SORT ) $OUT_GIF
#ffmpeg -ss 30 -t 3 -i input.mp4 -vf "fps=10,scale=320:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 output.gif
ffmpeg -i "$OUT_VID" -loop 0 "$OUT_GIF"

echo -e "\t$OUT_GIF"