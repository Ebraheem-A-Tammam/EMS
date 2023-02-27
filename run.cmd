if [ -e system.db ]
then
    echo "running the program..."
    echo "______________________"
    echo ""
    python main.py
else
    ./init/init.cmd
    echo "running the program..."
    echo "______________________"
    echo ""
    python main.py
fi