#!/bin/bash
(echo "ibase=2;"; cat input.txt | sed "s/[BR]/1/g" | sed "s/[FL]/0/g" | sort | tail -1) | bc
