#! /usr/bin/env bash     
# the previous statement indicates to interpret this program using bash

#set -x  #uncomment for execution logging - try it

TARPGM="python ../src/mytar.py"

rm -rf dst
mkdir dst
(cd src; $TARPGM c *) | (cd dst; $TARPGM x)
if diff -r src dst
then
    echo "success" >&2		# error msg to stdout
    exit 0			# return success
else
    echo "failure" >&2
    exit 1			# return failure
fi
     

