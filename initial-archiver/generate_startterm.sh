#!/bin/bash
set -e
echo "exec gnome-terminal \\"
for a in `find $1 -name "run.sh"|sort`
do
	dir=$(dirname $a)
	echo "--tab -e \"bash ./launch_tab.sh $dir\" \\"
done
