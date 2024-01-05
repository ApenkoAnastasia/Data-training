#!/bin/bash

LOGFILE="/test_docker_log.log"

# stout, errors to log file
exec 3>&1 1>"$LOGFILE" 2>&1
trap "echo 'ERROR: An error occurred during execution, check log $LOGFILE for details.' >&3" ERR
trap '{ set +x; } 2>/dev/null; echo -n "[$(date -Is)]  "; set -x' DEBUG

echo "Hello-docker! We are inside!"

#----- test Python
echo "Testing Python: "
python3 -V
pip3 -V

#----- test MySQL DB
echo "Testing MySQL DB: "
service --status-all
service mysql start
echo "Next: enter your password to MySQL." >&3
mysql -u 'root' -p -e 'SHOW DATABASES;'

#----- test OS tools
echo "Testing directories: "

cd ../
if [ -e ./students_accommodation/source/rooms.json -a -e ./students_accommodation/source/students.json ]; then
	echo "Source files exists."
	cd ./students_accommodation/source
  head rooms.json
  head students.json
else
	echo "Couldn't find source files."
fi

exec 1>&- | 2>&- | 3>&-
