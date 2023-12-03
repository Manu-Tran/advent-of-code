#!/usr/bin/env sh

if [[ -z "$1" ]]; then
    echo "Usage : $0 \$YEAR \$DAY"
    exit
fi
if [[ -z "$2" ]]; then
    echo "Usage : $0 \$YEAR \$DAY"
    exit
fi
if [[ -z "$3" ]]; then
    DIR="."
else
    DIR=$3
fi

if [ ! -d "$DIR"/"$1"/day"$2" ]; then
    mkdir -p "$DIR"/"$1"/day"$2"
fi
curl https://adventofcode.com/"$1"/day/"$2" -A "github.com/curl/curl for emmanuel.tran@gmail.com" -H 'cookie: session='"$(cat ~/.config/aocd/token)"';' | markdownify | head -n -20 | tail -n +33 > "$DIR"/"$1"/day"$2"/README.md
