#!usr/bin/bash
day_value=$1

curl "https://adventofcode.com/2023/day/${day_value}/input" --header "Cookie: session=53616c7465645f5ffd8df0f4a5f9ab290bab47b491c1635f293b8a20ce07a35d25f7f4989252b1c0b3f923d331e5b1d7d86733e39de4f3d8a144dd152f87c41f" -o $1.txt
mv $1.txt inputs/$1.txt