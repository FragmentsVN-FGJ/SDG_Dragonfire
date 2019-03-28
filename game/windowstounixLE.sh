#!/bin/bash
# Convert Windows Line Endings to UNIX
for file in $(find)
do
    if [ "${file:(-4)}" == ".rpy" ]
	then
		echo "${file}"
		tr -d '\015' < ${file} > "${file}_unix"
        rm -rf ${file}
        mv ${file}_unix ${file}
	fi
done
