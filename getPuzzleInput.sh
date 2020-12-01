echo Which day is it?
read day
URL=https://adventofcode.com/2020/day/$day/input
dirName=./day$day
mkdir -p $dirName
curl $URL --output $dirName/input.txt --cookie ./Settings/cookies-adventofcode-com.txt
