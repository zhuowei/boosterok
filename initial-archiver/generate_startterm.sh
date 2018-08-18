#!/bin/bash
set -e
echo "exec gnome-terminal \\"
for a in `find $1 -name "run.sh"|sort`
do
	echo "--tab -e \"bash $a\" \\"
done
