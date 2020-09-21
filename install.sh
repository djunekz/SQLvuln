#!/bin/bash

LIBRARY_PATH="/usr/include/"

if [ $# -eq 0 ];
then
    echo "INSTALL: $0 main.cpp"
    echo "Install Successful. . ."
    exit
fi

if [ -d "/usr/bin" ] || [ -d "/usr/include/"];
then
    sudo cp -r curl $LIBRARY_PATH
    sudo apt-get install libcurl4-gnutls-dev -y
    g++ $1 -std=c++11 -lcurl -o dork
    printf "\nCompile command: g++ main.cpp -std=c++11 -lcurl -o dork\nRUN: ./dork\n"
else
    echo "Sorry, this tool not available on your operating system"
fi
