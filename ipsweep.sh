#!/bin/bash
## This tool scans for active IP Addresses
if [ "$1" == "" ]
	then
	echo "You forgot an IP address!"
	echo "Syntax: ./ipsweep.sh 192.168.0"
else
	for ip in `seq 1 254`; do
	ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
	ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" >> ip.txt &
  done
fi


for ip in $(cat ip.txt); do nmap $ip; done

