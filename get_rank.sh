#! /bin/bash


curl -s http://10.4.21.147:3000/getleaderboard\?id\=JVlzF9h4oeN3fyaOoSYgA1HiW82SlS1iptEqtB4lDQAeCK2k8C | tr '<' '\n' | tr '>' '\n' | grep -A4 team_95 | tail -n 1