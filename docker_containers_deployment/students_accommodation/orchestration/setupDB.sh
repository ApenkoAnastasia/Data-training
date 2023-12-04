#!/bin/bash

# get variables from config.txt
. ./properties/config.txt

# function for connection to DB
function check_connection {
  if mysql -u "$USERNAME" -p"$PASSWORD" -e "USE $DATABASE";
  then
    return 0
  else
      return 1
  fi
}

# function for creation database & table
function setup_db {
  if check_connection $CHECK_CONNECTION -eq 0 ;
  then
    echo "Database exists. Check it in DBeaver."
  else
    echo "Database DOESN'T exists. Let's create them."
    mysql -u "$USERNAME" -p"$PASSWORD" < ./db_admin/DDL/createDestinationDB.sql
    mysql -u "$USERNAME" -p"$PASSWORD" < ./db_admin/DDL/createRoomTable.sql
    mysql -u "$USERNAME" -p"$PASSWORD" < ./db_admin/DDL/createStudentTable.sql
    echo "We create databases. Check it in DBeaver."
  fi
}

# function for creation procedures
function create_procedures {
  if check_connection $CHECK_CONNECTION -eq 0 ;
  then
    echo "Connect to DB."
    mysql -u "$USERNAME" -p"$PASSWORD" < ./db_admin/DML/procedures/listRoomsWithDifferentSex.sql
    mysql -u "$USERNAME" -p"$PASSWORD" < ./db_admin/DML/procedures/listRoomsWithMaximumAverageAge.sql
    mysql -u "$USERNAME" -p"$PASSWORD" < ./db_admin/DML/procedures/listRoomsWithMinimalAverageAge.sql
    mysql -u "$USERNAME" -p"$PASSWORD" < ./db_admin/DML/procedures/listRoomsWithStudentsAmount.sql
    echo "We create procedures. Check it in DBeaver."
  else
    echo "Couldn't connect to DB."
  fi
}

setup_db;
create_procedures;
