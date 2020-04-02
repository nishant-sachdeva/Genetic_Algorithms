#! /bin/bash 


curl -s  http://10.4.21.147:3000/getusage | tr '<' '\n' | tr '>' '\n' | grep -A4 team_95 | tail -n 1
