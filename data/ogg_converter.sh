#!/bin/sh

# convert all mid files to ogg
for fname in *.mid
do
    oggname=`echo $fname | sed 's/.mid/.ogg/'`
    mscore -o $oggname $fname
done