#!/bin/bash

count=1
for i in $(seq $count)
do
  echo $i
  echo 'Run python.'
  python3 -m src.students_accommodation.main -sp "./source/students.json" -rp "./source/rooms.json" --max_avg 1 -lm 1 --min_avg 1
done

#python3 -m src.students_accommodation.main -sp "./source/students.json" -rp "./source/rooms.json" --max_avg 1 -lm 1 --min_avg 1
