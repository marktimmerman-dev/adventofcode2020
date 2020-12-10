#!/bin/bash
(echo "ibase=2;"; cat input.txt | sed "s/[BR]/1/g" | sed "s/[FL]/0/g" | sort ) | bc > seats.txt
FIRST=`cat seats.txt | head -1`
LAST=`cat seats.txt | tail -1`
for (( i=$FIRST; i<= $LAST; i++))
do
    grep $i seats.txt > /dev/null || echo "$i is missing"
done
