#!/usr/bin/env sh

if [[ -z "$1" ]]; then
    echo "Usage : $0 \$YEAR \$DAY"
    exit
fi
if [[ -z "$2" ]]; then
    echo "Usage : $0 \$YEAR \$DAY"
    exit
fi
curl https://adventofcode.com/"$1/day/"$2" -A "emmanuel.tran@gmail.com via curl" -H 'cookie: session='"$(cat ~/.config/aocd/token)"';' | markdownify | head -n -20 | tail -n +33 > README.md
