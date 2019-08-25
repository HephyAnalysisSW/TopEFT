# recover a corrupted sqlite DB
# First argument: path
# Second argument: DB name

DB_NAME=$1
DB_PATH=$2

echo "Repairing database file $DB_NAME in $DB_PATH"
echo '.dump'|sqlite3 $DB_PATH/$DB_NAME|sqlite3 $DB_PATH/repaired_$DB_NAME
mv $DB_PATH/$DB_NAME $DB_PATH/corrupt_$DB_NAME
mv $DB_PATH/repaired_$DB_NAME $DB_PATH/$DB_NAME
