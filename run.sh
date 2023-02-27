if [ -e system.db ]
then
    echo "running the program..."
    echo "______________________"
    echo ""
    python3 main.py
else
    ./init/init.sh
    echo "running the program..."
    echo "______________________"
    echo ""
    python3 main.py
fi