echo "Setting up environment for first time..."

echo "Creating database"
sqlite3 system.db < db/tables.sql

echo "Setting up environment finished"
echo "_______________________________"
echo ""