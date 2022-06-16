#!/bin/bash
args=("$@")
if [ "$#" == "3" ]
    then 
    python astrophlocal/main.py --institute ${args[0]} --start_date ${args[1]} --end_date ${args[2]}
elif [ "$#" == "2" ]
    then 
    python astrophlocal/main.py --institute ${args[0]} --start_date ${args[1]}
elif [ "$#" == "1" ]
    then 
    python astrophlocal/main.py --institute ${args[0]}
else
    python astrophlocal/main.py
fi
open html/main.html
