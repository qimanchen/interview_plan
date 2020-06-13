#!/bin/bash
#Function: test operation calculation
a=$1
# read -p "please input two interge: " a b
b=$2
echo "a-b=$(($a-$b))
echo "a+b=$(($a+$b))
echo "a*b=$(($a*$b))
echo "a/b=$(($a/$b))
echo "a**b=$(($a**$b))
echo "a%b=$(($a%$b))