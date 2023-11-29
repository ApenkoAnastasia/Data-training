#!/bin/sh

echo "Hello-docker! We are inside!"

#----- test Python
echo "Testing Python: "
python3 -V
pip3 -V

#----- test MySQL DB
echo "Testing MySQL DB: "
#systemctl status mysql
service mysql status

#----- test OS tools
echo "Testing directories: "

#if [ -e /tmp/Datasets/ml-latest-small/movies.csv ]; then
#	echo "File csv exists."
#elif [ -e /tmp/ml-latest-small.zip ]; then
#	unzip /tmp/ml-latest-small.zip \*movies -d /tmp/Datasets
#	rm /tmp/ml-latest-small.zip
#else
#	curl -P /tmp https://files.grouplens.org/datasets/movielens/ml-latest-small.zip
#	unzip /tmp/ml-latest-small.zip \ml-latest-small/movies.csv -d /tmp/Datasets
#	rm /tmp/ml-latest-small.zip
#fi
#
#cd /tmp/Datasets/ml-latest-small
#head movies.csv
