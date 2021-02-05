#!/bin/bash

term=$1
 
if [[ ${term:0:1} != [[:upper:]] ]]
then
	echo "The term must start with Uppercase letter"
	exit 0
fi

file_name=$2
cde="https://en.wikipedia.org/wiki/"${term}

curl -# $cde > temp

if cat temp | grep -q "If a page was recently created here, it may not be visible yet" 
then	
	echo "No Article Found!!"
	exit 0
else
	echo "URL saved in output file"
	echo "URL for $1 : $cde" >> ${file_name}
fi