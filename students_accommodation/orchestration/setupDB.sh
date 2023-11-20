#!/bin/bash

# get variables from config.txt
. ./properties/config.txt

function check_connection {
  if mysql -u "$USERNAME" -p"$PASSWORD" -e "USE $DATABASE";
  then
    return 0
  else
      return 1
  fi
}

# create database & table
function setup_db {
  if check_connection $CHECK_CONNECTION -eq 0 ;
  then
    echo "Database exists. Check it in DBeaver."
#    mysql -u "$USERNAME" -p"$PASSWORD" < ./db_admin/DML/truncate/truncateDestinationTables.sql
#    mysql -u "$USERNAME" -p"$PASSWORD" < ./db_admin/DML/procedures/selectResultsProcedure.sql
  else
    echo "Database DOESN'T exists. Check it in DBeaver. Let's create them."
    mysql -u "$USERNAME" -p"$PASSWORD" < ./db_admin/DDL/createDestinationDB.sql
    mysql -u "$USERNAME" -p"$PASSWORD" < ./db_admin/DDL/createRoomTable.sql
    mysql -u "$USERNAME" -p"$PASSWORD" < ./db_admin/DDL/createStudentTable.sql
    echo "We create databases. Check it in DBeaver."
  fi
}


setup_db;
