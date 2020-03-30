#!/bin/bash

if [ -z "$1" ]; then
    echo -e "\e[31mERROR: Please specify a new command name"
    echo -e "$(basename $0) NAME"
    exit 1
fi

newcmdfile="mgshell-$1".sh

if [ -f $newcmdfile ]; then
    echo -e "\e[31mERROR: $newcmdfile already exists, exiting..."
    exit 1
fi

cp mgshell-cmd.sh.template $newcmdfile
sed -i "s/\$COMM/${1,,}/g" $newcmdfile
sed -i "s/\$CAPCOMM/${1^^}/g" $newcmdfile

echo -e "\e[32mCreated $newcmdfile"